# Trin 1: Tegn brættet

[English](Step-1-Draw-the-Board) · **Dansk** · [Bahasa Melayu](Step-1-Draw-the-Board-ms)

## Hvad trinnet bygger

Et bræt med ni felter og `print_board(board)`, som tegner tre rækker med tre felter og streger imellem. Et tomt felt viser sit nummer, så en spiller kan se, hvilket nummer der skal skrives.

## Hvad programmet viser

![Skærmbillede af programmets output (1)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-1-draw-the-board.png)

Skærmbilledet er lavet af `scripts/make_screenshots.py` i en Docker-container ud fra koden i dette repositorium.

## Hvad du får ud af det

- **Modellér data, og vis dem så.** Brættet er ni felter i en liste, nummereret fra 1 til 9. Hvordan det ser ud, er en separat funktion, så reglerne aldrig afhænger af tegningen.
- **Byg tekst ud fra data.** `enumerate(..., start=1)` sætter hvert felt sammen med dets nummer, et udsnit af listen deler felterne i rækker, og `join` og f-strenge sætter rækkerne sammen.
- **Giv dine tal navne.** `BOARD_SIZE` og `EMPTY_CELL` ligger i `constants.py`, så der ikke gemmer sig et magisk tal i koden.
- **Dokumentér undervejs.** Hver funktion har en kort kommentar om, hvad den gør, og Doxygen bygger dokumentationen ud fra den.

## Sådan virker det

```python
def render_board(board: Board) -> str:
    shown = [
        mark if mark != EMPTY_CELL else str(number)
        for number, mark in enumerate(board.marks(), start=1)
    ]
    rows = [
        "|".join(f" {cell} " for cell in shown[start : start + BOARD_SIZE]).rstrip()
        for start in range(0, len(shown), BOARD_SIZE)
    ]
    return _ROW_SEPARATOR.join(rows)
```

## Prøv det

Tegn et tomt bræt og et bræt med to mærker:

```bash
python -c "from tic_tac_toe import print_board
from tic_tac_toe.domain.board import Board
board = Board()
print_board(board)
board.place('X', 5)
board.place('O', 1)
print()
print_board(board)"
```

Forrige: [Kom i gang](Getting-Started-da) · Næste: [Trin 2: Tag en tur](Step-2-Take-a-Turn-da)
