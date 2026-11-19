# Ringkasan

[English](Summary) · [Dansk](Summary-da) · **Bahasa Melayu**

Empat langkah membawa fail kosong menjadi permainan yang telah diuji. Halaman ini meletakkannya bersebelahan.

## Langkah-langkah bersebelahan

| Langkah | Apa yang anda bina | Fungsi | Kemahiran |
| --- | --- | --- | --- |
| [Langkah 1](Step-1-Draw-the-Board-ms) | Papan dan lukisannya | `print_board` | Senarai, hirisan, f-string dan pemalar |
| [Langkah 2](Step-2-Take-a-Turn-ms) | Satu giliran dengan input yang disemak | `play_round`, `parse_number` | Input, pengecualian dan gelung |
| [Langkah 3](Step-3-Find-the-Winner-ms) | Pemenang dan seri | `check_winner`, `is_board_full` | Peraturan berasaskan data, `any` dan `all` |
| [Langkah 4](Step-4-Play-Again-ms) | Main lagi dan penamat yang baik | `play_game` | Gelung, kod keluar dan pakej |

## Cara kod disusun

Kod mengikut reka bentuk yang kecil: **Domain** (`Board`, peraturan dan pemalar) tidak tahu apa-apa tentang skrin, **Application** (kes guna dan antara muka `GameView`) menjalankan permainan, dan **Presentation** (paparan konsol dan arahan) bercakap dengan pemain. Oleh sebab itu, 86 ujian menjalankan permainan tanpa papan kekunci.

## Ke mana selepas ini

- Main menentang komputer: tambah fungsi yang memilih petak kosong, kemudian yang lebih baik yang menyekat kemenangan.
- Besarkan papan, contohnya 4 kali 4, dan ubah `BOARD_SIZE` dan `WINNING_LINES` sahaja.
- Simpan skor untuk beberapa permainan.
- Lukis papan dalam tetingkap; hanya paparan baharu diperlukan, kerana kes guna sudah bercakap dengan antara muka.
