from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from users.models import User
import database


app = FastAPI()

DB_SESSION = None


@app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = database.get_sesion()
    sync_table(User)


@app.get("/")
async def root():
    return {
        "data": "Hello World",
    }
