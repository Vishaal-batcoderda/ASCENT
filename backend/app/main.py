from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "ASCENT",
        "status": "Backend Running 🚀"
    }