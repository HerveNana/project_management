import pytest
from app import create_app
from extensions import db
from models.user import User
from models.project import Project
from models.task import Task

@pytest.fixture
def app():
    """Crée et configure une nouvelle instance de l'application pour chaque test."""
    app = create_app('testing')
    
    # Crée un contexte d'application
    with app.app_context():
        # Crée les tables de la base de données
        db.create_all()
        yield app
        # Nettoie la base de données après chaque test
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Un client de test pour envoyer des requêtes à l'application."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Un runner de test pour appeler des commandes Click."""
    return app.test_cli_runner()

@pytest.fixture
def user(app):
    """Crée un utilisateur de test."""
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def project(app, user):
    """Crée un projet de test."""
    project = Project(name='Test Project', description='A test project', owner_id=user.id)
    db.session.add(project)
    db.session.commit()
    return project

@pytest.fixture
def task(app, project):
    """Crée une tâche de test."""
    task = Task(name='Test Task', description='A test task', project_id=project.id)
    db.session.add(task)
    db.session.commit()
    return task