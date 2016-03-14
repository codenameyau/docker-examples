# docker-flask

```bash
# Running uWSGI locally.
uwsgi --http 127.0.0.1:8000 -w application:application

# Running uWSGI with nginx.
uwsgi --socket 127.0.0.1:8000 -w application:application
```
