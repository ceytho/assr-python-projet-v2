
# Manuel d'utilisation

Squelette d'exemple simplifié de la documentation à rendre :
- sous format PDF = points normaux
- sous format Markdown = points bonus

## Introduction

Le script `server.py` permet de [décrire brièvement ce que fait le serveur...]
Il expose une API REST qui [...]

## Prérequis

1. Python ??? (préciser la version minimale)

2. Fichier de données : `weather-data.csv` (format CSV avec séparateur `;`)

3. Bibliothèques / dépendances tierces (si applicable) :
   - ???

## Fichier de configuration

Description des clés du fichier **config.ini** :

| Section | Clé | Description | Valeur par défaut |
|---------|-----|-------------|-------------------|
| `server` | `host` | ??? | `127.0.0.1` |
| `server` | `port` | ??? | `8080` |
| `data` | `path` | ??? | `./weather-data.csv` |

## Installation

```bash
# Cloner / décompresser l'archive
???

# Installer les dépendances (si requirements.txt non vide)
pip install -r requirements.txt
```

## Lancer le serveur

```bash
python server.py
```

Le serveur écoute sur `http://127.0.0.1:8080` par défaut.

## Routes disponibles

| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/data` | ??? |
| GET | `/data?city=<ville>` | ??? |
| GET | `/stats` | ??? |
| GET | `/html` | ??? |

## Exemples d'utilisation

```bash
# Récupérer toutes les données
curl http://127.0.0.1:8080/data

# Filtrer par ville
curl "http://127.0.0.1:8080/data?city=Paris"

# Statistiques
curl http://127.0.0.1:8080/stats
```
