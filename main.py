from fastapi import FastAPI, HTTPException # importo FastAPI e HTTPException per la gestione degli errori
from pydantic import BaseModel # importo BaseModel per la validazione dei dati

app = FastAPI() # creo l'istanza di FastAPI

# creo una classe Post per rappresentare i dati 
class Post(BaseModel):
    title: str
    content: str

# Posts
posts = [
    {"id": 1, "title": "Vacanze", "content": "Che bello andare in vacanza!"},
    {"id": 2, "title": "Informatica", "content": "L'informatica è interessante!"},
    {"id": 3, "title": "Videogiochi", "content": "I videogiochi sono divertenti!"},
]

# creo una funzione per ottenere tutti i post
@app.get("/posts")
def get_posts():
    return posts

# creo una funzione per creare un nuovo post
@app.post("/posts")
def create_post(post: Post):
    # Controllo duplicati
    for p in posts:
        if p["title"] == post.title and p["content"] == post.content:
            raise HTTPException(status_code=400, detail="Post già esistente")
    # Calcolo nuovo id
    new_id = max([p["id"] for p in posts], default=0) + 1
    new_post = {"id": new_id, "title": post.title, "content": post.content}
    posts.append(new_post)
    return new_post