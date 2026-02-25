# Projet Python - Analyse de logs serveur

## Contexte

L'objectif de ce projet est de mettre en pratique les connaissances en Python
que vous avez acquises jusqu'ici, avec une mise en situation qui se rapproche de
ce que vous pourrez rencontrer dans un contexte professionnel.

L'administrateur système de votre organisation souhaite analyser les logs
d'accès du serveur web pour identifier les tendances, détecter les erreurs et
repérer les comportements suspects. Votre mission est d'écrire un script Python
qui parse ces logs bruts et produit des rapports exploitables dans plusieurs
formats.

## Consignes

Votre script devra :
- lire et parser un fichier de logs au format Nginx combined avec temps de réponse
- extraire pour chaque ligne : IP source, date, méthode HTTP, endpoint, code de
  statut, taille de la réponse, temps de réponse
- calculer des statistiques globales sur l'ensemble des requêtes
- exporter les données parsées dans un fichier CSV
- exporter les statistiques dans un fichier JSON
- générer un rapport de synthèse au format HTML
- récupérer les paramètres (chemins, nombre de résultats à afficher, etc.)
  depuis un fichier de configuration
- gérer les erreurs courantes (fichier introuvable, ligne malformée, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8

Aucune bibliothèque tierce n'est requise. Tout est réalisable avec la
bibliothèque standard Python (`re`, `csv`, `json`, `collections`).

### Format du fichier de logs

Le fichier fourni utilise le format Nginx combined étendu avec le temps de
réponse en fin de ligne :

```
192.168.1.10 - alice [24/Feb/2026:10:00:01 +0000] "GET /api/users HTTP/1.1" 200 2048 "-" "Mozilla/5.0" 0.045
```

Les champs dans l'ordre sont :
1. adresse IP
2. ident (généralement `-`)
3. utilisateur authentifié (ou `-`)
4. date et heure entre crochets
5. requête entre guillemets (méthode, chemin, protocole)
6. code de statut HTTP
7. taille de la réponse en octets (ou `-`)
8. referer entre guillemets
9. user-agent entre guillemets
10. temps de réponse en secondes

### Statistiques à calculer

Le script doit calculer les statistiques suivantes sur l'ensemble des
enregistrements parsés :

- `total_requests` : nombre total de requêtes
- `top_ips` : liste des N adresses IP les plus actives (avec le nombre de requêtes)
- `top_endpoints` : liste des N endpoints les plus consultés (avec le nombre de requêtes)
- `status_codes` : répartition des codes de statut HTTP
- `avg_response_time_s` : temps de réponse moyen en secondes
- `error_rate` : proportion de requêtes avec un code >= 400
- `potential_bruteforce` : liste des IPs ayant effectué plus de
  `bruteforce_threshold` requêtes avec un code 401 ou 403

La valeur de N (nombre de résultats à afficher) est configurable.

### Formats de sortie

**`report.csv`** — une ligne par requête parsée, avec en-tête, séparateur `;` :

```
ip;datetime;method;path;status;size;response_time
192.168.1.10;24/Feb/2026:10:00:01 +0000;GET;/api/users;200;2048;0.045
```

**`report.json`** — statistiques globales :

```json
{
  "total_requests": 500,
  "top_ips": [["192.168.1.10", 150], ["10.0.0.1", 80]],
  "top_endpoints": [["/api/users", 120], ["/", 90]],
  "status_codes": {"200": 350, "404": 80, "500": 20},
  "avg_response_time_s": 0.045,
  "error_rate": 0.2,
  "potential_bruteforce": ["10.0.0.99"]
}
```

**`report.html`** — page HTML de synthèse contenant au minimum :
- un tableau récapitulatif des statistiques globales
- un tableau des N IPs les plus actives
- un tableau des N endpoints les plus consultés
- une alerte si des IPs suspectes ont été détectées

### Bonus (optionnel)

- bonus : filtrage par plage de dates ou par code de statut avant le calcul
  des statistiques
- bonus : détection affinée du brute force (fenêtre de temps configurable)
- bonus avancé : génération de graphiques avec `matplotlib` intégrés dans le
  rapport HTML (sous forme d'images encodées en base64)
- bonus avancé : containeriser le script avec Docker

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3/
|-- access.log          <- le fichier de logs fourni (peut être enrichi)
|-- config.ini          <- votre fichier de configuration
|-- README.md           <- une documentation d'installation et d'utilisation
|-- requirements.txt    <- vos dépendances tierces, s'il y en a
`-- script.py           <- votre script
```

À envoyer à l'adresse avec présentation : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle de Python est votre meilleure alliée :

- `re` : https://docs.python.org/3/library/re.html
- `csv` : https://docs.python.org/3/library/csv.html
- `json` : https://docs.python.org/3/library/json.html
- `collections.Counter` : https://docs.python.org/3/library/collections.html#collections.Counter
- `configparser` : https://docs.python.org/3/library/configparser.html

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse participer et que ça puisse profiter à tous.
