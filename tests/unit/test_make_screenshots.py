"""@file test_make_screenshots.py
@brief Tests of the parts of the screenshot script that need no Docker."""

from pathlib import Path

from PIL import Image

from make_screenshots import STEPS, Step, render


def test_there_is_one_step_with_its_own_image_for_each_lecture_step() -> None:
    files = [step.file for step in STEPS]
    assert len(files) == 4
    assert len(set(files)) == 4
    assert all(file.endswith(".png") for file in files)


def test_every_step_runs_the_program_of_this_project() -> None:
    for step in STEPS:
        assert any("tic_tac_toe" in c or "scripted_play" in c for c in step.commands)


def test_render_writes_a_png_taller_for_more_lines(tmp_path: Path) -> None:
    step = Step("a.png", "Title", ("echo one",))
    render(step, ["one"], tmp_path / "short.png")
    render(step, ["one\ntwo\nthree"], tmp_path / "long.png")
    with (
        Image.open(tmp_path / "short.png") as short,
        Image.open(tmp_path / "long.png") as long,
    ):
        assert short.format == "PNG"
        assert long.height > short.height
