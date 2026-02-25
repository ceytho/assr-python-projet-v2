
# Manuel d'utilisation

Squelette d'exemple simplifié de la documentation à rendre :
- sous format PDF = points normaux
- sous format Markdown = points bonus

## Introduction

Le script `script.py` permet d'analyser un fichier de logs serveur au format
Nginx combined. Il extrait [...] et génère trois rapports : [...]

## Prérequis

1. Python ??? (préciser la version minimale)

2. Fichier d'entrée : `access.log` (format Nginx combined avec temps de réponse)

3. Bibliothèques / dépendances tierces :
   - aucune (bibliothèque standard uniquement)

## Fichier de configuration

Description des clés du fichier **config.ini** :

| Section | Clé | Description |
|---------|-----|-------------|
| `input` | `log_path` | ??? |
| `analysis` | `top_n` | ??? |
| `analysis` | `bruteforce_threshold` | ??? |
| `output` | `csv_path` | ??? |
| `output` | `json_path` | ??? |
| `output` | `html_path` | ??? |

## Installation

```bash
# Décompresser l'archive
???

# Aucune dépendance à installer (bibliothèque standard uniquement)
```

## Lancer le script

```bash
python3 script.py
```

## Exemple de sortie

```
30 lignes parsées
Rapports générés : report.csv, report.json, report.html
```

## Fichiers produits

- `report.csv` : toutes les requêtes parsées, séparateur `;`
- `report.json` : statistiques globales (top IPs, endpoints, codes HTTP...)
- `report.html` : rapport de synthèse lisible dans un navigateur
