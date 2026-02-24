# Projet Python - Web Scraper

## Contexte

L'objectif de ce projet est de mettre en pratique les connaissances en Python
que vous avez acquises jusqu'ici, avec une mise en situation qui se rapproche de
ce que vous pourrez rencontrer dans un contexte professionnel.

Votre équipe de data analysts souhaite constituer un catalogue de livres avec
leurs prix, notes et disponibilités à partir d'un site web public. Votre mission
est de développer un script Python capable de récupérer automatiquement ces
données page par page, et de les exporter dans un fichier CSV réutilisable.

## Consignes

Votre script devra :
- récupérer les paramètres (URL de départ, chemin de sortie, etc.) depuis un
  fichier de configuration
- télécharger les pages HTML du site cible
- extraire les données de chaque livre (titre, prix, note, disponibilité, URL)
- exporter les résultats dans un fichier CSV
- gérer les erreurs courantes (page inaccessible, timeout, structure inattendue)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8

L'utilisation de `BeautifulSoup` est autorisée pour parser le HTML. Un parsing
manuel avec les modules `re` ou `html.parser` de la bibliothèque standard est
également accepté. L'utilisation de `Selenium` est **interdite**.

Si vous utilisez des bibliothèques tierces, les indiquer dans `requirements.txt`.

### Site à scraper

```
https://books.toscrape.com/
```

Ce site est un catalogue de démonstration conçu spécifiquement pour
l'apprentissage du scraping. Il contient 1000 livres répartis sur 50 pages.
Pour le socle obligatoire, une seule page suffit.

### Données à extraire

Pour chaque livre, votre script doit extraire :
- `title` : titre complet du livre
- `price` : prix affiché (ex: `£51.77`)
- `rating` : note sur 5 (entier de 1 à 5)
- `availability` : disponibilité (ex: `In stock`)
- `url` : URL relative ou absolue de la page du livre

### Format de sortie

En cours d'exécution, le script doit afficher sa progression :

```
$ python3 script.py
Page traitée : 20 livres récupérés
Export terminé : 20 livres enregistrés dans books.csv
```

Le fichier CSV de sortie utilise le séparateur `;` et l'encodage UTF-8 :

```
title;price;rating;availability;url
A Light in the Attic;£51.77;3;In stock;a-light-in-the-attic_1000/index.html
Tipping the Velvet;£53.74;1;In stock;tipping-the-velvet_999/index.html
```

### Bonus (optionnel)

- bonus : parcourir plusieurs pages en suivant les liens de pagination
- bonus : rendre le nombre de pages à parcourir configurable (`max_pages`)
- bonus : détection de changement de structure (avertir si les sélecteurs
  attendus sont absents de la page téléchargée)
- bonus : filtrage des résultats par note minimale ou prix maximum
- bonus : mode reprise (ne pas re-scraper les pages déjà traitées si le
  script est interrompu)
- bonus avancé : scraping concurrent avec `threading` ou `asyncio`
- bonus avancé : containeriser le script avec Docker

## Rendu

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3/
|-- config.ini          <- votre fichier de configuration
|-- README.md           <- une documentation d'installation et d'utilisation
|-- requirements.txt    <- vos dépendances tierces, s'il y en a
`-- script.py           <- votre script
```

À envoyer à l'adresse avec présentation : [assrdepotpython@outlook.fr](mailto:assrdepotpython@outlook.fr)

## Aide

La documentation officielle de Python est votre meilleure alliée :

- `urllib.request` : https://docs.python.org/3/library/urllib.request.html
- `html.parser` : https://docs.python.org/3/library/html.parser.html
- `csv` : https://docs.python.org/3/library/csv.html
- `configparser` : https://docs.python.org/3/library/configparser.html
- Documentation BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

En cas de blocage, posez vos questions dans l'espace de discussions du projet
afin que chacun puisse participer et que ça puisse profiter à tous.
