
# TP – Intégration de fonctions OpenFaaS dans une chaîne de traitement de commandes

## Objectifs pédagogiques

Ce travail pratique a pour objectif de permettre aux étudiants de :

- Concevoir et déployer plusieurs fonctions OpenFaaS utilisant différents types de déclencheurs : HTTP, planification (CRON), file de messages (NATS) et traitement de fichiers via SFTP ;
- Automatiser une chaîne de traitement métier distribuée sur Kubernetes ;
- Intégrer des événements système dans une logique applicative conforme à des standards industriels.

---

## Contexte professionnel

L'entreprise **DataRetailX** est une plateforme spécialisée dans la gestion automatisée de commandes clients pour des sites de e-commerce. Dans le cadre d'un projet de modernisation de son système d'information, l'équipe technique souhaite adopter une architecture serverless en s'appuyant sur OpenFaaS et Kubernetes.

Chaque étudiant joue le rôle d'un développeur DevOps en charge d'automatiser le traitement des fichiers de commandes d'un client spécifique, identifié par un dossier SFTP personnel (USX, où X est le numéro du participant).

## Évaluation attendue

### 1. Code source des trois fonctions (organisation claire)

**Réponse :**
```
[Prévoir ici un lien Git ou lister les répertoires de chaque fonction avec leur contenu : handler.py, YAML, etc.]
```

### 2. Démonstration fonctionnelle

**Réponse :**
J'ai programmer les cron pour trigger tout les jours a 8h, au lancement le fichier 'input.csv' doit etre netroye et enregistrer dans le dossier depot de status-checker, qui affiche tout les fichiers dans son dossier, ce qui est 1 comme ils ont tous le meme nom

### 3. Analyse des logs / sorties attendues

**Réponse :**
daily-checker -> affiche un json contenant '"order_date": "{date du jour}"'
file-transformer -> affiche 'Transformation réussie, fichier généré : /home/app/function/status-checker/depot/output.csv'
status-checker -> affiche 'Nombre de fichiers dans depot/ : {nombre de fichiers (1 dans notre cas)}'
### 4. Rapport synthétique (2 pages maximum)

**Réponse :**
j'ai fais le choix de suivre pour la plus part du projet les consignes, a l'exception des parties ou la connexion sftp etait requise.
j'ai fais tout le projet en local.
pour la manipulation du fichier csv j'ai utiliser pandas car c'est un outil extremement efficace avec python et que je le connais plutot bien.

j'ai eu un peu de mal avec les cron au depart mais j'ai finis par les faire marcher.
---

## Additionel

Voir le fichier 'images' pour des captures d'ecrans des logs et de prometheus

