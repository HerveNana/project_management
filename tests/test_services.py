from services.project_service import create_project, update_project, delete_project
from services.task_service import create_task, update_task, delete_task
from models.project import Project
from models.task import Task

def test_create_project(app, user):
    """
    ÉTANT DONNÉ un utilisateur existant
    QUAND la fonction create_project est appelée avec des données valides
    ALORS vérifier qu'un nouveau projet est créé dans la base de données
    """
    with app.app_context():
        project_data = {
            'name': 'New Project',
            'description': 'A new test project',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        }
        project = create_project(project_data, user.id)
        assert isinstance(project, Project)
        assert Project.query.count() == 1

def test_update_project(app, project):
    """
    ÉTANT DONNÉ un projet existant
    QUAND la fonction update_project est appelée avec de nouvelles données
    ALORS vérifier que le projet est mis à jour dans la base de données
    """
    with app.app_context():
        updated_data = {
            'name': 'Updated Project',
            'description': 'An updated test project',
            'start_date': '2023-02-01',
            'end_date': '2023-11-30'
        }
        updated_project = update_project(project, updated_data)
        assert updated_project.name == 'Updated Project'
        assert updated_project.description == 'An updated test project'

def test_delete_project(app, project):
    """
    ÉTANT DONNÉ un projet existant
    QUAND la fonction delete_project est appelée
    ALORS vérifier que le projet est supprimé de la base de données
    """
    with app.app_context():
        delete_project(project)
        assert Project.query.count() == 0

def test_create_task(app, project):
    """
    ÉTANT DONNÉ un projet existant
    QUAND la fonction create_task est appelée avec des données valides
    ALORS vérifier qu'une nouvelle tâche est créée dans la base de données
    """
    with app.app_context():
        task_data = {
            'name': 'New Task',
            'description': 'A new test task',
            'status': 'todo',
            'start_date': '2023-01-01',
            'end_date': '2023-01-31'
        }
        task = create_task(task_data, project.id)
        assert isinstance(task, Task)
        assert Task.query.count() == 1

def test_update_task(app, task):
    """
    ÉTANT DONNÉ une tâche existante
    QUAND la fonction update_task est appelée avec de nouvelles données
    ALORS vérifier que la tâche est mise à jour dans la base de données
    """
    with app.app_context():
        updated_data = {
            'name': 'Updated Task',
            'description': 'An updated test task',
            'status': 'in_progress',
            'start_date': '2023-02-01',
            'end_date': '2023-02-28'
        }
        updated_task = update_task(task, updated_data)
        assert updated_task.name == 'Updated Task'
        assert updated_task.status == 'in_progress'

def test_delete_task(app, task):
    """
    ÉTANT DONNÉ une tâche existante
    QUAND la fonction delete_task est appelée
    ALORS vérifier que la tâche est supprimée de la base de données
    """
    with app.app_context():
        delete_task(task)
        assert Task.query.count() == 0