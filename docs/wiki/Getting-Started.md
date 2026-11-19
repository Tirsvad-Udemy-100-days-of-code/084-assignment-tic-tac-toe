# Getting started

**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

You need Python 3.13 or newer. The game uses the standard library only, so nothing is downloaded to play it.

## Get the code

Clone the repository and open its folder:

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe.git
cd 084-assignment-tic-tac-toe
```

## Create and use a local virtual environment

A virtual environment named `.venv` keeps the tools of this project apart from the rest of your computer.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Linux and macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave out `[dev]` if you only want to play. `[dev]` adds `pytest`, `ruff`, `mypy` and Pillow for development. `deactivate` leaves the environment.

## Run the game

```bash
python -m tic_tac_toe
```

Two players share the keyboard. `X` starts. Type the number of a free cell and press Enter. Press `Ctrl+C` to stop.

## Run the tests

```bash
python -m pytest
```

## Build the source documentation

Doxygen is only needed for this step; the output goes to `docs/doxygen/`.

```bash
doxygen Doxyfile
```

Next: [Step 1: Draw the board](Step-1-Draw-the-Board)
