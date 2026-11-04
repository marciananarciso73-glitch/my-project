# my-project

A clean, modern Python project template featuring a **FastAPI** REST API, an interactive **CLI**, and a **pytest** test suite.

---

## Features

- **FastAPI REST API**: High-performance asynchronous API with automatic interactive OpenAPI/Swagger docs at `/docs`.
- **Command-Line Interface (CLI)**: Built with `click` to run server commands and manage resources from the terminal.
- **Data Validation**: Request and response validation powered by `pydantic`.
- **Comprehensive Test Suite**: Automated unit and endpoint testing with `pytest` and `httpx`.
- **Standard Packaging**: Configured with modern `pyproject.toml` standards.

---

## Project Structure

```text
my-project/
├── .gitignore
├── pyproject.toml            # Project configuration and dependency definitions
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development & testing dependencies
├── README.md
├── src/
│   └── my_project/
│       ├── __init__.py       # Package metadata and version
│       ├── __main__.py       # Module entry point (python -m my_project)
│       ├── cli.py            # CLI commands (Click)
│       ├── main.py           # FastAPI application & endpoints
│       ├── models.py         # Pydantic schemas
│       └── service.py        # Business logic & repository
└── tests/
    ├── __init__.py
    ├── test_api.py           # API endpoint integration tests
    └── test_cli.py           # CLI command unit tests
```

---

## Quickstart

### 1. Environment Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

Or install via requirements files:

```bash
pip install -r requirements-dev.txt
```

---

## Usage

### Running the API Server

Start the API server via the CLI:

```bash
my-project serve --reload
```

Or run directly with `uvicorn`:

```bash
uvicorn my_project.main:app --reload --port 8000
```

Once running, access:
- **API Root**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Using the Command-Line Interface (CLI)

```bash
# Check version
my-project version

# View available commands
my-project --help

# List items
my-project items list

# Add a new item
my-project items add "Complete documentation" --description "Add usage details to README" --completed
```

You can also run the CLI via Python module syntax:

```bash
python -m my_project items list
```

---

## Running Tests

Execute the test suite using `pytest`:

```bash
pytest
```
