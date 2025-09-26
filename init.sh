# Create a new virtual environment
uv venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# or on Windows PowerShell
.venv\Scripts\Activate.ps1

# Install PyMC using uv
uv pip install pymc