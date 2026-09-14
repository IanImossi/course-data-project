# course-data-project

A local Python environment for exploring and analyzing course data.

## Setup

This project uses a standard library virtual environment (`venv`) plus `pip`.

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```
2. Activate it:
   - PowerShell: `.venv\Scripts\Activate.ps1`
   - Command Prompt: `.venv\Scripts\activate.bat`
3. Install the project's dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Launch Jupyter to start exploring:
   ```
   jupyter notebook
   ```

See `requirements.txt` for the exact package list (pandas, numpy, matplotlib, jupyter).

## Project layout

- `requirements.txt` — Python dependencies
- `data/` — place course data files here (ignored by git; see `.gitignore`)
- `.venv/` — local virtual environment (ignored by git, created by you, not committed)
