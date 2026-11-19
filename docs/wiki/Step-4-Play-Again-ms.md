# Langkah 4: Main lagi

[English](Step-4-Play-Again) · [Dansk](Step-4-Play-Again-da) · **Bahasa Melayu**

## Apa yang dibina langkah ini

`play_game()` membungkus permainan dalam satu gelung. Selepas keputusan, ia bertanya sama ada mahu bermain lagi; `y` atau `yes` memulakan permainan pada papan kosong dan sebarang jawapan lain menamatkan program.

## Apa yang dipaparkan program

![Tangkapan skrin output program (4)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-4-play-again.png)

Tangkapan skrin dibuat oleh `scripts/make_screenshots.py` dalam bekas Docker, daripada kod repositori ini.

## Apa yang diperoleh

- **Bungkus permainan dalam gelung.** `Board` baharu untuk setiap permainan ialah keseluruhan penetapan semula; tiada keadaan yang perlu dibersihkan.
- **Normalkan jawapan.** `.strip().lower()` menjadikan `Y`, `yes` dan ` YES ` bermaksud ya, dan setiap jawapan lain bermaksud tidak.
- **Tamat dengan baik.** Hujung input atau `Ctrl+C` menghentikan program dengan ucapan selamat tinggal yang ringkas dan kod keluar 0, bukan traceback.
- **Jadikan pakej boleh dijalankan.** `__main__.py` membolehkan `python -m tic_tac_toe` memulakan permainan, dan nama fungsi tugasan kekal tersedia daripada pakej.

## Cara ia berfungsi

```python
def run_game(view: GameView) -> None:
    while True:
        view.show_result(play_round(view))
        if not wants_another_game(view.ask_play_again()):
            return
```

## Cubalah

Main dua permainan berturut-turut, kemenangan kemudian seri:

```bash
python scripts/scripted_play.py 1 4 2 5 3 y 1 2 3 5 4 6 8 7 9 n | grep -E 'wins|draw|Play again'
```

Sebelumnya: [Langkah 3: Cari pemenang atau seri](Step-3-Find-the-Winner-ms) · Seterusnya: [Ringkasan](Summary-ms)
