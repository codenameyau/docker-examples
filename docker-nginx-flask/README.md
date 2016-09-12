# docker-flask

Application Stack: python3, pip3, flask, and uWSGI with nginx.

### Container Details
Http requests will be forwarded through nginx on HTTP port 80 to the Flask uWSGI
application server. Server-side templates will be served from Flask, and all other static
files (js, css, img, html, etc) will be served with nginx by default.

If you need more sophisticated app configuration, check out:
http://flask.pocoo.org/docs/0.10/config/

--

```bash
# Running locally with flask dev server.
python3 run.py

# Running locally with uWSGI server.
uwsgi --socket 0.0.0.0:80 --protocol=http -w application:app
```
