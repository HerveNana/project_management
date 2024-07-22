// kanban.js - Script pour le tableau Kanban

// Fonction pour initialiser le tableau Kanban
function initKanban(projectId) {
    // Chargement des données du projet
    fetch(`/api/project/${projectId}/kanban-data`)
        .then(response => response.json())
        .then(data => {
            renderKanbanBoard(data);
            initializeDragAndDrop();
        });
}

// Fonction pour rendre le tableau Kanban
function renderKanbanBoard(data) {
    const columns = ['todo', 'in_progress', 'done'];
    columns.forEach(status => {
        const column = document.querySelector(`.kanban-column[data-status="${status}"]`);
        data[status].forEach(task => {
            const taskElement = createTaskElement(task);
            column.appendChild(taskElement);
        });
    });
}

// Fonction pour créer un élément de tâche
function createTaskElement(task) {
    const taskElement = document.createElement('div');
    taskElement.classList.add('kanban-item');
    taskElement.setAttribute('draggable', 'true');
    taskElement.setAttribute('data-task-id', task.id);
    taskElement.innerHTML = `
        <h3>${task.name}</h3>
        <p>${task.description}</p>
    `;
    return taskElement;
}

// Fonction pour initialiser le drag and drop
function initializeDragAndDrop() {
    const items = document.querySelectorAll('.kanban-item');
    const columns = document.querySelectorAll('.kanban-column');

    items.forEach(item => {
        item.addEventListener('dragstart', dragStart);
        item.addEventListener('dragend', dragEnd);
    });

    columns.forEach(column => {
        column.addEventListener('dragover', dragOver);
        column.addEventListener('dragenter', dragEnter);
        column.addEventListener('dragleave', dragLeave);
        column.addEventListener('drop', drop);
    });
}

// Fonctions de gestion des événements de drag and drop
function dragStart() {
    this.classList.add('dragging');
}

function dragEnd() {
    this.classList.remove('dragging');
}

function dragOver(e) {
    e.preventDefault();
}

function dragEnter(e) {
    e.preventDefault();
    this.classList.add('drag-over');
}

function dragLeave() {
    this.classList.remove('drag-over');
}

function drop() {
    this.classList.remove('drag-over');
    const taskId = document.querySelector('.dragging').getAttribute('data-task-id');
    const newStatus = this.getAttribute('data-status');
    updateTaskStatus(taskId, newStatus);
    this.appendChild(document.querySelector('.dragging'));
}

// Fonction pour mettre à jour le statut d'une tâche
function updateTaskStatus(taskId, newStatus) {
    fetch(`/api/task/${taskId}/status`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Statut de la tâche mis à jour:', data);
    })
    .catch((error) => {
        console.error('Erreur:', error);
    });
}