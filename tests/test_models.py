from models.user import User
from models.project import Project
from models.task import Task

def test_new_user():
    """
    ÉTANT DONNÉ un modèle User
    QUAND un nouvel utilisateur est créé
    ALORS vérifier que les champs sont correctement définis
    """
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('password123')

def test_new_project(user):
    """
    ÉTANT DONNÉ un modèle Project
    QUAND un nouveau projet est créé
    ALORS vérifier que les champs sont correctement définis
    """
    project = Project(name='Test Project', description='A test project', owner_id=user.id)
    assert project.name == 'Test Project'
    assert project.description == 'A test project'
    assert project.owner_id == user.id

def test_new_task(project):
    """
    ÉTANT DONNÉ un modèle Task
    QUAND une nouvelle tâche est créée
    ALORS vérifier que les champs sont correctement définis
    """
    task = Task(name='Test Task', description='A test task', project_id=project.id)
    assert task.name == 'Test Task'
    assert task.description == 'A test task'
    assert task.project_id == project.id