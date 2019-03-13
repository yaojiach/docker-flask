# Docker Flask Boilerplate

**Tested on Mac, Linux, Windows**

Flask JWT boilerplate with `gunicorn`, `nginx`, and external `psql` database. Good for quickly set up an authentication backend (for example for a frontend development).

* Use `Pipfile` for dependency management. 
* Use `Flask-Restful` as the REST API framework.
* Use `Flask-JWT-Extended` as the (opinionated) JWT framework. Including features like `refresh token` and `token revoking`.

## Features

* Docker
* nginx
* gunicorn
* flask
* jwt

## Non-Features

* external Postgres

## Usage

Stand up external psql database

```sh
bash db/dbscript.sh
```

Build containers

```sh
docker-compose up --build
```

Kill processes

```sh
docker-compose rm -fs
```

To access (example in `Postman`):

![Registration Example](https://github.com/yaojiach/docker-flask-boilerplate/blob/master/postman-example.png)


## Gotchas

Set `PROPAGATE_EXCEPTIONS` to propagate exceptions from `flask-jwt-extended`

```python
class Config:
    ...
    PROPAGATE_EXCEPTIONS = True
```

Must include `Pipfile.lock` for `pipenv` to install system-wide in docker

```dockerfile
...
COPY Pipfile.lock /home/project/web
...
```

Use `host.docker.internal` inside container to access host machine's localhost

```sh
DATABASE_URL=postgresql://dev:12345@host.docker.internal:5432/jwt
```

## References

* https://github.com/oleg-agapov/flask-jwt-auth
* https://github.com/sladkovm/docker-flask-gunicorn-nginx
