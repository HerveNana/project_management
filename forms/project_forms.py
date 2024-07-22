from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class ProjectForm(FlaskForm):
    """Formulaire de création/édition de projet"""
    
    name = StringField('Nom du projet', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    start_date = DateField('Date de début', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('Date de fin', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Enregistrer')

    def validate_end_date(self, field):
        """Vérifie que la date de fin est postérieure à la date de début"""
        if field.data < self.start_date.data:
            raise ValidationError('La date de fin doit être postérieure à la date de début.')