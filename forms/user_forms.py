from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models.user import User
from flask_login import current_user

class EditProfileForm(FlaskForm):
    """Formulaire de modification de profil"""
    
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Nouveau mot de passe', validators=[Length(min=6)])
    password2 = PasswordField(
        'Répéter le nouveau mot de passe', validators=[EqualTo('password')])
    submit = SubmitField('Mettre à jour')

    def validate_username(self, username):
        """Vérifie que le nouveau nom d'utilisateur n'est pas déjà utilisé"""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')

    def validate_email(self, email):
        """Vérifie que le nouvel email n'est pas déjà utilisé"""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Cet email est déjà utilisé. Veuillez en choisir un autre.')

class AdminUserForm(FlaskForm):
    """Formulaire d'édition d'utilisateur par un administrateur"""
    
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    is_admin = BooleanField('Administrateur')
    submit = SubmitField('Mettre à jour')

    def __init__(self, original_username, *args, **kwargs):
        super(AdminUserForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        """Vérifie que le nouveau nom d'utilisateur n'est pas déjà utilisé"""
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')