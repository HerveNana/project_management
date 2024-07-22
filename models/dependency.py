# models/dependency.py

from extensions import db

class Dependency(db.Model):
    """Modèle représentant une dépendance entre tâches"""
    
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, index=True)
    dependency_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, index=True)

    def __repr__(self):
        return f'<Dependency {self.task_id} -> {self.dependency_id}>'