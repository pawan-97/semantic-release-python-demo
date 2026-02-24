from fastapi import FastAPI

app = FastAPI(title="Semantic Release Demo")

@app.get("/")
def read_root():
    return {"message": "Hello from semantic-release 🚀"}
