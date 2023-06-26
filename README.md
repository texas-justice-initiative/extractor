TODO:
- Make devcontainer
- Make test resources/sample tests for xlsx extraction
- Make test resources/sample tests for pdf extraction
- Make schema for final table
- START WITH PREGNANT INMATES

# TJI Data Extractor

Scrapers, parsers, and loaders for various reports on jails, prisons, and police produced by the government of Texas.

## Contents

## Architecture

## Repo Structure

## Setup

### System Requirements
1. [Pyenv](https://github.com/pyenv/pyenv)
2. [Poetry](https://python-poetry.org/docs/#installation)
3. To use the local database, you need to install Docker and Docker Compose PLugin following [these instructions](https://docs.docker.com/desktop/).

## Development

Makefile commands:
- `make local_dev`: Install poetry environment with dev dependencies
- `make local_analytics`: Install analytics dependencies
- `make jupyter`: Run a jupyter notebook

### Pre-commit hooks

Pre-commit hooks are run after each commit to ensure consistent formatting, linting, and use of types.

### Running tests

To run unit tests: `make unit_test`

### Github Actions

Checks run:
- Confirm Black code formatter was run
- Tests/Code Coverage
- Type Checking (TODO)
- Confirm Changelog updated (TODO)

### Database Migrations

Database migrations are managed by Alembic. The most common commands are included in the Makefile.

- `make local_db`: Run Docker Compose to create a local version of the database and run all available migrations (Required before all other commands)
- `make migration`: Create a new revision to add/delete tables and columns
- `make db_history`: Get a verbose version of the database's migrations so far
- `make db_up`: Upgrade to the latest migration
- `make db_down`: Go back one migration
- `make db_query`: Open a psql terminal to query database directly. [See command reference](https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/).

The up/down commands require a running local database, which can be created by running the docker compose.

# how to access the db:
https://stackoverflow.com/questions/37694987/connecting-to-postgresql-in-a-docker-container-from-outside
`docker exec -it postgres-container psql -U postgres`