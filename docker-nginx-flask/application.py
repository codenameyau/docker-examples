from config import PRODUCTION
from app import application

if __name__ == "__main__":
    application.run(**PRODUCTION)
