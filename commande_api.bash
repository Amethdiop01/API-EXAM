#!/bin/bash

# Endpoint pour vérifier que l'API est fonctionnelle
echo "Endpoint pour vérifier que l'API est fonctionnelle :"
curl -X GET "http://127.0.0.1:8000/"

# Endpoint pour authentifier l'utilisateur
echo "Endpoint pour authentifier l'utilisateur :"
curl -X GET "http://127.0.0.1:8000/login/" -u "alice:wonderland"

# Endpoint pour créer une nouvelle question
echo "Endpoint pour créer une nouvelle question :"
curl -X POST "http://127.0.0.1:8000/create_question/" -u "admin:4dm1N" -H "Content-Type: application/json" -d '{
    "question": "Quelle est la capitale de la France ?",
    "subject": "Géographie",
    "use": "Test de géographie",
    "correct": "Paris",
    "responseA": "Paris",
    "responseB": "Londres",
    "responseC": "Berlin"
}'

# Endpoint pour récupérer des questions aléatoires
echo "Endpoint pour récupérer des questions aléatoires :"
curl -X GET "http://127.0.0.1:8000/get_questions/?use=Test%20de%20positionnement&subject=BDD&count=5"
