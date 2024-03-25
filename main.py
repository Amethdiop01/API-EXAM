from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import csv
import random

app = FastAPI()

security = HTTPBasic()

# Chargement des données depuis le fichier CSV
questions_db = []
with open('questions.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        questions_db.append(row)

# Modèle pour représenter une question
class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str] = None
    remark: Optional[str] = None

# Endpoint pour vérifier que l'API est fonctionnelle
@app.get("/")
async def root():
    return {"message": "API fonctionnelle"}

# Endpoint pour authentifier l'utilisateur
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()
security = HTTPBasic()

@app.get("/login/")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    users = {
        "alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine"
    }
    if credentials.username in users and credentials.password == users[credentials.username]:
        return {"message": "Authentification réussie"}
    else:
        raise HTTPException(status_code=401, detail="Identifiants invalides")


# Endpoint pour créer une nouvelle question (accessible aux administrateurs uniquement)
@app.post("/create_question/")
async def create_question(question: Question, credentials: HTTPBasicCredentials = Depends(security)):
    users = {
        "alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine"
    }
    if credentials.username == "admin" and credentials.password == "4dm1N":
        questions_db.append(question.dict())
        return {"message": "Question créée avec succès"}
    else:
        raise HTTPException(status_code=403, detail="Accès non autorisé")

# Modèle pour représenter les données envoyées dans le corps de la requête
class RequestData(BaseModel):
    use: str
    subjects: str
    count: int = 5

# Endpoint pour récupérer des questions aléatoires
@app.get("/get_questions/")
async def get_questions(use: str, subject: str, count: int = 5):
    filtered_questions = [q for q in questions_db if q['use'] == use and q['subject'] == subject]
    if len(filtered_questions) < count:
        raise HTTPException(status_code=400, detail="Pas assez de questions disponibles")
    random_questions = random.sample(filtered_questions, count)
    return random_questions
