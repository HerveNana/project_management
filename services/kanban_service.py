# services/kanban_service.py

from models.task import Task

def generate_kanban_data(project_id):
    """
    Génère les données pour le tableau Kanban
    
    :param project_id: ID du projet
    :return: Dictionnaire représentant les colonnes du tableau Kanban
    """
    tasks = Task.query.filter_by(project_id=project_id).all()
    kanban_data = {
        'todo': [],
        'in_progress': [],
        'done': []
    }
    
    for task in tasks:
        kanban_data[task.status].append({
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'assigned_to': task.assigned_to.username if task.assigned_to else 'Unassigned'
        })
    
    return kanban_data

def update_task_status(task_id, new_status):
    """
    Met à jour le statut d'une tâche
    
    :param task_id: ID de la tâche
    :param new_status: Nouveau statut
    :return: Objet Task mis à jour
    """
    task = Task.query.get_or_404(task_id)
    task.status = new_status
    db.session.commit()
    return task