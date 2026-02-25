
# Manuel d'utilisation

Squelette d'exemple simplifié de la documentation à rendre :
- sous format PDF = points normaux
- sous format Markdown = points bonus

## Introduction

Le script `script.py` permet de [décrire brièvement ce que fait le script...]
Il télécharge des fichiers CSV depuis le bucket S3 [...] et génère [...]

## Prérequis

1. Python ??? (préciser la version minimale)

2. Une connexion internet (pour accéder au bucket S3 public NOAA)

3. Bibliothèques / dépendances tierces :
   - `boto3` : ???
   - autres : ???

## Fichier de configuration

Description des clés du fichier **config.ini** :

| Section | Clé | Description |
|---------|-----|-------------|
| `s3` | `bucket` | ??? |
| `s3` | `region` | ??? |
| `s3` | `keys` | ??? |
| `filter` | `min_temp_f` | ??? |
| `filter` | `max_temp_f` | ??? |
| `output` | `csv_path` | ??? |
| `output` | `report_path` | ??? |

## Installation

```bash
# Décompresser l'archive
???

# Installer les dépendances
pip install -r requirements.txt
```

## Lancer le script

```bash
python3 script.py
```

## Exemple de sortie

```
Téléchargement de 2023/72594024233.csv...
  365 enregistrements récupérés
Téléchargement de 2023/72278024233.csv...
  365 enregistrements récupérés
Après nettoyage et filtrage : 710 enregistrements
Données exportées dans output.csv
Rapport généré dans report.json
```

## Fichiers produits

- `output.csv` : données nettoyées et filtrées, séparateur `;`
- `report.json` : rapport de traitement avec statistiques
