# app.py

from flask import Flask
from config import Config
from extensions import db, migrate, login_manager, cache
from views import main, auth, project, task, user
from models import User

def create_app(config_class=Config):
    """
    Crée et configure l'application Flask.
    
    :param config_class: Classe de configuration à utiliser
    :return: Application Flask configurée
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cache.init_app(app)

    # Enregistrement des blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(project.bp)
    app.register_blueprint(task.bp)
    app.register_blueprint(user.bp)

    # Configuration du gestionnaire de connexion
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Gestion des erreurs
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    return app