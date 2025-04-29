# Desktop Indicator

A small Windows 10 tray-icon utility that shows your currently active virtual desktop number. Written in Python and designed to run headlessly at login.

---

## 🚀 Features

- 🖥️ **Live desktop indicator**  
  A colored circle in the system tray that updates whenever you switch virtual desktops.  
- 🔄 **Auto-refresh**  
  Checks for desktop changes every second.  
- 🚫 **No console window**  
  Runs under `pythonw.exe` or as a `.pyw` script so no terminal ever pops up.  
- 🔧 **Easy startup integration**  
  Works via the Windows Startup folder or Task Scheduler.  

---

## 🛠️ Prerequisites

- **Operating System**: Windows 10 or later  
- **Python**: 3.7+  
- **Packages** (install with pip):  
  ```bash
  pip install pyvda pystray pillow
  ```

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/desktop-indicator.git
   cd desktop-indicator
   ```

2. **Install dependencies**  
   ```bash
   pip install --user pyvda pystray pillow
   ```

3. **Verify it runs**  
   ```bash
   python desktop_indicator.py
   ```
   You should see a new tray icon with your current desktop number.

---

## ▶️ Usage

### Manual launch

```bash
pythonw desktop_indicator.py
```

or, if you prefer the console version:

```bash
python desktop_indicator.py
```

### Background launch via Startup folder

1. Create a batch wrapper (e.g. `run_desktop_indicator.bat`):

   ```bat
   @echo off
   set "PYTHON=C:\Path\To\pythonw.exe"
   set "SCRIPT=C:\Path\To\desktop_indicator.py"
   "%PYTHON%" "%SCRIPT%"
   ```

2. Create a shortcut to `run_desktop_indicator.bat` and place it in your Startup folder:

   ```
   %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
   ```

### Using Task Scheduler

```powershell
schtasks /create /tn "Desktop Indicator" `
    /tr "\"C:\Path\To\pythonw.exe\" \"C:\Path\To\desktop_indicator.py\"" `
    /sc onlogon /rl lowest /f
```

---

## 🧰 Packaging into a standalone EXE

You can bundle the script with PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --clean desktop_indicator.py
```

The resulting `dist/desktop_indicator.exe` can be run directly or scheduled at login.

---

## 🐛 Troubleshooting

- **ModuleNotFoundError: No module named 'pyvda'**  
  Make sure you install into the same Python interpreter you’re invoking:
  ```bash
  <full-path-to-python> -m pip install --user pyvda pystray pillow
  ```
- **“The system cannot find the path specified.”**  
  Double-check your `PYTHON` and `SCRIPT` paths in the batch file.
- **Tray icon doesn’t appear at login**  
  • Confirm your `.bat` shortcut is in the correct Startup folder.  
  • Try running the batch manually and inspect `%TEMP%\desktop_indicator.log`.

---

## 🤝 Contributing

1. Fork this repository  
2. Create a feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am 'Add foo'`)  
4. Push to your branch (`git push origin feature/foo`)  
5. Open a Pull Request

Please keep commits focused and include descriptive commit messages.

---
