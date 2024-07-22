// main.js - Script principal de l'application

// Fonction pour initialiser les éléments interactifs de la page
function initializePageElements() {
    // Exemple : Ajout d'une classe 'active' aux liens de navigation
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Fonction pour gérer les messages flash
function handleFlashMessages() {
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(message => {
        // Faire disparaître le message après 5 secondes
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
}

// Exécuter les fonctions lorsque le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
    initializePageElements();
    handleFlashMessages();
});