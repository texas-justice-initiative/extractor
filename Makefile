# setup
local_dev:
	poetry install --with dev

local_analytics:
	poetry install --with analytics

# start jupyter notebook (requires analytics environment to be installed)
# TODO: run from inside docker and then post url to command line?
jupyter: 
	poetry run jupyter-notebook

# run tests
unit_test:
	poetry run pytest --cov=tracker tests/unit/

excel_test:
	poetry run pytest --cov=tracker tests/unit/converters/test_xlsx.py

## the integration tests require a postgres db; so we need to start/stop it
integration_test: pg_start integration_runner pg_stop

integration_runner:
	poetry run pytest --cov=tracker tests/integration/*

# POSTGRES DATABASE
### start/stop database
pg_start:
	docker compose up -d

pg_stop:
	docker compose down

### management - requires db to be running
new_migration:
	poetry run alembic revision --autogenerate -m '$(name)'

db_history:
	poetry run alembic history --verbose

db_up:
	poetry run alembic upgrade head

db_down:
	poetry run alembic downgrade -1

db_destroy:
	poetry run alembic downgrade base

# requires user to be postgres; opens database with psql
db_query: pg_start
	docker exec -it postgres psql -U postgres python

db_export: pg_start
	mkdir -p ./backups && docker exec -t postgres pg_dumpall -c -U postgres | gzip > ./backups/tracker_db_backup_$$(date +"%Y-%m-%d_%H_%M_%S").gz
