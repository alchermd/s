-include .env.mk
SHELL := /bin/bash
APP_NAME := s
REGISTRY := registry.digitalocean.com/alcher-dev-registry
IMAGE_LATEST := $(REGISTRY)/$(APP_NAME):latest
IMAGE_UNIQUE := $(REGISTRY)/$(APP_NAME):$(shell git rev-parse --short HEAD)
DC := docker compose
MANAGE := $(DC) exec s python src/manage.py

.PHONY: help run shell migrate makemigrations superuser

help:
	@echo "Commands:"
	@echo "  make up                       # Run dev server"
	@echo "  make push                     # Build and push image to DO Container Registry"
	@echo "  make shell                    # Django shell"
	@echo "  make migrate          		   # Apply migrations"
	@echo "  make makemigrations           # Create migrations"
	@echo "  make superuser                # Create a superuser"
	@echo "  make i pkg=<package name>     # Install a Python package"
	@echo "  make idev pkg=<package name>  # Install a Python package as a dev dependency"
	@echo "  make <command>                # Run 'manage.py <command>'"

up:
	$(DC) up --build

# Push to DO Container Registry
push:
	# Login
	echo $(DO_TOKEN) | docker login $(REGISTRY) --username doctl --password-stdin
	# Build the Compose image
	$(DC) build $(APP_NAME)
	docker tag $(APP_NAME):latest $(IMAGE_LATEST)
	docker tag $(APP_NAME):latest $(IMAGE_UNIQUE)
	# Push both tags
	docker push $(IMAGE_LATEST)
	docker push $(IMAGE_UNIQUE)
	echo "Successfully pushed $(IMAGE_LATEST) and $(IMAGE_UNIQUE)"

shell:
	$(MANAGE) shell

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

superuser:
	$(MANAGE) createsuperuser

i:
	uv add $(pkg)

idev:
	uv add --dev $(pkg)

# Catch-all: forward any unknown target to manage.py
%:
	$(MANAGE) $@
