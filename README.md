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
python -m src.main --tournament payoff --seed 42
python -m src.main --match tit-for-tat all-d --rounds 200
```

Pour jouer une partie directement, les stratégies disponibles sont `all-d`,
`random`, `tit-for-tat`, `tester`, `joss`, `pavlov` et `all-c`. Le bruit d'une
partie directe est optionnel :

```bash
python -m src.main --match pavlov tit-for-tat --rounds 200 --match-noise 0.05
```


## Développement

```bash
python -m unittest discover -s tests -v
```

Le journal existe aussi en version LaTeX dans
`journal_de_bord.pdf`. 

