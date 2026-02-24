# Projet Python - API Hubeau

## Contexte

L'objectif de ce projet est de mettre en pratique les connaissances en Python
que vous avez acquises jusqu'ici, avec une mise en situation qui se rapproche de
ce que vous pourrez rencontrer dans un contexte professionnel.

Votre client souhaite consulter la dureté de l'eau du robinet dans différentes
communes de France. Ces données sont fournies par l'API publique Hub'eau,
maintenue par le Ministère de la Transition Écologique. Votre mission est de
développer un **serveur HTTP intermédiaire** qui interroge cette API et met en
cache les réponses pour limiter les appels extérieurs

## Consignes

Votre script devra :
- récupérer les paramètres (URL de l'API, TTL, limite de requêtes, etc.) depuis
  un fichier de configuration
- interroger l'API Hub'eau pour récupérer les mesures de dureté de l'eau
- mettre en cache les réponses (clé, valeur, TTL configurable) en mémoire
- gérer les erreurs courantes (API indisponible, paramètre manquant, limite
  de requêtes atteinte, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8

La bibliothèque `requests` est autorisée pour les appels HTTP vers Hub'eau.
Si vous utilisez d'autres bibliothèques tierces, les indiquer dans `requirements.txt`.

### Routes à implémenter

```
GET /hardness?code_reseau=<code>          <- mesures de dureté pour un réseau
GET /hardness?code_reseau=<code>&size=<n> <- avec un nombre de résultats personnalisé
GET /cache                                <- état actuel du cache (nb entrées, etc.)
GET /health                               <- vérification que le serveur tourne
```

Toute route inconnue doit retourner une erreur 404.
Un paramètre manquant ou invalide doit retourner une erreur 400.
Un client ayant dépassé sa limite de requêtes doit recevoir une erreur 429.

Les réponses doivent être en JSON avec le bon `Content-Type`.

### Format de réponse attendu

**`GET /hardness?code_reseau=077001506`** :
```json
{
  "cached": false,
  "count": 3,
  "data": [
    {
      "commune": "Melun",
      "departement": "Seine-et-Marne",
      "date": "2024-01-15",
      "hardness_f": 28.5,
      "unit": "degré français (degré hydrotimétrique)",
      "distributor": "Nom du distributeur",
      "network": "Nom du réseau"
    }
  ]
}
```

Le champ `cached` indique si la réponse provient du cache ou d'un appel frais
à l'API Hub'eau.

### API Hub'eau

L'endpoint à utiliser est le suivant :

```
https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis
```

Paramètres pertinents :
- `code_parametre=1345` (dureté de l'eau, fixe)
- `code_reseau` (code du réseau de distribution)
- `size` (nombre de résultats)
- `sort=desc` (du plus récent au plus ancien)

La documentation complète est disponible sur https://hubeau.eaufrance.fr/

### Bonus (optionnel)

- bonus : ajouter la possibilité de surcharger la configuration via des
  paramètres de ligne de commande
- bonus : logging des requêtes dans un fichier
- bonus : tri ou filtrage supplémentaire des résultats (par commune, par date)
- bonus : implémenter un rate limiting par adresse IP
- bonus avancé : utiliser Redis comme backend de cache à la place du dict mémoire
- bonus avancé : utiliser `asyncio` et `aiohttp` à la place de `requests`
- bonus avancé : containeriser le serveur avec Docker

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3/
|-- config.ini          <- votre fichier de configuration
|-- README.md           <- une documentation d'installation et d'utilisation
|-- requirements.txt    <- vos dépendances tierces
`-- server.py           <- votre script
```

À envoyer à l'adresse avec présentation orale : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle de Python est votre meilleure alliée :

- `http.server` : https://docs.python.org/3/library/http.server.html
- `urllib.parse` : https://docs.python.org/3/library/urllib.parse.html
- `time` : https://docs.python.org/3/library/time.html
- `configparser` : https://docs.python.org/3/library/configparser.html
- Documentation Hub'eau : https://hubeau.eaufrance.fr/

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse participer et que ça puisse profiter à tous.
