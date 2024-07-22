from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models.user import User

class TaskForm(FlaskForm):
    """Formulaire de création/édition de tâche"""
    
    name = StringField('Nom de la tâche', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    status = SelectField('Statut', choices=[('todo', 'À faire'), ('in_progress', 'En cours'), ('done', 'Terminé')])
    start_date = DateField('Date de début', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('Date de fin', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Enregistrer')

    def validate_end_date(self, field):
        """Vérifie que la date de fin est postérieure à la date de début"""
        if field.data < self.start_date.data:
            raise ValidationError('La date de fin doit être postérieure à la date de début.')

class AssignTaskForm(FlaskForm):
    """Formulaire d'assignation de tâche"""
    
    user = QuerySelectField('Assigner à', query_factory=lambda: User.query, get_label='username')
    submit = SubmitField('Assigner')