# docker-flask

Application Stack: python3, pip3, flask, and nginx.

### Container Details
Http requests will be forwarded through nginx on HTTP port 80 to the Flask uWSGI
application server. Server-side templates will be served from Flask, and all other static
files (js, css, img, html, etc) will be served with nginx by default.

If you need more sophisticated app configuration, check out:
http://flask.pocoo.org/docs/0.10/config/

--

```bash
# Running locally with flask dev server.
python run.py

# Running uWSGI locally.
uwsgi --http 127.0.0.1:5000 -w application:application

# Running uWSGI with nginx.
uwsgi --socket 127.0.0.1:5000 -w application:application
```

```bash
# These are the available URLS
localhost:5000
localhost:5000/boilerplate
```
