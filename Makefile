create-repo:
	docker run --name ctrl-leitos-psql -e "POSTGRES_PASSWORD=postgres" -p 5433:5432 -d postgres

start-repo:
	docker start ctrl-leitos-psql

create-tables:
	@export ENV='commit'
	@python3.9 ./src/database/repo.py
	@export ENV='desenv'