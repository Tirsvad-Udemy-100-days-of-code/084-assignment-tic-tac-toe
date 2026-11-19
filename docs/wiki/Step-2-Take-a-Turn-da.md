# Trin 2: Tag en tur

[English](Step-2-Take-a-Turn) · **Dansk** · [Bahasa Melayu](Step-2-Take-a-Turn-ms)

## Hvad trinnet bygger

Spilleren, hvis tur det er, skriver nummeret på et felt. Spillet sætter mærket dér og tegner brættet igen. Et valg, der ikke er tilladt, afvises med årsagen, og samme spiller bliver spurgt igen.

## Hvad programmet viser

![Skærmbillede af programmets output (2)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-2-take-a-turn.png)

Skærmbilledet er lavet af `scripts/make_screenshots.py` i en Docker-container ud fra koden i dette repositorium.

## Hvad du får ud af det

- **Læs input, og gør det til et tal.** `input()` giver tekst; `int()` gør den til et tal og fejler med `ValueError`, når den ikke er et.
- **Kontrollér det, du fik.** Tre ting kan være galt: det er ikke et tal, det ligger uden for 1 til 9, eller feltet er optaget. Hver er sin egen årsag i én fejltype, `InvalidMoveError`.
- **Rejs din egen undtagelse.** Fejlen bevarer årsagen med `raise ... from`, og brættet ændres aldrig, når et træk afvises (beslutning ADR-0001).
- **Gentag med `while True` og `continue`.** Efter et afvist træk bliver samme spiller spurgt igen, så en tastefejl aldrig koster en tur.
- **Hold skærmen adskilt fra reglerne.** Use casen taler med et `GameView`-interface, så hele forløbet testes med en manuskriptstyret visning uden tastatur (beslutning ADR-0002).

## Sådan virker det

```python
def parse_number(choice: str) -> int:
    try:
        return int(choice.strip())
    except ValueError as err:
        raise InvalidMoveError(REASON_NOT_A_NUMBER) from err
```

```python
def place(self, mark: str, number: int) -> None:
    if not self.is_free(number):
        raise InvalidMoveError(REASON_TAKEN)
    self._cells[number - 1] = mark
```

## Prøv det

Spil et spil med en fejl af hver slags (svarene er `1`, `x`, `1` og `5`):

```bash
python scripts/scripted_play.py 1 x 1 5
```

Forrige: [Trin 1: Tegn brættet](Step-1-Draw-the-Board-da) · Næste: [Trin 3: Find vinderen eller uafgjort](Step-3-Find-the-Winner-da)
