# views/task.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.task import Task
from models.project import Project
from forms.task_forms import TaskForm, AssignTaskForm
from services.task_service import create_task, update_task, delete_task, assign_task
from extensions import db, cache

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/create/<int:project_id>', methods=['GET', 'POST'])
@login_required
def create(project_id):
    """Gère la création d'une nouvelle tâche"""
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to add tasks to this project.')
        return redirect(url_for('project.detail', project_id=project_id))
    
    form = TaskForm()
    if form.validate_on_submit():
        task = create_task(form.data, project_id)
        flash('Task created successfully.')
        return redirect(url_for('project.detail', project_id=project_id))
    return render_template('task/create.html', form=form, project=project)

@bp.route('/<int:task_id>')
@login_required
@cache.cached(timeout=60)
def detail(task_id):
    """Affiche les détails d'une tâche"""
    task = Task.query.get_or_404(task_id)
    if task.project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to view this task.')
        return redirect(url_for('project.list_projects'))
    return render_template('task/detail.html', task=task)

@bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    """Gère l'édition d'une tâche"""
    task = Task.query.get_or_404(task_id)
    if task.project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to edit this task.')
        return redirect(url_for('project.detail', project_id=task.project_id))
    
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        update_task(task, form.data)
        flash('Task updated successfully.')
        return redirect(url_for('task.detail', task_id=task.id))
    return render_template('task/edit.html', form=form, task=task)

@bp.route('/<int:task_id>/delete', methods=['POST'])
@login_required
def delete(task_id):
    """Gère la suppression d'une tâche"""
    task = Task.query.get_or_404(task_id)
    if task.project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this task.')
        return redirect(url_for('project.detail', project_id=task.project_id))
    
    project_id = task.project_id
    delete_task(task)
    flash('Task deleted successfully.')
    return redirect(url_for('project.detail', project_id=project_id))

@bp.route('/<int:task_id>/assign', methods=['GET', 'POST'])
@login_required
def assign(task_id):
    """Gère l'assignation d'une tâche à un utilisateur"""
    task = Task.query.get_or_404(task_id)
    if task.project.owner_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to assign this task.')
        return redirect(url_for('project.detail', project_id=task.project_id))
    
    form = AssignTaskForm()
    if form.validate_on_submit():
        assign_task(task, form.user.data)
        flash('Task assigned successfully.')
        return redirect(url_for('task.detail', task_id=task.id))
    return render_template('task/assign.html', form=form, task=task)