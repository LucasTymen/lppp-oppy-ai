# Google Cloud Console — OAuth pour n8n (éviter les blocages)

**Objectif** : Configurer correctement l’ID client OAuth dans Google Cloud Console pour que les agents n8n (Gmail, Google Sheets, Google Drive, etc.) fonctionnent **sans être bloqués** après coup.

**Contexte** : Projet Google Cloud type **LPPP-generator-personnal-bot** (ou équivalent) ; écran « Créer un ID client OAuth » avec **Origines JavaScript autorisées** et **URI de redirection autorisés**.

**Pilotes** : Automatizer (n8n), DevOps (hébergement n8n), Chef de Projet (validation accès).

---

## 1. Ce qu’il faut mettre dans la Google Cloud Console

### Origines JavaScript autorisées (Authorized JavaScript origins)

« À utiliser avec les requêtes provenant d’un navigateur. »  
Il faut indiquer **l’origine exacte** où n8n est accessible (schéma + domaine + port, **sans** chemin ni slash final).

| Environnement | URI à ajouter |
|---------------|----------------|
| **n8n en local (Docker / localhost)** | `http://localhost:5678` |
| **n8n en production (votre domaine)** | `https://votre-domaine-n8n.com` (sans slash final, sans chemin) |

**Conseil** : ajouter **dès maintenant** local + prod si vous prévoyez les deux (évite de modifier l’OAuth plus tard et de re-valider).

---

### URI de redirection autorisés (Authorized redirect URIs)

« À utiliser avec les requêtes provenant d’un serveur Web. »  
Google redirige ici après la connexion OAuth. n8n utilise un **callback** dédié.

| Environnement | URI à ajouter |
|---------------|----------------|
| **n8n en local** | `http://localhost:5678/rest/oauth2-credential/callback` |
| **n8n en production** | `https://votre-domaine-n8n.com/rest/oauth2-credential/callback` |

**Important** : l’URL de redirection doit être **exactement** celle qu’affiche n8n quand vous créez une credential Google (voir § 2). En cas de doute, **récupérer l’URL dans n8n d’abord**, puis la coller dans la Google Cloud Console.

---

## 2. Récupérer l’URL exacte depuis n8n (recommandé)

1. Dans n8n : **Settings** (ou **Paramètres**) → **Credentials** (ou **Credentials** dans le menu) → **Add credential** → choisir **Google** (OAuth2 API ou le type utilisé).
2. Dans l’écran de création de la credential, n8n affiche en général une **« OAuth Redirect URL »** ou **« Redirect URL to use »**.
3. **Copier cette URL** et l’ajouter telle quelle dans Google Cloud Console → **URI de redirection autorisés** (puis **+ Ajouter un URI**).
4. Ne pas inventer d’URL : si n8n est derrière un proxy ou un tunnel, l’URL peut être différente (ex. tunnel ngrok). Toujours utiliser celle indiquée par n8n.

---

## 3. Checklist pour ne pas être bloqué après

| # | Action |
|---|--------|
| 1 | **Type d’application** : « Application Web » (Web application) pour l’ID client OAuth. |
| 2 | **Origines JavaScript** : au moins `http://localhost:5678` (local) ; si vous avez une URL n8n en prod, l’ajouter aussi. |
| 3 | **URI de redirection** : au moins `http://localhost:5678/rest/oauth2-credential/callback` ; ou l’URL exacte fournie par n8n. En prod, ajouter l’équivalent avec votre domaine n8n. |
| 4 | **Écran de consentement OAuth** : si l’app est en « Test », les comptes de test doivent être ajoutés (utilisateurs autorisés). En « Production », validation Google possible — garder le projet cohérent (nom, domaine). |
| 5 | **Pas d’URL générique** : Google n’accepte pas `http://*` ou des wildcards. Une entrée par origine / redirect exacte. |

---

## 4. Exemple de remplissage (écran « Créer un ID client OAuth »)

- **Origines JavaScript autorisées**  
  - URI 1 : `http://localhost:5678`  
  - (optionnel) URI 2 : `https://n8n.votredomaine.com`

- **URI de redirection autorisés**  
  - URI 1 : `http://localhost:5678/rest/oauth2-credential/callback`  
  - (optionnel) URI 2 : `https://n8n.votredomaine.com/rest/oauth2-credential/callback`

Ensuite : **Créer** → récupérer **Client ID** et **Client Secret** → les entrer dans n8n dans la credential Google.

---

## 5. Niveaux d’accès (scopes / champs d’application)

Sur l’écran **Accès aux données** (OAuth consent screen), le bouton **« Ajouter ou supprimer des niveaux d’accès »** ouvre une liste de **champs d’application** (scopes). Il faut en ajouter **uniquement ceux dont n8n a besoin** pour limiter les refus Google et les révisions.

### Règle

- **Moindre privilège** : ne cocher que les scopes correspondant aux **nœuds Google** que vous utilisez dans n8n (Gmail, Sheets, Drive, etc.).
- **Recherche** : utiliser le champ **« Filtrer »** (en haut de la modale) et taper le nom de l’API (ex. `Gmail`, `Sheets`, `Drive`) pour afficher les scopes concernés.

### Souvent nécessaires (base OAuth)

| Scope (exemple) | Description | À cocher si |
|-----------------|-------------|-------------|
| `../auth/userinfo.email` | Afficher l’adresse e-mail du compte Google | Oui (souvent requis pour identifier l’utilisateur) |
| `../auth/userinfo.profile` | Consulter les infos de profil | Souvent oui (OAuth de base) |
| `openid` | Lier l’utilisateur à son compte Google | Oui si vous utilisez OpenID |

### Selon l’usage n8n

| Usage n8n | Mots-clés à taper dans Filtrer | Exemples de scopes à ajouter |
|-----------|--------------------------------|------------------------------|
| **Gmail** (lire / envoyer des mails) | `Gmail` | Gmail API : lecture, envoi (ex. `gmail.readonly`, `gmail.send`, `gmail.modify` selon la doc n8n) |
| **Google Sheets** (lire / écrire des feuilles) | `Sheets` ou `Spreadsheet` | Google Sheets API : `spreadsheets`, `spreadsheets.readonly` selon besoin |
| **Google Drive** (fichiers) | `Drive` | Drive API : `drive`, `drive.readonly`, `drive.file` selon besoin |
| **BigQuery** (visible dans ta capture) | `BigQuery` | BigQuery : `bigquery`, `bigquery.readonly` uniquement si tes workflows utilisent BigQuery |

**À éviter si inutile** : ne pas ajouter `../auth/cloud-platform` (accès très large) ni des scopes BigQuery / Cloud Storage si vous n’utilisez que Gmail ou Sheets. Moins de scopes = moins de risque de blocage ou de revue Google.

### Après avoir coché les scopes

Valider (ex. **« Mettre à jour »** / **« Enregistrer »**), puis revenir à la création de l’ID client OAuth si besoin. Les scopes choisis s’affichent dans « Vos champs d’application sensibles » ou « non sensibles » selon le type.

---

## 6. Références

- n8n : [Google OAuth2 (generic)](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic) — redirect URL et configuration.
- Google Cloud : **APIs & Services** → **Identifiants** → **Créer des identifiants** → **ID client OAuth**.
- Projet LPPP : `enrichissement-osint-flowise-n8n.md`, `info-automatizer-pour-equipe.md` (rôle Automatizer, n8n).

---

*Document créé pour configurer Google Cloud OAuth une seule fois et éviter les erreurs « redirect_uri_mismatch » ou blocages après mise en prod. Dernière mise à jour : 2025-02-03.*
