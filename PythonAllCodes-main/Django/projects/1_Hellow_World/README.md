# 1_Hellow_World

This is a minimal "Hello World" project for beginners. It includes two ways to run a Hello World program:

1. Console script (`hello.py`) — prints "Hello, World!" to the terminal.
2. Simple web app (`app.py`) — a tiny Flask app that serves "Hello, World!" at http://127.0.0.1:5000/.

Quick start (Windows PowerShell)

1. Open PowerShell and change directory into the project folder:

```powershell
cd .\projects\1_Hellow_World
```

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4a. Run the console script:

```powershell
python hello.py
# You should see: Hello, World!
```

4b. Run the web app (Flask):

```powershell
python app.py
# Open http://127.0.0.1:5000/ in your browser to see "Hello, World!"
```

Notes for beginners

- If `Activate.ps1` is blocked by execution policy, run PowerShell as Administrator and set

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- You do not need to run the Flask app to use the console script.
