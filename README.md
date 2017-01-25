## Docker Flask Boilerplate

* Docker
* nginx
* gunicorn
* flask
* postgres
* data migration
  * Add migrations folder
```sh
docker-compose run web /usr/local/bin/python manage.py db init
```

  * Create db
```sh
docker-compose run web /usr/local/bin/python manage.py create_db
```

  * Migaration and upgrade
```sh
docker-compose run web /usr/local/bin/python manage.py db migrate
docker-compose run web /usr/local/bin/python manage.py db upgrade
```


## TODO

* authentication/JWT
* testing
* mongodb
* npm/node
* react/redux/webpack/etc
* separate dev/prod configs
