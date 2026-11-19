# Langkah 1: Lukis papan

[English](Step-1-Draw-the-Board) · [Dansk](Step-1-Draw-the-Board-da) · **Bahasa Melayu**

## Apa yang dibina langkah ini

Sebuah papan dengan sembilan petak, dan `print_board(board)`, yang melukis tiga baris dengan tiga petak dan garisan di antaranya. Petak kosong menunjukkan nombornya, supaya pemain dapat melihat nombor yang perlu ditaip.

## Apa yang dipaparkan program

![Tangkapan skrin output program (1)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-1-draw-the-board.png)

Tangkapan skrin dibuat oleh `scripts/make_screenshots.py` dalam bekas Docker, daripada kod repositori ini.

## Apa yang diperoleh

- **Modelkan data, kemudian paparkannya.** Papan ialah sembilan petak dalam senarai, dinomborkan 1 hingga 9. Rupanya ialah fungsi yang berasingan, supaya peraturan tidak pernah bergantung pada lukisan.
- **Bina teks daripada data.** `enumerate(..., start=1)` memadankan setiap petak dengan nombornya, hirisan senarai memotong petak menjadi baris, dan `join` serta f-string menyatukan baris.
- **Namakan nombor anda.** `BOARD_SIZE` dan `EMPTY_CELL` berada dalam `constants.py`, jadi tiada nombor ajaib tersembunyi dalam kod.
- **Dokumenkan semasa menulis.** Setiap fungsi mempunyai komen ringkas tentang apa yang dilakukannya, dan Doxygen membina dokumentasi daripadanya.

## Cara ia berfungsi

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

## Cubalah

Lukis papan kosong dan papan dengan dua tanda:

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

Sebelumnya: [Mula di sini](Getting-Started-ms) · Seterusnya: [Langkah 2: Ambil giliran](Step-2-Take-a-Turn-ms)
