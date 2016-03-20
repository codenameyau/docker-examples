# docker-flask

Static files will be served with nginx.

```bash
# Running locally with flask dev server.
python run.py

# Running uWSGI locally.
uwsgi --http 127.0.0.1:5000 -w application:application

# Running uWSGI with nginx.
uwsgi --socket 127.0.0.1:5000 -w application:application
```

```
# Available URLS:
localhost:5000
localhost:5000/boilerplate
```
