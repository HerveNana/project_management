// gantt.js - Script pour le diagramme de Gantt

// Fonction pour initialiser le diagramme de Gantt
function initGantt(projectId) {
    // Configuration de base du diagramme
    gantt.config.date_format = "%Y-%m-%d %H:%i";
    gantt.config.scale_unit = "week";
    gantt.config.date_scale = "%d %M";
    gantt.config.subscales = [
        {unit: "day", step: 1, date: "%D"}
    ];

    // Initialisation du diagramme
    gantt.init("gantt-container");

    // Chargement des données du projet
    gantt.load(`/api/project/${projectId}/gantt-data`);

    // Gestion des événements de modification des tâches
    gantt.attachEvent("onAfterTaskAdd", function(id, task){
        // Envoi des données de la nouvelle tâche au serveur
        sendTaskToServer('POST', task);
    });

    gantt.attachEvent("onAfterTaskUpdate", function(id, task){
        // Envoi des données mises à jour de la tâche au serveur
        sendTaskToServer('PUT', task);
    });
}

// Fonction pour envoyer les données de tâche au serveur
function sendTaskToServer(method, task) {
    fetch('/api/task', {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(task)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Tâche sauvegardée:', data);
    })
    .catch((error) => {
        console.error('Erreur:', error);
    });
}