# exceptions.py

class ProjectManagementException(Exception):
    """Exception de base pour l'application"""
    pass

class TaskDependencyException(ProjectManagementException):
    """Exception levée pour les problèmes de dépendance entre tâches"""
    pass

class ResourceNotFoundException(ProjectManagementException):
    """Exception levée quand une ressource n'est pas trouvée"""
    pass