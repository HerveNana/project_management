# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration de l'application"""
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://username:password@localhost/project_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration du cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300
    
    # Configuration de l'upload de fichiers
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max-limit