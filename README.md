# Application Dash - Avocado Data

Application Dash pour visualiser les ventes d'avocats aux États-Unis.

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Lancer l'application

```bash
python app.py
```

Ouvrir le navigateur sur : http://127.0.0.1:8050

## Structure du projet

```
├── app.py              # Point d'entrée de l'application
├── pages/
│   ├── table.py        # Page 1 : layout tableau filtrable
│   ├── table_cb.py     # Page 1 : callbacks
│   ├── compare.py      # Page 2 : layout comparaison régions
│   ├── compare_cb.py   # Page 2 : callbacks
│   └── markdown.py     # Page 3 : accordion Markdown
├── assets/             # CSS et ressources statiques
├── datas/
│   └── avocado.csv     # Jeu de données
├── expli1.md
├── expli2.md
├── expli3.md
└── requirements.txt
```
