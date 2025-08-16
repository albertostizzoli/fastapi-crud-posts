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

# creo una funzione per modificare un post esistente
@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post): # passo come parametro l'id del post da modificare
    posts = load_posts() # chiamo la funzione load_posts
    # ciclo per modificare i dati
    for p in posts:
        if  p["id"] == post_id:
            p["title"] = updated_post.title
            p["content"] = updated_post.content
            save_posts(posts) # chiamo la funzione save_posts per salvare il dato modificato
            return p
    raise HTTPException(status_code=404, detail="Post non trovato") # errore se il post non viene trovato

# creo una funzione per cancellare un post esistente
@app.delete("/posts/{post_id}")
def delete_post(post_id: int): # passo come parametro l'id del post da cancellare
    posts = load_posts() # chaimo la funzione load_posts
    for p in posts:
        if p["id"] == post_id: # tro il post_id del post del post selezionato
            posts.remove(p) # rimuovo il post selezionato
            save_posts(posts) # chiamo la funzione save_posts per aggiornare i posts
            return {"message": "Post cancellato"} # messaggio di conferma
    raise HTTPException(status_code=404, detail="Post non trovato") #errore se il post non viene trovato