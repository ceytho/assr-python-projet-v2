
# Manuel d'utilisation

Squelette d'exemple simplifie de la documentation a rendre :
- sous format PDF = points normaux
- sous format Markdown = points bonus

## Introduction

Le script `server.py` permet de [decrire brievement ce que fait le serveur...]
Il interroge l'API Hub'eau pour [...] et met en cache [...]

## Prerequis

1. Python ??? (preciser la version minimale)

2. Une connexion internet (pour interroger l'API Hub'eau)

3. Bibliotheques / dependances tierces :
   - `requests` : ???
   - autres : ???

## Fichier de configuration

Description des cles du fichier **config.ini** :

| Section | Cle | Description |
|---------|-----|-------------|
| `server` | `host` | ??? |
| `server` | `port` | ??? |
| `hubeau` | `api_url` | ??? |
| `cache` | `ttl` | ??? |
| `rate_limit` | `max_requests` | ??? |
| `rate_limit` | `window_seconds` | ??? |

## Installation

```bash
# Decompresser l'archive
???

# Installer les dependances
pip install -r requirements.txt
```

## Lancer le serveur

```bash
python server.py
```

Le serveur ecoute sur `http://127.0.0.1:8080` par defaut.

## Routes disponibles

| Methode | Route | Description |
|---------|-------|-------------|
| GET | `/hardness?code_reseau=<code>` | ??? |
| GET | `/cache` | ??? |
| GET | `/health` | ??? |

## Exemples d'utilisation

```bash
# Durete de l'eau pour un reseau
curl "http://127.0.0.1:8080/hardness?code_reseau=077001506"

# Etat du cache
curl http://127.0.0.1:8080/cache

# Verification que le serveur tourne
curl http://127.0.0.1:8080/health
```
