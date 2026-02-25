# Projet Python - Audit de dépendances

## Contexte

L'objectif de ce projet est de mettre en pratique les connaissances en Python
que vous avez acquises jusqu'ici, avec une mise en situation qui se rapproche de
ce que vous pourrez rencontrer dans un contexte professionnel.

Pour ce projet vous devrez vérifier que les dépendances Python d'un projet
ne présentent pas de vulnérabilités connues, pour cela vous avez à disposition
un catalogue (CSV ou SQLite au choix) avec un champ `package` et un champ
`version`.

## Consignes

Votre script devra :
- récupérer les paramètres (chemin vers le catalogue, URL de l'API, etc.) depuis
  un fichier de configuration
- parcourir le catalogue de paquets
- vérifier chaque paquet contre l'API du site https://osv.dev/
- sortir un fichier CSV contenant le résultat de l'analyse
- servir un serveur HTTP (sans cache) exposant les résultats de l'analyse
- gérer les erreurs courantes (fichier introuvable, API injoignable, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8
- bonus : ajouter la possibilité de surcharger la configuration via des
  paramètres de ligne de commande

Si vous utilisez des bibliothèques tierces (non dans la stdlib), il faut les
indiquer dans un fichier nommé `requirements.txt`, à rendre avec le projet.

En sortie votre script devra afficher le résultat du test pour chaque paquet.
Exemple :

```
$ python3 script.py
package             version     vulns
------------------- ----------- -----
requests            2.25.0          2
pillow              9.0.0           3
cryptography        38.0.0          4
jinja2              3.0.0           1
numpy               1.21.0          0
```

### Serveur HTTP

Le serveur doit écouter sur un port configurable et répondre en JSON avec le bon `Content-Type`.

#### Routes à implémenter

```
GET /audit                                      <- audit complet du catalogue
GET /audit?package=<nom>&version=<version>      <- audit d'un paquet spécifique
GET /health                                     <- vérification que le serveur tourne
```

Toute route inconnue doit retourner une erreur 404.
Un paramètre manquant ou invalide doit retourner une erreur 400.

#### Format de réponse attendu

**`GET /audit`** :
```json
{
  "count": 5,
  "vulnerable": 4,
  "results": [
    { "package": "requests",     "version": "2.25.0", "vulns": 2 },
    { "package": "pillow",       "version": "9.0.0",  "vulns": 3 },
    { "package": "cryptography", "version": "38.0.0", "vulns": 4 },
    { "package": "jinja2",       "version": "3.0.0",  "vulns": 1 },
    { "package": "numpy",        "version": "1.21.0", "vulns": 0 }
  ]
}
```

**`GET /audit?package=requests&version=2.25.0`** :
```json
{
  "package": "requests",
  "version": "2.25.0",
  "vulns": 2,
  "ids": ["GHSA-j8r2-6x86-q33q", "PYSEC-2023-74"]
}
```

### Bonus (optionnel)

- bonus : support du format SQLite pour le catalogue (driver configurable) et pour l'export
- bonus : ajouter la possibilité de surcharger la configuration via des
  paramètres de ligne de commande
- bonus : filtrer l'affichage pour ne montrer que les paquets vulnérables
- bonus avancé : containeriser le script avec Docker

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3/
|-- config.ini          <- votre fichier de configuration
|-- README.md           <- une petite documentation d'installation et d'utilisation, c'est toujours utile
|-- requirements.txt    <- vos dépendances tierces, s'il y en a
|-- script.py           <- votre script
`-- packages.*          <- votre catalogue de paquets
```

À envoyer à l'adresse avec présentation orale : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle de Python est votre meilleure alliée :

- `configparser` : https://docs.python.org/3/library/configparser.html
- `csv` : https://docs.python.org/3/library/csv.html
- `sqlite3` : https://docs.python.org/3/library/sqlite3.html
- `json` : https://docs.python.org/3/library/json.html
- `http.server` : https://docs.python.org/3/library/http.server.html
- `urllib.parse` : https://docs.python.org/3/library/urllib.parse.html
- Documentation OSV API : https://google.github.io/osv.dev/api/

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse participer et que ça puisse profiter à tous.
