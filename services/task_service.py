# services/task_service.py

from models.task import Task
from extensions import db

def create_task(data, project_id):
    """
    Crée une nouvelle tâche
    
    :param data: Données de la tâche
    :param project_id: ID du projet parent
    :return: Objet Task créé
    """
    task = Task(
        name=data['name'],
        description=data['description'],
        status=data['status'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        project_id=project_id
    )
    db.session.add(task)
    db.session.commit()
    return task

def update_task(task, data):
    """
    Met à jour une tâche existante
    
    :param task: Objet Task à mettre à jour
    :param data: Nouvelles données de la tâche
    :return: Objet Task mis à jour
    """
    task.name = data['name']
    task.description = data['description']
    task.status = data['status']
    task.start_date = data['start_date']
    task.end_date = data['end_date']
    db.session.commit()
    return task

def delete_task(task):
    """
    Supprime une tâche
    
    :param task: Objet Task à supprimer
    """
    db.session.delete(task)
    db.session.commit()

def assign_task(task, user):
    """
    Assigne une tâche à un utilisateur
    
    :param task: Objet Task à assigner
    :param user: Objet User à qui assigner la tâche
    :return: Objet Task mis à jour
    """
    task.assigned_to = user
    db.session.commit()
    return task