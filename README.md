# Team Uwu Final




## Local Setup

We are using [uv](https://github.com/astral-sh/uv) to manage our dependencies and virtual environment

**1. Sync the environment:**
This command will automatically read the `uv.lock` file, create a `.venv` folder, and install all of our required packages in seconds.
```bash
uv sync
```

**2. Activate the virtual environment:**
You must activate the environment before running the python scripts or opening the Jupyter Notebooks.

```bash
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```