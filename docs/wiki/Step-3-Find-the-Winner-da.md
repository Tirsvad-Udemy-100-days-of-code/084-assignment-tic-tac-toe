# Trin 3: Find vinderen eller uafgjort

[English](Step-3-Find-the-Winner) · **Dansk** · [Bahasa Melayu](Step-3-Find-the-Winner-ms)

## Hvad trinnet bygger

Efter hvert træk spørger spillet `check_winner(board, mark)`, om mærket har en række, en søjle eller en diagonal. Hvis ikke, fortæller `is_board_full(board)`, om spillet er uafgjort. Ellers er det den anden spillers tur.

## Hvad programmet viser

![Skærmbillede af programmets output (3)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-3-find-the-winner.png)

Skærmbilledet er lavet af `scripts/make_screenshots.py` i en Docker-container ud fra koden i dette repositorium.

## Hvad du får ud af det

- **Lad data bære reglerne.** De otte vindende rækker er en tuple af tupler; kontrollen er ét `any` over dem med ét `all` indeni, uden en lang kæde af `if`.
- **Sæt kontrollerne i rækkefølge.** Vinderen testes før det fulde bræt, fordi det sidste træk kan vinde på et fyldt bræt.
- **Returnér en værdi, der siger det hele.** `play_round` returnerer vinderens mærke eller `None` ved uafgjort, og den, der kalder, bestemmer, hvad der vises.
- **Test hvert tilfælde.** `pytest.mark.parametrize` kører én test for hver af de otte rækker, så en tastefejl i tabellen ikke kan skjule sig.

## Sådan virker det

```python
WINNING_LINES = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
    (1, 5, 9), (3, 5, 7),             # diagonals
)

def check_winner(board: Board, mark: str) -> bool:
    return any(
        all(board.cell_at(number) == mark for number in line) for line in WINNING_LINES
    )

def is_board_full(board: Board) -> bool:
    return EMPTY_CELL not in board.marks()
```

## Prøv det

Afslut et spil med en sejr og et spil uafgjort, og vis enden af hvert:

```bash
python scripts/scripted_play.py 1 4 2 5 3 n | tail -n 8
python scripts/scripted_play.py 1 2 3 5 4 6 8 7 9 n | tail -n 9
```

Forrige: [Trin 2: Tag en tur](Step-2-Take-a-Turn-da) · Næste: [Trin 4: Spil igen](Step-4-Play-Again-da)
