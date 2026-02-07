# Intégration d’une vidéo YouTube dans une landing

**Objectif** : Intégrer **n’importe quelle** vidéo YouTube (hero ou autre) sans reproduire l’erreur 153 et avec un fallback utilisateur.  
**Pour** : Dev Django, Designer, tout agent qui ajoute une vidéo YouTube à une landing.  
**Référence erreur** : `erreurs-et-solutions.md` § « YouTube embed — Erreur 153 ».

---

## 1. Règle à ne pas reproduire

- **Erreur 153** vient en priorité du **serveur** : si la **page** est servie avec `Referrer-Policy: same-origin` (défaut Django depuis 3.1), l’iframe YouTube ne reçoit pas le Referer et YouTube renvoie l’erreur 153. Il faut que la **réponse HTTP** de la page ait `Referrer-Policy: strict-origin-when-cross-origin`.
- **Côté projet LPPP** : `lppp/settings.py` définit **`SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"`** (obligatoire pour les embeds YouTube). Ne pas repasser à `same-origin` ni supprimer ce réglage.
- Sur l’**iframe**, garder **`referrerpolicy="strict-origin-when-cross-origin"`** en complément.
- **Toujours** prévoir un **lien de secours** « Regarder la vidéo sur YouTube » (filtre `youtube_watch_url`) au cas où l’embed échoue.

---

## 2. Filtres template à utiliser

Dans `apps/landing_pages/templatetags/landing_filters.py` :

| Filtre | Usage |
|--------|--------|
| `youtube_embed_background` | URL embed pour fond hero : autoplay, mute, loop, sans contrôles (youtube-nocookie.com). Peut déclencher l’Erreur 153 sur certains environnements. |
| `youtube_embed_no_autoplay` | URL embed **sans autoplay**, contrôles visibles (`autoplay=0`, `controls=1`, `modestbranding=1`). **À privilégier** quand l’embed avec autoplay renvoie l’Erreur 153 : l’utilisateur clique sur lecture dans le lecteur. Souvent plus fiable. |
| `youtube_watch_url` | URL de visionnage `https://www.youtube.com/watch?v=ID`. À utiliser pour le **lien de secours** « Ouvrir sur YouTube ». |

Les deux filtres acceptent indifféremment :
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID` (avec ou sans paramètres `?si=...`)

---

## 3. Checklist : ajouter une vidéo YouTube (hero)

1. **Donnée** : renseigner `hero_video_url` dans le `content_json` de la landing (migration ou admin). Ex. : `https://www.youtube.com/watch?v=0btaHttkokc` ou `https://www.youtube.com/embed/0btaHttkokc`.
2. **Template** (ex. `proposition.html`) :
   - **iframe** : `src="{{ content.hero_video_url|youtube_embed_background }}"` + **obligatoire** : `referrerpolicy="strict-origin-when-cross-origin"`.
   - **Lien de secours** : `<a href="{{ content.hero_video_url|youtube_watch_url }}" target="_blank" rel="noopener noreferrer">Regarder la vidéo sur YouTube</a>` (à afficher seulement si `content.hero_video_url|youtube_watch_url` est non vide, ex. avec `{% with watch_url=... %}{% if watch_url %}...{% endif %}{% endwith %}`).
3. **Vue** : si le template utilise `content.hero_video_url`, s’assurer que la clé existe (ex. via `_content_with_defaults` pour les templates concernés, ou valeur vide par défaut).

**Exemple iframe minimal (à réutiliser)** :

```html
<iframe src="{{ content.hero_video_url|youtube_embed_background }}"
        referrerpolicy="strict-origin-when-cross-origin"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen loading="eager" title="Fond hero"></iframe>
{% with watch_url=content.hero_video_url|youtube_watch_url %}
{% if watch_url %}
<a href="{{ watch_url }}" target="_blank" rel="noopener noreferrer" class="hero-video-fallback">Regarder la vidéo sur YouTube</a>
{% endif %}
{% endwith %}
```

---

## 4. Vidéo YouTube ailleurs qu’en hero

Pour une vidéo YouTube **hors hero** (ex. section démo, encart) :

1. Utiliser les **mêmes filtres** (`youtube_embed_background` pour lecture automatique / fond, ou construire une URL embed classique avec `youtube_watch_url` + lien « Voir sur YouTube »).
2. **Toujours** ajouter `referrerpolicy="strict-origin-when-cross-origin"` sur l’iframe.
3. Proposer un **lien de secours** vers `{{ url|youtube_watch_url }}` si l’embed peut échouer.

---

## 6. Références

- **Registre erreurs** : `erreurs-et-solutions.md` § « YouTube embed — Erreur 153 ».
- **Code** : `apps/landing_pages/templatetags/landing_filters.py`, `templates/landing_pages/proposition.html` (section hero avec `hero_video_url`).
