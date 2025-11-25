# MasterPythonRepo – Django (workspace level)

This repository folder is prepared to contain multiple projects. I reorganised documentation into `docs/` so the root is ready for more projects.

Recommended layout:

- `projects/` — keep separate projects here (create `projects/<project-name>/`)
- `docs/` — shared documentation and course material
- `tools/` — optional helper scripts or utilities

How to add a new project:

1. Create a new folder at the repository root, for example `projects/my_new_project/`.
2. Add a virtual environment or use an environment manager and add a `requirements.txt` or `pyproject.toml`.
3. Keep project-specific README and docs inside the project folder.

To view docs in PowerShell:

```powershell
Get-ChildItem -Recurse .\docs
```

Create a new project using the provided PowerShell helper script:

```powershell
# from the `Django` folder
.\scripts\create_project.ps1 -Name MyProject
# add -WithVenv if you want the helper to print venv creation instructions
.\scripts\create_project.ps1 -Name MyProject -WithVenv
```

The script will create `projects/MyProject/` with `README.md`, `requirements.txt` and a `.gitkeep` file.
