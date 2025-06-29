## Fonctionnalités

- Génération de plusieurs types de motifs géométriques :
  - Polygones répétés
  - Spirales progressives
  - Fractales simples (étoile récursive)
  
- Interface web accessible et intuitive permettant à l'utilisateur de configurer les paramètres suivants :
  - Nombre de côtés du motif
  - Profondeur ou nombre de répétitions
  - Taille initiale du motif
  - Angle de rotation entre chaque répétition
  - Couleur
  - Type de motif

- Aperçu immédiat du motif généré sous forme d'image
- Interface responsive compatible avec différents types d'écrans (ordinateurs, tablettes, smartphones)
- Séparation claire entre les fichiers Python (logique et génération graphique) et les fichiers web (HTML/CSS)
- Nettoyage automatique des anciennes images générées
- Utilisation de processus indépendants pour éviter les erreurs liées à la bibliothèque Turtle

## Structure du projet

```
geometric_generator/
├── app.py                  # Serveur Flask
├── generator.py            # Génération graphique avec Turtle
├── requirements.txt        # Dépendances Python
├── static/
│   ├── css/
│   │   └── style.css       # Fichier de style CSS
│   └── images/             # Images générées par l'application
├── templates/
│   └── index.html          # Page web principale
└── README.md               # Documentation du projet
```

## Installation

### Prérequis

- Python 3.8 ou version ultérieure
- Pip (gestionnaire de paquets Python)

## Utilisation

Lancement de l'application :

```bash
python3 app.py
```

L'interface est accessible depuis un navigateur web à l'adresse suivante :

```
http://127.0.0.1:5000
```

L'utilisateur peut alors configurer les paramètres du motif et générer une image qui s'affichera automatiquement.

## Exemples d'utilisation

| Paramètre         | Exemple              |
|-------------------|---------------------|
| Nombre de côtés   | 6 (hexagone)        |
| Profondeur        | 20                  |
| Taille initiale   | 150                 |
| Angle de rotation | 20 degrés           |
| Couleur           | red, blue, green    |
| Type de motif     | polygon, spiral, fractal |
