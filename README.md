# Project S.A.N.D.

Project S.A.N.D. (Spreading Awareness of Natural Disasters) is a Python project that provides both a command-line interface and a Flask web UI to explore FEMA's National Risk Index (NRI) data at the U.S. county level. The codebase includes tools to query hazard ratings for specific disaster types, return the top-5 hazards for a county, and render interactive pages that display county-level risk information.

**Key capabilities**

- Return a county's top-5 most hazardous disaster types (CLI and web API).
- Query hazard ratings for one or more disasters in a county (CLI).
- Browser-based UI with templates and JavaScript to select counties and disasters.

**Stack**: Python, Flask, PostgreSQL (via `psycopg2`), simple HTML/CSS/JS for the frontend.

**Ports / defaults**: The Flask app runs on port `5100` when started with `python3 flask_app.py`.

**Repository layout**

- `command_line.py` — CLI entrypoint. Usage: `--disaster <disasters> --county <County,ST>` or `--top5 <County,ST>`.
- `flask_app.py` — Flask application with routes used by the web UI and API endpoints.
- `ProductionCode/datasource.py` — database connection and data access (expects a `COUNTY_AND_RISKVALUES` table).
- `ProductionCode/helper.py` — utility functions (validation, sorting, formatting, disaster lists).
- `Data/` — CSV files and SQL to create the table (`createtable.sql`).
- `templates/`, `static/` — web templates and static assets used by the Flask app.
- `Tests/` — unit tests for CLI and Flask routes (`test_cl.py`, `test_flask_app.py`).

## Quick start (How to use)

1. Create and activate a virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

If `requirements.txt` is missing or incomplete, at minimum install:

```sh
pip install Flask psycopg2-binary python-dotenv pytest
```

3. Create a PostgreSQL database (local or remote) and load the schema in `Data/createtable.sql` into it. Example using `psql`:

```sh
# replace names as desired)
createdb sand_db
# run table creation script
psql -d sand_db -f Data/createtable.sql
```

4. Load the CSV data into the `COUNTY_AND_RISKVALUES` table. You can use `COPY` or a GUI tool. Example (psql):

```sql
\copy COUNTY_AND_RISKVALUES FROM 'Data/County_and_Disasters_only.csv' DELIMITER ',' CSV HEADER;
```

5. Provide DB credentials via environment variables. Create a `.env` file in the project root with:

```
database=<your_database_name>
user=<db_user>
password=<db_password>
host=localhost
```

The `ProductionCode/datasource.py` uses these variables (via `python-dotenv`) to connect.

## CLI usage

All CLI behavior is implemented in `command_line.py`. Run examples from the repository root.

- Query one or multiple disasters in a county (comma-separated disasters):

```sh
python3 command_line.py --disaster 'Tornado' --county 'Los Angeles,CA'
python3 command_line.py --disaster 'Tornado,Earthquake' --county 'Los Angeles,CA'
```

- Get top-5 hazards for a county:

```sh
python3 command_line.py --top5 'Rice,MN'
```

Notes:

- County input must be in the format `Name,ST` (e.g. `Los Angeles,CA`).
- The CLI validates disaster names against the built-in list in `ProductionCode/helper.py`.

## Web UI

Start the Flask app (it listens on port `5100` in development mode):

```sh
python3 flask_app.py
```

Routes of interest:

- `/` — homepage (template `index.html`).
- `/<disaster>/<county>` — returns hazard ratings for the given disaster(s) and county.
- `/top5/<county>` — returns the top-5 hazards for `county`.
- `/displaycountydata` and `/top5` (with query parameters) — used by the web UI forms.

If you want to call the API directly, use the same patterns as the CLI but in the URL, for example:

```
http://localhost:5100/Earthquake/Los%20Angeles,CA
http://localhost:5100/top5/Los%20Angeles,CA
```

## Tests

The project includes `unittest` tests in `Tests/` that exercise the CLI and Flask routes. Run them with:

```sh
pytest -q
# OR
python -m unittest discover -v Tests
```

The tests rely on a working DB connection and populated `COUNTY_AND_RISKVALUES` table (see Data setup above).

## Contributing

- Fork, create a topic branch, add tests for behavior changes, and submit a pull request.
- Keep changes focused; follow PEP8 for Python code and document any schema changes.

## License

This project is available under the MIT License — see `LICENSE`.

## Contact

Maintainer: Dynamique Twizere — `twizered@carleton.edu`








