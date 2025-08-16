from fastapi import FastAPI, HTTPException # importo FastAPI e HTTPException per la gestione degli errori
from pydantic import BaseModel # importo BaseModel per la validazione dei dati
import json # importo json per la gestione dei dati in formato JSON
import os # importo os per la gestione dei percorsi dei file

app = FastAPI() # creo l'istanza di FastAPI

# creo una classe Post per rappresentare i dati 
class Post(BaseModel):
    title: str
    content: str

POSTS_FILE = "posts.json" # file dove verranno salvati i post

# creo una funzione per caricare i post da un file JSON
def load_posts():
    if not os.path.exists(POSTS_FILE): # controllo se il file esiste
        return []
    with open(POSTS_FILE, "r", encoding="utf-8") as f: # apro il file in modalità lettura
        return json.load(f) # carico i dati dal file JSON

# creo una funzione per salvare i post su un file JSON
def save_posts(posts):
    with open(POSTS_FILE, "w", encoding="utf-8") as f: # apro il file in modalità scrittura
        json.dump(posts, f, ensure_ascii=False, indent=4) # salvo i dati in formato JSON 


# creo una funzione per ottenere tutti i post
@app.get("/posts")
def get_posts():
    return load_posts()

# creo una funzione per creare un nuovo post
@app.post("/posts")
def create_post(post: Post):
    posts = load_posts() # chiamo la funzione load_posts
    # Controllo duplicati
    for p in posts:
        if p["title"] == post.title and p["content"] == post.content:
            raise HTTPException(status_code=400, detail="Post già esistente")
    # Calcolo nuovo id
    new_id = max([p["id"] for p in posts], default=0) + 1 # calcolo il nuovo id come il massimo id esistente + 1
    new_post = {"id": new_id, "title": post.title, "content": post.content} # creo un nuovo post con l'id, il titolo e il contenuto
    posts.append(new_post) # aggiungo il nuovo post alla lista dei post
    save_posts(posts) # chiamo la funzione save_posts per salvare i post aggiornati
    return new_post