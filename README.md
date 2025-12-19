# Number Guess Game 🎯

A fullscreen Python Tkinter Number Guessing Game with multiple difficulty levels, image-based UI, and persistent high-score storage.

## Project structure
```
Number-Guess-Game/
│
├── Guess-a -number.py         # Main entry point (rename recommended: guess_a_number.py)
├── game_logic.py              # Core game logic
├── storage.py                 # High-score storage handling
│
├── image/                     # UI images
│   ├── bg.png
│   └── icon.png
│
├── tests/                     # Test files (pytest)
│
├── highest_score.json         # Runtime high-score data (do not commit; add to .gitignore or use the template `highest_score.example.json`)
├── highest_score.txt
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files
```

## Quick start

1. Install Python 3.10 (or 3.x).
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the game:
```bash
python "Guess-a -number.py"
# Recommended: rename file to avoid spaces then:
# python guess_a_number.py
```

## Run tests & CI
- Locally: `pytest -q`
- CI: GitHub Actions workflow is included at `.github/workflows/python-app.yml` (it installs requirements and runs pytest).

## Notes & recommendations
- Use relative paths for images and avoid absolute paths in code.
- Do not commit runtime files (e.g., `highest_score.json`). Instead add them to `.gitignore` and, if useful, include a template like `highest_score.example.json`.
- Add a LICENSE and a short CONTRIBUTING guide if you plan to accept contributions.

## Dependencies
- Pillow

## Authors
group 13 — Vinay, Tushar, Vivek, Shubank, Suhas

## contacts
orlbgmvinay@gmail.com


⭐ If you like this project, give it a star on GitHub!

