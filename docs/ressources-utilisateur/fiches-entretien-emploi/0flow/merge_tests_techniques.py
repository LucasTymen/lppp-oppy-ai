#!/usr/bin/env python3
"""Insère la section Tests techniques (modèle canonique) dans la fiche 0Flow."""
import os

base = os.path.dirname(os.path.abspath(__file__))
fiche_path = os.path.join(base, "fiche-entretien-0flow.html")
body_path = os.path.join(base, "_section2_body_only.html")
out_path = os.path.join(base, "fiche-entretien-0flow.html")

with open(fiche_path, "r", encoding="utf-8") as f:
    fiche = f.read()
with open(body_path, "r", encoding="utf-8") as f:
    panel_content = f.read()

new_section = '''    <!-- 3. TESTS TECHNIQUES — Programmation & Growth -->
    <button class="accordion">💻 3. TESTS TECHNIQUES — Programmation & Growth</button>
''' + panel_content + '''

    <!-- 4. QUESTIONS À POSER À 0FLOW -->
    <button class="accordion">❓ 4. Questions à poser à 0Flow</button>
    <div class="panel">
        <ul>
            <li>"Quelle est la part du Shadow IT dans les use cases que vous résolvez le plus ?"</li>
            <li>"Comment gérez-vous l'interopérabilité avec les SI legacy (on-premise) de vos gros clients ?"</li>
            <li>"Quels sont vos objectifs de réduction du CAC sur le segment Grands Comptes cette année ?"</li>
            <li>"Comment gérez-vous le cycle de vente long du B2B ?" (nurturing, contenu à haute valeur)</li>
        </ul>
    </div>
'''

# Repérer le bloc à remplacer (de "<!-- 3. QUESTIONS" jusqu'à la fin du panel Questions, avant "<!-- 4. 0FLOW")
start_marker = "    <!-- 3. QUESTIONS À POSER À 0FLOW -->"
end_marker = "    <!-- 5. 0FLOW — CE QUE VOUS DEVEZ SAVOIR -->"
idx_start = fiche.find(start_marker)
idx_end = fiche.find(end_marker)
if idx_start == -1 or idx_end == -1:
    print("ERREUR: marqueurs non trouvés. start=", idx_start, "end=", idx_end)
else:
    old_block = fiche[idx_start:idx_end]
    fiche = fiche[:idx_start] + new_section + fiche[idx_end:]

# Renuméroter section 4 -> 5 (0Flow)
fiche = fiche.replace("<!-- 4. 0FLOW — CE QUE VOUS DEVEZ SAVOIR -->", "<!-- 5. 0FLOW — CE QUE VOUS DEVEZ SAVOIR -->")
fiche = fiche.replace("🏢 4. 0Flow — Ce que vous devez savoir", "🏢 5. 0Flow — Ce que vous devez savoir")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(fiche)
print("OK: section Tests techniques insérée, sections 4 et 5 renumérotées.")
