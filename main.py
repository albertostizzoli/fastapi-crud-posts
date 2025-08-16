from fastapi import FastAPI # importo FastAPI

app = FastAPI() # creo l'istanza di FastAPI

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