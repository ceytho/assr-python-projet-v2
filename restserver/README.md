# Projet Python - Serveur HTTP REST

## Contexte

Votre équipe a collecté des relevés météorologiques pour
plusieurs villes françaises au cours des dernières semaines. Ces données sont
stockées dans un fichier CSV. D'autres services applicatifs de votre organisation
ont besoin d'accéder à ces données via une API REST. Vous avez besoin d'un premier prototype à leur mettre à disposition avant que ces données soient mises au propre dans une vraie base de données et exposées avec les outils traditionnels.

Votre mission est de développer un **serveur HTTP minimaliste** en Python capable
d'exposer ces données via une API REST, **sans utiliser de framework web** (pas
de Flask, FastAPI, Django, etc).

## Consignes

Votre serveur devra :

- Lire les données météo depuis un fichier CSV au démarrage
- Servir une **API REST** avec les routes décrites ci-dessous
- Récupérer les paramètres (chemin vers le CSV, port d'écoute, etc.) depuis un
  **fichier de configuration**
- Gérer les erreurs courantes (fichier CSV introuvable, port déjà utilisé, route
  inconnue: 404, paramètre invalide: 400, etc.)
- Être découpé en **fonctions** (une par responsabilité)
- Être conforme au guide de style **PEP8**

### Contraintes techniques

- Utiliser **uniquement la bibliothèque standard** Python pour le serveur HTTP
  (`http.server` ou `socket`)
- Le parsing des routes et des paramètres de requête doit être fait **manuellement**
- Les réponses de l'API doivent être en **JSON** avec le bon `Content-Type`
- Si vous utilisez des bibliothèques tierces, les lister dans `requirements.txt`

### Routes obligatoires

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET` | `/data` | Retourne toutes les données CSV en JSON |
| `GET` | `/data?city=<ville>` | Filtre les relevés par ville |
| `GET` | `/data?min_temp=<n>` | Filtre les relevés dont la température est ≥ n |
| `GET` | `/data?max_temp=<n>` | Filtre les relevés dont la température est ≤ n |
| `GET` | `/stats` | Retourne des statistiques agrégées (count, min, max, moyenne) |
| `GET` | `/html` | Retourne une page HTML dynamique présentant les données dans un tableau |

Les filtres de `/data` peuvent être **combinés** (ex: `?city=Paris&min_temp=15`).

### Format de réponse attendu

**`GET /data`** :
```json
[
  {"city": "Paris", "date": "2024-11-01", "temp_c": 12.3, "humidity_pct": 78},
  {"city": "Lyon",  "date": "2024-11-01", "temp_c": 14.1, "humidity_pct": 65}
]
```

**`GET /stats`** :
```json
{
  "count": 42,
  "temp_c": {"min": 2.1, "max": 28.5, "avg": 14.3},
  "humidity_pct": {"min": 30, "max": 95, "avg": 67.2}
}
```

**`GET /html`** :
Page HTML valide avec un tableau `<table>` présentant les relevés, un titre,
et a minima un style CSS inline.

### Bonus (optionnel)

- **Pagination** sur `/data` avec les paramètres `?page=1&limit=10`
- **Cache mémoire** : ne pas relire le CSV à chaque requête (chargement au démarrage)
- **Logging** des requêtes reçues dans un fichier de log
- **Tri** des résultats via `?sort=temp_c&order=desc`
- **Docker** : un `Dockerfile` et un `docker-compose.yml` pour containeriser le serveur
- Documentation en **Markdown** au lieu de PDF (voir barème)

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) contenant :

```
NOM1_NOM2_NOM3/
├── config.ini          <- votre fichier de configuration
├── README.md           <- documentation d'installation et d'utilisation
├── requirements.txt    <- dépendances tierces (peut être vide)
├── server.py           <- votre script principal
└── weather-data.csv    <- votre fichier de données (peut être enrichi)
```

À envoyer à l'adresse avec présentation : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle de Python est votre meilleure alliée :

- [`http.server`](https://docs.python.org/3/library/http.server.html)
- [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html)
  (parsing des query strings)
- [`csv`](https://docs.python.org/3/library/csv.html)
- [`json`](https://docs.python.org/3/library/json.html)
- [`configparser`](https://docs.python.org/3/library/configparser.html)

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse en bénéficier.
