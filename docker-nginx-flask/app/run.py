from config import DEVELOPMENT
from routes import app

if __name__ == '__main__':
    app.run(**DEVELOPMENT)
