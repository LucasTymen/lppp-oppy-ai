"""
Scoring configurable par expressions sécurisées (inspiré SquidResearch data_nodes).
Utilisé pour noter les prospects, prioriser les contenus, filtrer par seuil.
"""
import ast
import operator
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

SAFE_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

SAFE_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

SAFE_FUNCTIONS = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
}


def safe_eval_expression(expression: str, context: Dict[str, Any]) -> Any:
    """
    Évalue une expression mathématique simple de manière sécurisée.
    Variables fournies dans context (ex. email_score, company_score, has_contact).
    Opérateurs : +, -, *, /, %, **. Fonctions : abs, round, min, max.
    """
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Expression vide")

    try:
        parsed = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"Expression invalide: {expression}") from exc

    def _evaluate(node: ast.AST) -> Any:
        if isinstance(node, ast.Expression):
            return _evaluate(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Constante non supportée")
        if getattr(ast, "Num", None) and isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Name):
            if node.id in context:
                return context[node.id]
            raise ValueError(f"Variable non autorisée: {node.id}")
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in SAFE_BINARY_OPERATORS:
                raise ValueError(f"Opérateur non autorisé: {op_type}")
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            return SAFE_BINARY_OPERATORS[op_type](left, right)
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in SAFE_UNARY_OPERATORS:
                raise ValueError(f"Opérateur unaire non autorisé: {op_type}")
            operand = _evaluate(node.operand)
            return SAFE_UNARY_OPERATORS[op_type](operand)
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Appel de fonction non autorisé")
            func_name = node.func.id
            if func_name not in SAFE_FUNCTIONS:
                raise ValueError(f"Fonction non autorisée: {func_name}")
            if node.keywords:
                raise ValueError("Arguments nommés non autorisés")
            args = [_evaluate(arg) for arg in node.args]
            return SAFE_FUNCTIONS[func_name](*args)
        raise ValueError(f"Expression non supportée: {type(node).__name__}")

    return _evaluate(parsed)


# Formule par défaut : score sur 100 à partir de sous-scores
DEFAULT_SCORE_EXPRESSION = "min(100, round(email_score + company_score + contact_score))"


def score_prospect(
    *,
    has_email: bool = False,
    has_company: bool = False,
    has_contact_name: bool = False,
    enriched_completeness: float = 0.0,
    expression: str = DEFAULT_SCORE_EXPRESSION,
) -> float:
    """
    Calcule un score prospect (0–100) à partir de critères de complétude.
    Sous-scores : email 40, company 30, contact 20, enriched 10 (répartitions modulables).
    """
    email_score = 40.0 if has_email else 0.0
    company_score = 30.0 if has_company else 0.0
    contact_score = 20.0 if has_contact_name else 0.0
    # enriched_completeness attendu en 0.0–1.0, on le ramène à 10 pts max
    enriched_score = min(10.0, max(0.0, enriched_completeness * 10.0))

    context = {
        "email_score": email_score,
        "company_score": company_score,
        "contact_score": contact_score,
        "enriched_score": enriched_score,
        "has_email": 1 if has_email else 0,
        "has_company": 1 if has_company else 0,
        "has_contact": 1 if has_contact_name else 0,
    }
    try:
        result = safe_eval_expression(expression, context)
        return float(result) if result is not None else 0.0
    except (ValueError, TypeError) as e:
        logger.warning("Scoring prospect failed: %s", e)
        return 0.0
