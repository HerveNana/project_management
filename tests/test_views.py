import json

def test_home_page(client):
    """
    ÉTANT DONNÉ un client Flask configuré pour les tests
    QUAND la page d'accueil ('/) est demandée (GET)
    ALORS vérifier que la réponse est valide
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenue sur notre application de Gestion de Projet" in response.data

def test_login(client):
    """
    ÉTANT DONNÉ un client Flask configuré pour les tests
    QUAND une requête POST est envoyée à '/login' avec des identifiants valides
    ALORS vérifier que la connexion est réussie
    """
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Connexion réussie" in response.data

def test_create_project(client, user):
    """
    ÉTANT DONNÉ un utilisateur connecté
    QUAND une requête POST est envoyée à '/project/create' avec des données de projet valides
    ALORS vérifier que le projet est créé avec succès
    """
    client.post('/login', data={'username': user.username, 'password': 'password123'})
    response = client.post('/project/create', data={
        'name': 'New Project',
        'description': 'A new test project'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Projet créé avec succès" in response.data

def test_create_task(client, user, project):
    """
    ÉTANT DONNÉ un utilisateur connecté et un projet existant
    QUAND une requête POST est envoyée à '/task/create/<project_id>' avec des données de tâche valides
    ALORS vérifier que la tâche est créée avec succès
    """
    client.post('/login', data={'username': user.username, 'password': 'password123'})
    response = client.post(f'/task/create/{project.id}', data={
        'name': 'New Task',
        'description': 'A new test task'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Tâche créée avec succès" in response.data