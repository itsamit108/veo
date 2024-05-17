from fastapi import FastAPI

# import config

app = FastAPI()

# settings = config.get_settings()


@app.get("/")
async def root():
    return {
        "data": "Hello World",
    }
