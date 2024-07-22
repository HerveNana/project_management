# models/user.py

from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Modèle représentant un utilisateur"""
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    tasks = db.relationship('Task', backref='assigned_to', lazy='dynamic')

    def set_password(self, password):
        """Définit le mot de passe de l'utilisateur"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Vérifie le mot de passe de l'utilisateur"""
        return check_password_hash(self.password_hash, password)