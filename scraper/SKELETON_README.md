
# Manuel d'utilisation

Squelette d'exemple simplifié de la documentation à rendre :
- sous format PDF = points normaux
- sous format Markdown = points bonus

## Introduction

Le script `script.py` permet de [décrire brièvement ce que fait le script...]
Il télécharge les pages du site [...] et extrait [...]

## Prérequis

1. Python ??? (préciser la version minimale)

2. Une connexion internet (pour télécharger les pages du site)

3. Bibliothèques / dépendances tierces :
   - `requests` : ???
   - `beautifulsoup4` : ???
   - autres : ???

## Fichier de configuration

Description des clés du fichier **config.ini** :

| Section | Clé | Description |
|---------|-----|-------------|
| `scraper` | `start_url` | ??? |
| `scraper` | `base_url` | ??? |
| `scraper` | `max_pages` | ??? |
| `scraper` | `timeout` | ??? |
| `output` | `path` | ??? |

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

Le fichier CSV est généré dans `???` par défaut.

## Exemple de sortie

```
Page 1/5 : 20 livres récupérés
Page 2/5 : 20 livres récupérés
...
Export terminé : 100 livres enregistrés dans books.csv
```
