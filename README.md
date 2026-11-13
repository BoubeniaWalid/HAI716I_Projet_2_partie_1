# Tournoi du dilemme du prisonnier itéré

Projet HAI716I - Projet 2, partie 1.

## Structure

```text
.
├── journal_de_bord.md
├── src/
│   ├── engine.py       # Une partie entre deux stratégies
│   ├── models.py       # Types et matrice des gains
│   ├── strategies.py   # Stratégies du cours et nouvelles stratégies
│   ├── tournaments.py  # Tournois tous contre tous et classements
│   ├── experiments.py  # Bruit, horizon inconnu, sélection, etc.
│   └── main.py         # Point d'entrée
└── tests/
    └── test_engine.py
```

## Lancer

Depuis la racine du dépôt :

```bash
python -m src.main --tournament baseline --seed 42
python -m src.main --tournament extended --seed 42
python -m src.main --tournament noise --seed 42 --noise 0.05
```


## Développement

```bash
python -m unittest discover -s tests -v
```


