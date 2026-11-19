"""@file make_screenshots.py
@brief Make one screenshot per step of the program's own output.

Each step runs its commands in a Docker container (Linux, Python 3.13, no desktop;
see framework/process/gui-testing.md), saves the text they print under results/
and draws it as a terminal-like PNG in docs/images/. Nothing starts on the
desktop of the host, and no screenshot of the lecture is used.

Usage:
    python scripts/make_screenshots.py [output_dir]
"""

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "images"
RESULTS = ROOT / "results"
IMAGE = "python:3.13-slim"
WIDTH = 1000
MARGIN = 24
FONT_SIZE = 20
LINE_HEIGHT = 28
TITLE_HEIGHT = 56
BACKGROUND = "#1e1e2e"
TITLE_BAR = "#313244"
TITLE_COLOR = "#cdd6f4"
COMMAND_COLOR = "#a6e3a1"
OUTPUT_COLOR = "#f5f5f5"
FONT_FILES = (
    "consola.ttf",
    "DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "Menlo.ttc",
)
WIN = "1 4 2 5 3"
DRAW = "1 2 3 5 4 6 8 7 9"


@dataclass(frozen=True)
class Step:
    """@brief One lecture step: its image file, its title and its commands."""

    file: str
    title: str
    commands: tuple[str, ...]


STEPS = (
    Step(
        "step-1-draw-the-board.png",
        "Step 1: Draw the board",
        (
            'python -c "'
            "from tic_tac_toe import print_board\n"
            "from tic_tac_toe.domain.board import Board\n"
            "board = Board()\n"
            "print_board(board)\n"
            "board.place('X', 5)\n"
            "board.place('O', 1)\n"
            "print()\n"
            "print_board(board)\n"
            '"',
        ),
    ),
    Step(
        "step-2-take-a-turn.png",
        "Step 2: Take a turn",
        ("python scripts/scripted_play.py 1 x 1 5",),
    ),
    Step(
        "step-3-find-the-winner.png",
        "Step 3: Find the winner or a draw",
        (
            f"python scripts/scripted_play.py {WIN} n | tail -n 8",
            f"python scripts/scripted_play.py {DRAW} n | tail -n 9",
        ),
    ),
    Step(
        "step-4-play-again.png",
        "Step 4: Play again",
        (
            f"python scripts/scripted_play.py {WIN} y {DRAW} n"
            " | grep -E 'wins|draw|Play again'",
        ),
    ),
)


def run_in_container(command: str) -> str:
    """@brief Run a shell command in a throw-away container.

    @param command The shell command.
    @return What the command printed, without the last line break.
    """
    docker = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{ROOT}:/work:ro",
        "-w",
        "/work",
        "-e",
        "PYTHONPATH=src",
        "-e",
        "PYTHONDONTWRITEBYTECODE=1",
        IMAGE,
        "sh",
        "-c",
        f"({command}) 2>&1",
    ]
    # The commands are the constants of STEPS in this file; no outside input reaches
    # the call, so the audit rule for a non-static string does not apply.
    done = subprocess.run(  # nosemgrep
        docker, capture_output=True, text=True, check=False
    )
    return done.stdout.replace("\r\n", "\n").rstrip("\n")


def load_font() -> ImageFont.FreeTypeFont:
    """@brief Find a monospaced font.

    @return The first font of `FONT_FILES` that this machine has.
    @throws SystemExit No such font is installed.
    """
    for name in FONT_FILES:
        try:
            return ImageFont.truetype(name, FONT_SIZE)
        except OSError:
            continue
    raise SystemExit("No monospaced font found; install DejaVu Sans Mono.")


def render(step: Step, outputs: list[str], target: Path) -> None:
    """@brief Draw the title bar, then each command with a prompt and its output.

    @param step The step that was run.
    @param outputs What each command of the step printed, in order.
    @param target The PNG file to write.
    """
    lines: list[tuple[str, str]] = []
    for command, output in zip(step.commands, outputs, strict=True):
        for index, line in enumerate(command.splitlines()):
            lines.append((("$ " if index == 0 else "  ") + line, COMMAND_COLOR))
        lines.extend((line, OUTPUT_COLOR) for line in output.splitlines())
    height = TITLE_HEIGHT + MARGIN * 2 + len(lines) * LINE_HEIGHT
    image = Image.new("RGB", (WIDTH, height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    font = load_font()
    draw.rectangle((0, 0, WIDTH, TITLE_HEIGHT), fill=TITLE_BAR)
    draw.text((MARGIN, 14), step.title, fill=TITLE_COLOR, font=font)
    y = TITLE_HEIGHT + MARGIN
    for text, color in lines:
        draw.text((MARGIN, y), text, fill=color, font=font)
        y += LINE_HEIGHT
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)


def main(out_dir: Path) -> None:
    """@brief Run every step in the container, save its text and write its image.

    @param out_dir The folder for the PNG files.
    """
    RESULTS.mkdir(exist_ok=True)
    for step in STEPS:
        outputs = [run_in_container(command) for command in step.commands]
        (RESULTS / f"{Path(step.file).stem}.txt").write_text(
            "\n".join(outputs) + "\n", encoding="utf-8", newline="\n"
        )
        render(step, outputs, out_dir / step.file)
        print(f"wrote {out_dir / step.file}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
