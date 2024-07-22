# views/project.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.project import Project
from forms.project_forms import ProjectForm
from services.project_service import create_project, update_project, delete_project
from extensions import db, cache

bp = Blueprint('project', __name__, url_prefix='/project')

@bp.route('/')
@login_required
@cache.cached(timeout=60)
def list_projects():
    """Affiche la liste des projets de l'utilisateur"""
    projects = Project.query.filter_by(owner_id=current_user.id).all()
    return render_template('project/list.html', projects=projects)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Gère la création d'un nouveau projet"""
    form = ProjectForm()
    if form.validate_on_submit():
        project = create_project(form.data, current_user.id)
        flash('Project created successfully.')
        return redirect(url_for('project.detail', project_id=project.id))
    return render_template('project/create.html', form=form)

@bp.route('/<int:project_id>')
@login_required
def detail(project_id):
    """Affiche les détails d'un projet"""
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to view this project.')
        return redirect(url_for('project.list_projects'))
    return render_template('project/detail.html', project=project)

@bp.route('/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(project_id):
    """Gère l'édition d'un projet"""
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to edit this project.')
        return redirect(url_for('project.list_projects'))
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        update_project(project, form.data)
        flash('Project updated successfully.')
        return redirect(url_for('project.detail', project_id=project.id))
    return render_template('project/edit.html', form=form, project=project)

@bp.route('/<int:project_id>/delete', methods=['POST'])
@login_required
def delete(project_id):
    """Gère la suppression d'un projet"""
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this project.')
        return redirect(url_for('project.list_projects'))
    delete_project(project)
    flash('Project deleted successfully.')
    return redirect(url_for('project.list_projects'))