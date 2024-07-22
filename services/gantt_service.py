# services/gantt_service.py

from models.task import Task

def generate_gantt_data(project_id):
    """
    Génère les données pour le diagramme de Gantt
    
    :param project_id: ID du projet
    :return: Liste de dictionnaires représentant les tâches pour le diagramme de Gantt
    """
    tasks = Task.query.filter_by(project_id=project_id).all()
    gantt_data = []
    
    for task in tasks:
        gantt_data.append({
            'id': task.id,
            'text': task.name,
            'start_date': task.start_date.strftime('%Y-%m-%d %H:%M'),
            'end_date': task.end_date.strftime('%Y-%m-%d %H:%M'),
            'progress': calculate_progress(task),
            'dependencies': [dep.dependency_id for dep in task.dependencies]
        })
    
    return gantt_data

def calculate_progress(task):
    """
    Calcule le progrès d'une tâche
    
    :param task: Objet Task
    :return: Pourcentage de progression (0-100)
    """
    # Cette fonction est un exemple simplifié. Vous devriez l'adapter à votre logique métier.
    if task.status == 'done':
        return 100
    elif task.status == 'in_progress':
        return 50
    else:
        return 0