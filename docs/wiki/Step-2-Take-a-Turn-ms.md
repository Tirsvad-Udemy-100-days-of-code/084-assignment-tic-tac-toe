# Langkah 2: Ambil giliran

[English](Step-2-Take-a-Turn) · [Dansk](Step-2-Take-a-Turn-da) · **Bahasa Melayu**

## Apa yang dibina langkah ini

Pemain yang mendapat giliran menaip nombor sebuah petak. Permainan meletakkan tanda di situ dan melukis papan semula. Pilihan yang tidak dibenarkan ditolak dengan sebabnya, dan pemain yang sama ditanya semula.

## Apa yang dipaparkan program

![Tangkapan skrin output program (2)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-2-take-a-turn.png)

Tangkapan skrin dibuat oleh `scripts/make_screenshots.py` dalam bekas Docker, daripada kod repositori ini.

## Apa yang diperoleh

- **Baca input dan tukarkannya kepada nombor.** `input()` memberi teks; `int()` menukarnya kepada nombor dan gagal dengan `ValueError` apabila ia bukan nombor.
- **Semak apa yang diberi.** Tiga perkara boleh salah: bukan nombor, di luar 1 hingga 9, atau petak sudah diambil. Setiap satu ialah sebab tersendiri dalam satu jenis ralat, `InvalidMoveError`.
- **Bangkitkan pengecualian anda sendiri.** Ralat itu mengekalkan puncanya dengan `raise ... from`, dan papan tidak pernah berubah apabila langkah ditolak (keputusan ADR-0001).
- **Ulang dengan `while True` dan `continue`.** Selepas langkah ditolak, pemain yang sama ditanya semula, jadi kesilapan menaip tidak pernah menghilangkan giliran.
- **Asingkan skrin daripada peraturan.** Kes guna bercakap dengan antara muka `GameView`, jadi keseluruhan aliran diuji dengan paparan berskrip tanpa papan kekunci (keputusan ADR-0002).

## Cara ia berfungsi

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

## Cubalah

Main satu permainan dengan satu kesilapan setiap jenis (jawapannya ialah `1`, `x`, `1` dan `5`):

```bash
python scripts/scripted_play.py 1 x 1 5
```

Sebelumnya: [Langkah 1: Lukis papan](Step-1-Draw-the-Board-ms) · Seterusnya: [Langkah 3: Cari pemenang atau seri](Step-3-Find-the-Winner-ms)
