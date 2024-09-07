import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'votre_secret_key'
    JWT_SECRET_KEY = 'votre_jwt_secret'
