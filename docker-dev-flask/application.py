from app.config import PRODUCTION
from app.routes import app

if __name__ == '__main__':
    app.run(**PRODUCTION)
