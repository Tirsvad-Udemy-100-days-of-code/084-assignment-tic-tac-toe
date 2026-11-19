# Kom i gang

[English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

Du skal bruge Python 3.13 eller nyere. Spillet bruger kun standardbiblioteket, så der skal ikke hentes noget for at spille det.

## Hent koden

Klon repositoriet og åbn dets mappe:

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe.git
cd 084-assignment-tic-tac-toe
```

## Opret og brug et lokalt virtuelt miljø

Et virtuelt miljø med navnet `.venv` holder dette projekts værktøjer adskilt fra resten af din computer.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Linux og macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Udelad `[dev]`, hvis du kun vil spille. `[dev]` tilføjer `pytest`, `ruff`, `mypy` og Pillow til udvikling. `deactivate` forlader miljøet.

## Kør spillet

```bash
python -m tic_tac_toe
```

To spillere deler tastaturet. `X` begynder. Skriv nummeret på et ledigt felt, og tryk Enter. Tryk `Ctrl+C` for at stoppe.

## Kør testene

```bash
python -m pytest
```

## Byg kildekodens dokumentation

Doxygen skal kun bruges til dette trin; resultatet lægges i `docs/doxygen/`.

```bash
doxygen Doxyfile
```

Næste: [Trin 1: Tegn brættet](Step-1-Draw-the-Board-da)
