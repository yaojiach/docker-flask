# Docker Flask Boilerplate

**Tested on Mac, Linux, Windows**

`Docker` + `Flask` + `JWT` boilerplate with `gunicorn`, `nginx`, and external (dockerized for dev) `Postgres` database. Good for quickly set up an authentication backend (for example for a frontend development). Implemented user registration, user login, access token, refresh token, and token revocation.

* Use `Pipfile` for dependency management.
* Use `Flask-Restful` as the REST API framework.
* Use `Flask-JWT-Extended` as the (opinionated) JWT framework. Including features like `refresh token` and `token revoking`.

## Features

* Docker
* nginx
* gunicorn
* flask
* jwt
* Postgres
* redis (Used to store jwt token information)

## Non-Features

* external `Postgres`
* Dockerized `Postgres` for dev

## Usage

Dev with dockerized `Postgres`

```sh
docker-compose --file docker-compose-dev.yml up --build
```

Stand up external `Postgres` database

```sh
bash db/dbscript.sh
```

Build containers

```sh
docker-compose up --build
```

Full clean up (remove `Postgres` volume)

```sh
docker stop $(docker ps -a -q)
docker-compose rm -fs
docker system prune -y
rm -rf postgres_data
```

User Registration example

```json
{
    "email": "test@test.com",
    "password": "12345"
}
```

Example in `Postman`:

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
