build:
	sudo docker compose up --build

run:
	sudo docker compose up

stop:
	sudo docker compose stop

up:
	uvicorn src.main:app --reload

seed:
	python -m seeds.seed
