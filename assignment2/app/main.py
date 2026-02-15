from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FastAPI running behind Nginx"}

@app.get("/health")
def health():
    return {"health": "OK"}
