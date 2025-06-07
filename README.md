### README.md

# Black-Box MVP

Black-Box est un moteur d'inférence minimaliste conçu pour retrouver automatiquement une fonction mathématique cachée (black-box) à partir d'un ensemble de données d'entrée/sortie (appelé ici K).

## Objectif

À partir d'une série de couples K = [{inputs: [...], output: ...}], le système tente d'identifier la ou les fonctions candidates qui peuvent reproduire au mieux le comportement observé.

## Composants principaux

- `core/functions/` : contient les fonctions mathématiques candidates
- `core/evaluator.py` : système d'évaluation des fonctions sur les données K
- `core/engine.py` : moteur de résolution
- `core/merger.py` : fusion d'hypothèses partiellement valides
- `core/models/` : définitions des structures de base : K, Hypothèse, Score

## Lancement

```bash
python main.py
```

## TODO v1

- [x] Chargement de K
- [x] Définition de fonctions candidates
- [ ] Évaluation de la précision des fonctions
- [ ] Itération sur des paires de K pour extraire des patterns
- [ ] Fusion et sélection des meilleures hypothèses