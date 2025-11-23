# Copilot Instructions for AI Coding Agents

## Project Overview
This is a Python-based sandbox project structured for experimentation and prototyping. The codebase is organized into clear directories for source code (`src/`), data (`data/`), notebooks (`notebooks/`), and tests (`tests/`).

## Architecture & Data Flow
- **Source Code**: All main logic resides in `src/`, with `main.py` as the entry point. Use `__init__.py` for package-level imports.
- **Data**: Raw and processed data are stored in `data/raw/` and `data/processed/` respectively. Scripts/notebooks should read/write data here.
- **Notebooks**: Exploratory analysis and prototyping are done in `notebooks/` (e.g., `exploration.ipynb`).
- **Tests**: All tests are in `tests/`, using standard Python test frameworks (pytest/unittest). Example: `test_main.py` for `main.py`.

## Developer Workflows
- **Run Main Script**: `python src/main.py`
- **Run Tests**: `pytest tests/` or `python -m unittest discover tests`
- **Install Dependencies**: `pip install -r requirements.txt`
- **Debugging**: Use print statements or Python debuggers (e.g., `pdb`).

## Conventions & Patterns
- Keep all new code in `src/` unless it's a notebook or test.
- Data files should be versioned in `data/` and not hardcoded in scripts.
- Tests should mirror the structure of `src/` for easy mapping.
- Use relative imports within `src/`.
- Notebooks should import from `src/` for reusable logic.

## Integration Points
- No external services are integrated by default; add API keys/configs to environment variables or config files (not hardcoded).
- All dependencies must be listed in `requirements.txt`.

## Examples
- To add a new module: create `src/new_module.py`, add tests in `tests/test_new_module.py`.
- To process data: read from `data/raw/`, write to `data/processed/`.
- To use code in a notebook: `from src.main import function_name`

## Key Files & Directories
- `src/main.py`: Main application logic
- `tests/`: All test cases
- `data/`: Data storage
- `notebooks/`: Prototyping and exploration
- `requirements.txt`: Dependency list

---
_If any conventions or workflows are unclear, please request clarification or examples from the user._
