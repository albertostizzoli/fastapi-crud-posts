# 📝 FastAPI-CRUD-Posts

Questo progetto è una semplice API REST realizzata con **FastAPI** per gestire post di tipo blog, salvandoli in un file JSON locale. Supporta operazioni di **creazione**, **lettura**, **aggiornamento** e **cancellazione** dei post (CRUD).

---

## 🛠️ Ambiente di sviluppo

Durante lo sviluppo del progetto, sono state create due cartelle importanti:

- **`.venv`** 🔹  
  Contiene l'ambiente virtuale Python, dove sono installate tutte le dipendenze del progetto.  
  Grazie a `.venv` è possibile isolare le librerie del progetto da quelle globali del sistema.

- **`__pycache__`** 📦  
  Contiene file compilati di Python (`.pyc`) generati automaticamente per velocizzare l'esecuzione dello script.  
  Non è necessario modificarli manualmente.

> ⚠️ Queste cartelle di solito **non si includono nel repository Git**, quindi è consigliabile aggiungerle al file `.gitignore`.

---

## ⚡ Funzionalità

L'API permette di:

- Ottenere tutti i post (`GET /posts`)
- Creare un nuovo post (`POST /posts`)
- Modificare un post esistente (`PUT /posts/{post_id}`)
- Cancellare un post (`DELETE /posts/{post_id}`)

Ogni post è composto dai seguenti campi:

- `id` (intero, generato automaticamente)
- `title` (stringa, titolo del post)
- `content` (stringa, contenuto del post)

---

## 📁 Struttura del progetto
- `main.py` - Script principale con la definizione dell'API.
- `posts.json` - File JSON dove vengono salvati tutti i post.

---

## ⚙️ Come funziona

1. **Creazione dell'API**:  
   Lo script utilizza `FastAPI` per creare le route dell'API e `Pydantic` per la validazione dei dati dei post.

2. **Gestione dei dati**:  
   I post vengono salvati in un file JSON locale (`posts.json`).  
   - `load_posts()` legge i post dal file JSON.  
   - `save_posts(posts)` scrive i post aggiornati sul file JSON.

3. **Operazioni CRUD**:

   - **Leggere tutti i post** (`GET /posts`) 📄: restituisce la lista di tutti i post salvati.
   - **Creare un post** (`POST /posts`) ✏️: accetta un JSON con `title` e `content`, verifica se il post esiste già, assegna un nuovo `id` e salva il post.
   - **Aggiornare un post** (`PUT /posts/{post_id}`) 🔄: modifica il titolo e il contenuto di un post esistente identificato dall'`id`.
   - **Cancellare un post** (`DELETE /posts/{post_id}`) 🗑️: elimina un post esistente identificato dall'`id`.

4. **Gestione degli errori** ⚠️:  
   L'API restituisce errori appropriati:
   - `400 Bad Request` se si tenta di creare un post duplicato.
   - `404 Not Found` se si prova ad aggiornare o cancellare un post inesistente.

---

## 🚀 Avvio API

1. Installare le dipendenze
```
pip install fastapi uvicorn pydantic
```
2. Avviare il server
```
uvicorn main:app --reload
```
