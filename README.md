# RccoWidget

RccoWidget is a small Windows desktop widget built with Python and Qt.  
It shows live crypto prices, time, quotes, and changes wallpapers automatically.

It is portable and runs in the background.

---

## Repository

https://github.com/HirunDinukshana/RccoWIdget

---

## Features

- **Live Binance Futures Price**
  - Track any trading pair (updates every 1 minute)

- **Automatic Wallpaper Cycling**
  - A `wallpapers/` folder **must exist**
  - The folder must be placed next to `main.py` or next to the built `.exe`
  - A random image is applied every time the app starts

- **Quote Updates**
  - Fetches a new quote every 10 minutes (internet required)

- **Minimal Clock**
  - Always visible and simple

- **Mouse Interactions**
  - Double-click name to edit (HTML supported)
  - Double-click price to change trading pair

- **Windows Startup**
  - The application starts automatically when Windows starts

---

## Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Build EXE

Create a standalone Windows executable using PyInstaller:

```bash
pyinstaller --noconfirm --onefile --windowed --clean \
--name "RccoWidget" \
--icon "app_icon.png" \
--add-data "utils/fonts;utils/fonts" \
main.py
```
Required Folder Structure
After building, the folder must be structured as follows:

RccoWidget\

 ├─ app_icon.png
 
 ├─ RccoWidget.exe
 
 └─ wallpapers/
 
    ├─ image1.jpg
    
    └─ image2.png
Supported image formats: .jpg, .png

License
Open source. Free to use and modify.
