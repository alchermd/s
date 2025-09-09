# Makefile for Django project "s"

PYTHON := python
MANAGE := docker compose exec web python src/manage.py

.PHONY: help run shell migrate makemigrations superuser

help:
	@echo "Common Django commands:"
	@echo "  make up              # Run dev server"
	@echo "  make shell            # Django shell"
	@echo "  make migrate          # Apply migrations"
	@echo "  make makemigrations   # Create migrations"
	@echo "  make superuser        # Create a superuser"
	@echo "  make <command>        # Run 'manage.py <command>'"

up:
	docker compose up --build

shell:
	$(MANAGE) shell

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

superuser:
	$(MANAGE) createsuperuser

i:
	docker compose exec web uv add $(pkg)

idev:
	docker compose exec web uv add --dev $(pkg)

# Catch-all: forward any unknown target to manage.py
%:
	$(MANAGE) $@
