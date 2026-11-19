# Langkah 3: Cari pemenang atau seri

[English](Step-3-Find-the-Winner) · [Dansk](Step-3-Find-the-Winner-da) · **Bahasa Melayu**

## Apa yang dibina langkah ini

Selepas setiap langkah, permainan bertanya `check_winner(board, mark)` sama ada tanda itu mempunyai satu baris, satu lajur atau satu pepenjuru. Jika tidak, `is_board_full(board)` memberitahu sama ada permainan itu seri. Jika tidak, giliran pemain lain.

## Apa yang dipaparkan program

![Tangkapan skrin output program (3)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-3-find-the-winner.png)

Tangkapan skrin dibuat oleh `scripts/make_screenshots.py` dalam bekas Docker, daripada kod repositori ini.

## Apa yang diperoleh

- **Biarkan data membawa peraturan.** Lapan barisan menang ialah tuple bagi tuple; semakannya ialah satu `any` ke atasnya dengan satu `all` di dalam, tanpa rantaian `if` yang panjang.
- **Susun semakan mengikut urutan.** Pemenang diuji sebelum papan penuh, kerana langkah terakhir boleh menang pada papan yang penuh.
- **Pulangkan nilai yang menyatakan segalanya.** `play_round` memulangkan tanda pemenang, atau `None` untuk seri, dan pemanggil memutuskan apa yang dipaparkan.
- **Uji setiap kes.** `pytest.mark.parametrize` menjalankan satu ujian untuk setiap satu daripada lapan barisan, supaya kesilapan menaip dalam jadual tidak dapat bersembunyi.

## Cara ia berfungsi

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

## Cubalah

Tamatkan satu permainan dengan kemenangan dan satu dengan seri, dan tunjukkan penghujung setiap satu:

```bash
python scripts/scripted_play.py 1 4 2 5 3 n | tail -n 8
python scripts/scripted_play.py 1 2 3 5 4 6 8 7 9 n | tail -n 9
```

Sebelumnya: [Langkah 2: Ambil giliran](Step-2-Take-a-Turn-ms) · Seterusnya: [Langkah 4: Main lagi](Step-4-Play-Again-ms)
