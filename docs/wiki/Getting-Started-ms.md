# Mula di sini

[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

Anda memerlukan Python 3.13 atau lebih baharu. Permainan ini hanya menggunakan pustaka standard, jadi tiada apa-apa dimuat turun untuk memainkannya.

## Dapatkan kod

Klon repositori dan buka foldernya:

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe.git
cd 084-assignment-tic-tac-toe
```

## Cipta dan gunakan persekitaran maya tempatan

Persekitaran maya bernama `.venv` mengasingkan alat projek ini daripada seluruh komputer anda.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Linux dan macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Tinggalkan `[dev]` jika anda hanya mahu bermain. `[dev]` menambah `pytest`, `ruff`, `mypy` dan Pillow untuk pembangunan. `deactivate` keluar daripada persekitaran.

## Jalankan permainan

```bash
python -m tic_tac_toe
```

Dua pemain berkongsi papan kekunci. `X` bermula. Taip nombor petak yang kosong dan tekan Enter. Tekan `Ctrl+C` untuk berhenti.

## Jalankan ujian

```bash
python -m pytest
```

## Bina dokumentasi kod sumber

Doxygen hanya diperlukan untuk langkah ini; hasilnya disimpan dalam `docs/doxygen/`.

```bash
doxygen Doxyfile
```

Seterusnya: [Langkah 1: Lukis papan](Step-1-Draw-the-Board-ms)
