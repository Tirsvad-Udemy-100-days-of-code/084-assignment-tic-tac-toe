# Trin 4: Spil igen

[English](Step-4-Play-Again) · **Dansk** · [Bahasa Melayu](Step-4-Play-Again-ms)

## Hvad trinnet bygger

`play_game()` pakker spillet ind i en løkke. Efter resultatet spørger den, om der skal spilles igen; `y` eller `yes` starter et spil på et tomt bræt, og ethvert andet svar afslutter programmet.

## Hvad programmet viser

![Skærmbillede af programmets output (4)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-4-play-again.png)

Skærmbilledet er lavet af `scripts/make_screenshots.py` i en Docker-container ud fra koden i dette repositorium.

## Hvad du får ud af det

- **Pak et spil ind i en løkke.** Et nyt `Board` til hvert spil er hele nulstillingen; der er ingen tilstand, der skal ryddes op.
- **Normalisér svaret.** `.strip().lower()` får `Y`, `yes` og ` YES ` til at betyde ja, og alle andre svar betyder nej.
- **Slut pænt.** Slutningen af inputtet eller `Ctrl+C` stopper programmet med et kort farvel og afslutningskode 0 i stedet for en traceback.
- **Gør en pakke kørbar.** `__main__.py` lader `python -m tic_tac_toe` starte spillet, og opgavens funktionsnavne er stadig tilgængelige fra pakken.

## Sådan virker det

```python
def run_game(view: GameView) -> None:
    while True:
        view.show_result(play_round(view))
        if not wants_another_game(view.ask_play_again()):
            return
```

## Prøv det

Spil to spil i træk, en sejr og så uafgjort:

```bash
python scripts/scripted_play.py 1 4 2 5 3 y 1 2 3 5 4 6 8 7 9 n | grep -E 'wins|draw|Play again'
```

Forrige: [Trin 3: Find vinderen eller uafgjort](Step-3-Find-the-Winner-da) · Næste: [Opsummering](Summary-da)
