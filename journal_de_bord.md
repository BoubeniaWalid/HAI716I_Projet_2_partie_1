# Journal de bord

## 1. Protocole

- Date : 13 novembre 2026
- Graine aléatoire : `42`
- Nombre de tours par partie : 200
- Nombre de parties par confrontation : 5
- Matrice des gains : `R=3`, `S=0`, `T=5`, `P=2`
- Stratégies de départ : ALL-D, RANDOM, TIT-FOR-TAT, TESTER, JOSS


## 2. Stratégies


### ALL-D

À compléter.

### RANDOM

À compléter

### TIT-FOR-TAT

À compléter.

### TESTER

À compléter .

### JOSS

À compléter .

### Nouvelles stratégies

#### Nouvelle stratégie 1

À compléter.

#### Nouvelle stratégie 2

À compléter.

## 3. Étape 1 : tournoi de base

### Prédiction

Je prévois que TIT-FOR-TAT sera bien classée grâce à sa coopération avec
elle-même et avec les stratégies coopératives. ALL-D devrait obtenir de bons
scores contre les stratégies coopératives, mais perdre des points contre les
stratégies qui répondent par D.

### Résultats

Commande exécutée :

```powershell
py -m src.main --tournament baseline --seed 42
```

Classement obtenu :

| Rang | Stratégie | Score total |
|---:|---|---:|
| 1 | ALL-D | 9467 |
| 2 | TESTER | 9275 |
| 3 | TIT-FOR-TAT | 9221 |
| 4 | JOSS | 9166 |
| 5 | RANDOM | 8663 |

Le résultat est reproductible avec la même commande et la même graine.

### Analyse

TIT-FOR-TAT ne gagne pas dans notre tournoi : elle arrive troisième avec
9221 points. ALL-D arrive première avec 9467 points.

Ce résultat diffère de celui d'Axelrod (1980) pour plusieurs raisons. Notre
population est beaucoup plus petite : elle contient seulement cinq stratégies.
De plus, notre moteur ne réalise pas d'auto-confrontations : chaque paire de
stratégies ne joue qu'une seule série de cinq parties. Cela retire notamment à
TIT-FOR-TAT ses parties très favorables contre elle-même.
Enfin, le résultat dépend des définitions précises de TESTER et JOSS, de la
graine aléatoire fixée à 42 et de notre protocole de classement. Le tournoi
d'Axelrod utilisait une population plus large et un protocole différent.

## 4. Étape 2 : stratégies supplémentaires

### Prédiction

L'ajout de PAVLOV devrait lui permettre d'obtenir de bons résultats contre
les stratégies coopératives et réactives. ALL-C devrait bien réussir contre
les stratégies coopératives, mais perdre beaucoup de points contre ALL-D.
L'ajout de ces deux stratégies devrait modifier les scores totaux et
peut-être le classement.

### Résultats et comparaison

Les deux stratégies absentes du cours ajoutées sont :

- **PAVLOV** : coopère au premier tour, puis conserve son dernier coup si le
  résultat précédent était favorable (`C/C` ou `D/D`), sinon change de coup ;
- **ALL-C** : coopère toujours.

Commande exécutée :

```powershell
py -m src.main --tournament extended --seed 42
```

Classement avec la population élargie :

| Rang | Stratégie | Score total |
|---:|---|---:|
| 1 | ALL-D | 16482 |
| 2 | TESTER | 15789 |
| 3 | TIT-FOR-TAT | 15228 |
| 4 | PAVLOV | 15176 |
| 5 | RANDOM | 15152 |
| 6 | JOSS | 14749 |
| 7 | ALL-C | 12225 |

ALL-D, TESTER et TIT-FOR-TAT conservent leurs positions respectives. PAVLOV
arrive directement derrière TIT-FOR-TAT, tandis que ALL-C termine dernière.
ALL-C perd notamment beaucoup de points contre ALL-D, qui obtient 5 points
par tour lorsqu'elle coopère face à lui.

Les scores totaux ne sont pas directement comparables entre les deux étapes :
la population élargie contient davantage de paires et donc davantage de
parties. La comparaison pertinente porte principalement sur les positions et
sur les écarts entre stratégies.

## 5. Étape 3 : modifications

Pour chaque modification, respecter l'ordre : prédiction, exécution, comparaison.

### Modification A : bruit

- Paramètres :
- Prédiction avant exécution :
- Résultats :
- Analyse :

### Modification B : horizon inconnu

- Paramètres :
- Prédiction avant exécution :
- Résultats :
- Analyse :

## 6. Impasses et changements

 les erreurs rencontrées, les hypothèses abandonnées et les corrections.

## 7. Captures d'écran

les captures des classements, sorties de programme et graphiques.

