from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from users.models import User
import database


app = FastAPI()

DB_SESSION = None


@app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = database.get_session()
    sync_table(User)


@app.get("/")
async def root():
    return {
        "data": "Hello World",
    }


@app.get("/users")
async def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)
