# App Music Launcher

## Overview
Python script that monitors running processes and triggers music playback (via ```pygame```) when predefined applications (e.g., Firefox, VS Code) are launched. Stops playback when all target apps are closed.

## Features
- Real-time process monitoring using psutil.
- Customizable app list: Edit APPS_MONITOREADAS to add/remove apps.
- Background logging: All events are saved to monitor_ventanas.log.
- Graceful shutdown: Handles KeyboardInterrupt (Ctrl+C) and errors.

## Installation 
#### Requirements: 

```bash
pip install pygame psutil
```
## Music file:
Place *eye_of_the_tiger.mp3* in the same directory as the script (or update the path in code).


## Usage
```
python script-code.py
```


## Expected Output:

```plaintext
Iniciando monitor 24/7 para: firefox.exe, Code.exe
APP ABIERTA: Code.exe
▶️ Reproduciendo música por primera vez
```
