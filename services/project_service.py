# services/project_service.py

from models.project import Project
from extensions import db

def create_project(data, owner_id):
    """
    Crée un nouveau projet
    
    :param data: Données du projet
    :param owner_id: ID de l'utilisateur propriétaire
    :return: Objet Project créé
    """
    project = Project(
        name=data['name'],
        description=data['description'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        owner_id=owner_id
    )
    db.session.add(project)
    db.session.commit()
    return project

def update_project(project, data):
    """
    Met à jour un projet existant
    
    :param project: Objet Project à mettre à jour
    :param data: Nouvelles données du projet
    :return: Objet Project mis à jour
    """
    project.name = data['name']
    project.description = data['description']
    project.start_date = data['start_date']
    project.end_date = data['end_date']
    db.session.commit()
    return project

def delete_project(project):
    """
    Supprime un projet
    
    :param project: Objet Project à supprimer
    """
    db.session.delete(project)
    db.session.commit()