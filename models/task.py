# models/task.py

from extensions import db
from datetime import datetime

class Task(db.Model):
    """Modèle représentant une tâche"""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='todo')
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False, index=True)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)

    dependencies = db.relationship('Dependency', 
                                   foreign_keys='Dependency.task_id',
                                   backref=db.backref('task', lazy='joined'),
                                   lazy='dynamic',
                                   cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Task {self.name}>'