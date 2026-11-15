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

ALL-D joue toujours `D`. Cette stratégie correspond à la défection
systématique, considérée comme la décision rationnelle dans le raisonnement
par récurrence à rebours. Elle obtient de bons scores contre les stratégies
qui coopèrent, mais seulement `P` contre une autre stratégie qui joue `D`.

### RANDOM

RANDOM joue `C` ou `D` au hasard, avec une probabilité d'une chance sur deux
pour chaque coup. Elle sert de stratégie témoin et ne cherche pas à exploiter
les coups précédents de l'adversaire.

### TIT-FOR-TAT

TIT-FOR-TAT joue `C` au premier tour, puis rejoue le coup de l'adversaire au
tour précédent. Elle devrait bien jouer contre les stratégies coopératives,
mais réagir immédiatement à une défection.

### TESTER

TESTER joue `D` au premier tour. Si l'adversaire riposte en jouant `D`, elle
adopte ensuite la règle de TIT-FOR-TAT. Sinon, elle répète la séquence
`C, C, D`. Cette stratégie commence donc par tester la réaction de
l'adversaire.

### JOSS

JOSS suit la règle de TIT-FOR-TAT, mais remplace un coup `C` par `D` une fois
sur dix en moyenne. Elle cherche ainsi à exploiter occasionnellement une
coopération tout en restant généralement réactive.

### Nouvelles stratégies

#### PAVLOV

PAVLOV coopère au premier tour, puis conserve son dernier coup lorsque les
deux coups précédents sont identiques et change de coup lorsqu'ils sont
différents. Nous l'avons ajoutée pour comparer une stratégie adaptative qui
ne copie pas directement l'adversaire à TIT-FOR-TAT.

#### ALL-C

ALL-C coopère à chaque tour, quelles que soient les actions de l'adversaire.
Elle sert de référence pour mesurer l'exploitation des stratégies
coopératives par ALL-D et par les autres stratégies.

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
Enfin, le résultat dépend  de la graine aléatoire fixée à 42 et de notre protocole de classement. Le tournoi d'Axelrod utilisait une population plus large et un protocole différent.

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

### Modification A : bruit

Nous avons choisi de modifier le tournoi avec du bruit car les coups ne sont
pas toujours exécutés parfaitement dans une situation réelle. Un joueur peut
vouloir coopérer mais jouer accidentellement `D`, ou vouloir trahir mais jouer
`C`. Cette modification permet donc de tester la robustesse des stratégies,
notamment la capacité de TIT-FOR-TAT et de PAVLOV à réagir aux erreurs, tout
en restant proche du dilemme du prisonnier itéré.

- Paramètres : population étendue, 200 tours par partie, 5 parties par paire,
  bruit de `5 %`, graine `42`.
- Prédiction avant exécution : le bruit devrait réduire les scores des
  stratégies coopératives, car une défection accidentelle peut provoquer une
  riposte de TIT-FOR-TAT ou de JOSS. PAVLOV pourrait être plus robuste, car
  elle peut rétablir la coopération après une erreur. ALL-D devrait être moins
  affectée par le bruit puisqu'elle joue déjà toujours D.
- Résultats :

  Commande exécutée :

  ```powershell
  py -m src.main --tournament noise --seed 42 --noise 0.05
  ```

  | Rang | Stratégie | Score total |
  |---:|---|---:|
  | 1 | ALL-D | 17191 |
  | 2 | JOSS | 15310 |
  | 3 | TESTER | 15231 |
  | 4 | PAVLOV | 15144 |
  | 5 | RANDOM | 15120 |
  | 6 | TIT-FOR-TAT | 14994 |
  | 7 | ALL-C | 12121 |

  La commande donne le même classement lorsqu'elle est relancée avec la même
  graine.

- Analyse : le bruit modifie fortement le classement des stratégies
  réactives. TIT-FOR-TAT passe de la troisième à la sixième place, car une
  défection accidentelle peut déclencher une riposte puis une alternance de
  représailles. JOSS devient deuxième, ce qui montre que sa défection
  aléatoire peut parfois limiter cet effet. PAVLOV reste quatrième et semble
  plus stable que TIT-FOR-TAT. ALL-C reste dernière, car elle continue de
  coopérer face aux défections. 

### Modification B : autres gains

Nous avons choisi de modifier la matrice des gains plutôt que l'horizon,
car cette modification change directement la valeur de chaque résultat
(`C/C`, `D/C` et `D/D`) tout en conservant la même structure du dilemme.
Cela permet d'étudier si le classement dépend seulement des comportements
des stratégies ou aussi de l'importance relative de la récompense et de la
tentation de trahir.

- Paramètres : population étendue, 200 tours par partie, 5 parties par paire,
  graine `42`, sans bruit. Nouvelle matrice :
  `R=4`, `S=0`, `T=6`, `P=1`.
- Justification : cette matrice vérifie toujours `T > R > P > S`
  (`6 > 4 > 1 > 0`) et reste donc un dilemme du prisonnier. La coopération
  mutuelle vaut davantage qu'avant, mais la tentation de trahir est également
  plus forte et la défection mutuelle est moins rémunérée.
- Prédiction avant exécution : les stratégies qui coopèrent ensemble, comme
  TIT-FOR-TAT et PAVLOV, devraient bénéficier de la hausse de `R`. ALL-D
  devrait rester forte contre les stratégies coopératives grâce à `T=6`,
  mais perdre davantage lors des confrontations entre déserteurs avec `P=1`.
- Résultats :

  Commande exécutée :

  ```powershell
  py -m src.main --tournament payoff --seed 42
  ```

  Classement obtenu :

  | Rang | Stratégie | Score total |
  |---:|---|---:|
  | 1 | TESTER | 17971 |
  | 2 | RANDOM | 16683 |
  | 3 | TIT-FOR-TAT | 16386 |
  | 4 | ALL-C | 16300 |
  | 5 | PAVLOV | 16214 |
  | 6 | JOSS | 13996 |
  | 7 | ALL-D | 13470 |

- Analyse :
  Par rapport au tournoi `extended`, qui utilise les mêmes sept stratégies
  avec les gains `R=3, S=0, T=5, P=2`, le classement change fortement.
  ALL-D passe de la première à la dernière place, car les confrontations
  entre déserteurs ne valent plus que 1 point par tour. TESTER passe de la
  deuxième à la première place et RANDOM de la cinquième à la deuxième.
  TIT-FOR-TAT reste troisième, tandis que PAVLOV recule de la quatrième à la
  cinquième place. ALL-C remonte de la septième à la quatrième, car les
  séquences de coopération mutuelle valent maintenant 4 points par tour.
  Comme la population, le nombre de tours et le nombre de parties sont
  identiques, cette comparaison isole mieux l'effet de la matrice des gains.
  Elle montre que le classement dépend aussi de l'importance relative de la
  coopération, de la tentation de trahir et de la défection mutuelle.

## 6. Impasses et changements

### Difficultés rencontrées

- Les résultats aléatoires peuvent changer d'une exécution à l'autre. Une
  graine fixe (`42`) est donc utilisée pour rendre les expériences
  reproductibles.
- Les scores de l'horizon inconnu auraient été difficiles à comparer car les
  parties n'auraient pas toutes eu la même durée. Nous avons finalement
  retenu les autres gains comme deuxième modification.

### Changements apportés
- Ajout de deux stratégies absentes du cours : PAVLOV et ALL-C.
- Ajout du bruit de 5 % et d'une matrice alternative
  `R=4, S=0, T=6, P=1`.
- Ajout de tests sur le moteur, TIT-FOR-TAT, TESTER et JOSS.


