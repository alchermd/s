# s

A private URL shortener service.

## Local Setup

```console
$ make up
$ make migrate
```

## Github Actions setup

This repo depends on several secrets to be set in the repo settings:

- `DO_TOKEN`: DigitalOcean API token with write access to push images to DO container registry.
