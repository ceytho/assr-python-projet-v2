# Projet Python - Traitement de données S3

## Contexte

L'objectif de ce projet est de mettre en pratique les connaissances en Python
que vous avez acquises jusqu'ici, avec une mise en situation qui se rapproche de
ce que vous pourrez rencontrer dans un contexte professionnel.

Votre équipe a besoin de traiter des relevés météorologiques journaliers mis à
disposition par la NOAA (National Oceanic and Atmospheric Administration) via
un bucket S3 public. Ces données brutes contiennent des valeurs manquantes et
nécessitent un nettoyage avant utilisation. Votre mission est d'écrire un script
Python qui télécharge un fichier, nettoie les données et génère un fichier de
sortie exploitable.

## Consignes

Votre script devra :
- récupérer les paramètres (bucket, clé S3, chemins, etc.) depuis un
  fichier de configuration
- se connecter au bucket S3 public de la NOAA **sans credentials AWS**
- télécharger un fichier CSV S3 spécifié dans la configuration
- nettoyer les données (valeurs manquantes encodées en `9999.9`)
- exporter les données traitées dans un nouveau fichier CSV
- générer un rapport de traitement au format JSON
- gérer les erreurs courantes (fichier introuvable, bucket inaccessible, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8

La bibliothèque `boto3` est obligatoire pour accéder à S3.
Si vous utilisez d'autres bibliothèques tierces, les indiquer dans `requirements.txt`.

### Accès anonyme à S3

Pour accéder à un bucket public sans credentials AWS, utilisez la configuration
suivante lors de la création du client boto3 :

```python
import boto3
from botocore import UNSIGNED
from botocore.config import Config

client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
```

### Bucket et format des données

Le bucket public de la NOAA est le suivant :

```
s3://noaa-gsod-pds/
```

Les fichiers sont organisés par année et par station :

```
s3://noaa-gsod-pds/2025/A5125600451.csv
```

Chaque fichier CSV contient les relevés journaliers d'une station pour une année.
Les colonnes utiles pour ce projet sont :

| Colonne | Description | Valeur manquante |
|---------|-------------|-----------------|
| `STATION` | Identifiant de la station | - |
| `DATE` | Date au format `YYYY-MM-DD` | - |
| `NAME` | Nom de la station | - |
| `TEMP` | Température moyenne journalière (°F) | `9999.9` |
| `MAX` | Température maximale (°F) | `9999.9` |
| `MIN` | Température minimale (°F) | `9999.9` |

### Traitement attendu

1. **Téléchargement** : récupérer le fichier indiqué dans la configuration
2. **Nettoyage** : remplacer les `9999.9` par une valeur nulle (champ vide
   dans le CSV de sortie)
3. **Export** : écrire les données traitées dans un CSV avec séparateur `;`
4. **Rapport** : générer un fichier JSON contenant des statistiques

### Format du rapport JSON

```json
{
  "total_records": 365,
  "valid_temp_records": 360,
  "missing_temp": 5,
  "temp_f": {
    "min": -5.2,
    "max": 98.3,
    "avg": 52.1
  },
  "date_range": {
    "from": "2023-01-01",
    "to": "2023-12-31"
  },
  "stations": ["72594024233", "72278024233"]
}
```

### Bonus (optionnel)

- bonus : filtrage des enregistrements selon une plage de température
  (`min_temp_f`, `max_temp_f`)
- bonus : support de plusieurs fichiers S3 dans la configuration
- bonus : filtrage supplémentaire par plage de dates (`min_date`, `max_date`)
- bonus : traitement par lots (chunking) pour les grands fichiers
- bonus avancé : téléchargement concurrent de plusieurs fichiers avec
  `threading`
- bonus avancé : containeriser le script avec Docker

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3/
|-- config.ini          <- votre fichier de configuration
|-- README.md           <- une documentation d'installation et d'utilisation
|-- requirements.txt    <- vos dépendances tierces
`-- script.py           <- votre script
```

À envoyer à l'adresse avec présentation : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle est votre meilleure alliée :

- `boto3` S3 : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
- `csv` : https://docs.python.org/3/library/csv.html
- `json` : https://docs.python.org/3/library/json.html
- `configparser` : https://docs.python.org/3/library/configparser.html
- Documentation NOAA GSOD : https://www.ncei.noaa.gov/data/global-summary-of-the-day/

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse participer et que ça puisse profiter à tous.
