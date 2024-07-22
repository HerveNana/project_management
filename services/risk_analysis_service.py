# services/risk_analysis_service.py

from models.task import Task
from models.dependency import Dependency

def calculate_critical_path(project_id):
    """
    Calcule le chemin critique du projet
    
    :param project_id: ID du projet
    :return: Liste des tâches sur le chemin critique
    """
    tasks = Task.query.filter_by(project_id=project_id).all()
    
    # Calcul des dates au plus tôt
    for task in tasks:
        task.earliest_start = task.start_date
        task.earliest_finish = task.end_date
        dependencies = Dependency.query.filter_by(task_id=task.id).all()
        for dep in dependencies:
            if dep.dependency.earliest_finish > task.earliest_start:
                task.earliest_start = dep.dependency.earliest_finish
                task.earliest_finish = task.earliest_start + (task.end_date - task.start_date)
    
    # Calcul des dates au plus tard
    for task in reversed(tasks):
        task.latest_finish = task.earliest_finish
        task.latest_start = task.earliest_start
        dependents = Dependency.query.filter_by(dependency_id=task.id).all()
        for dep in dependents:
            if dep.task.latest_start < task.latest_finish:
                task.latest_finish = dep.task.latest_start
                task.latest_start = task.latest_finish - (task.end_date - task.start_date)
    
    # Identification du chemin critique
    critical_path = [task for task in tasks if task.earliest_start == task.latest_start and task.earliest_finish == task.latest_finish]
    
    return critical_path

def calculate_project_risk(project_id):
    """
    Calcule le risque global du projet
    
    :param project_id: ID du projet
    :return: Score de risque (0-100)
    """
    tasks = Task.query.filter_by(project_id=project_id).all()
    critical_path = calculate_critical_path(project_id)
    
    # Cette fonction est un exemple simplifié. Vous devriez l'adapter à votre logique métier.
    risk_score = 0
    for task in critical_path:
        task_risk = calculate_task_risk(task)
        risk_score += task_risk
    
    return min(risk_score, 100)  # Plafonnement à 100

def calculate_task_risk(task):
    """
    Calcule le risque d'une tâche individuelle
    
    :param task: Objet Task
    :return: Score de risque de la tâche (0-100)
    """
    # Cette fonction est un exemple simplifié. Vous devriez l'adapter à votre logique métier.
    risk_score = 0
    
    # Facteur de risque basé sur la durée de la tâche
    task_duration = (task.end_date - task.start_date).days
    if task_duration > 30:
        risk_score += 20
    elif task_duration > 14:
        risk_score += 10
    
    # Facteur de risque basé sur les dépendances
    dependencies_count = task.dependencies.count()
    risk_score += dependencies_count * 5
    
    # Facteur de risque basé sur le statut
    if task.status == 'todo' and task.start_date < datetime.utcnow():
        risk_score += 15
    
    return min(risk_score, 100)  # Plafonnement à 100