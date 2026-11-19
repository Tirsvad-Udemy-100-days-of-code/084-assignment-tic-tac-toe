# Opsummering

[English](Summary) · **Dansk** · [Bahasa Melayu](Summary-ms)

Fire trin førte en tom fil til et testet spil. Denne side stiller dem side om side.

## Trinnene side om side

| Trin | Hvad du byggede | Funktionen | Færdigheden |
| --- | --- | --- | --- |
| [Trin 1](Step-1-Draw-the-Board-da) | Brættet og dets tegning | `print_board` | Lister, udsnit, f-strenge og konstanter |
| [Trin 2](Step-2-Take-a-Turn-da) | En tur med kontrolleret input | `play_round`, `parse_number` | Input, undtagelser og løkker |
| [Trin 3](Step-3-Find-the-Winner-da) | Vinderen og uafgjort | `check_winner`, `is_board_full` | Datadrevne regler, `any` og `all` |
| [Trin 4](Step-4-Play-Again-da) | At spille igen og en pæn afslutning | `play_game` | Løkker, afslutningskoder og pakker |

## Sådan er koden bygget op

Koden følger et lille design: **Domain** (`Board`, reglerne og konstanterne) ved intet om skærmen, **Application** (use casen og `GameView`-interfacet) kører et spil, og **Presentation** (konsolvisningen og kommandoen) taler med spillerne. Derfor kan 86 tests køre spillet uden tastatur.

## Hvor du kan gå videre

- Spil mod computeren: tilføj en funktion, der vælger et ledigt felt, og derefter en bedre, der blokerer en gevinst.
- Gør brættet større, for eksempel 4 gange 4, og ret kun `BOARD_SIZE` og `WINNING_LINES`.
- Før en stilling over flere spil.
- Tegn brættet i et vindue; der skal kun en ny visning til, fordi use casen allerede taler med et interface.
