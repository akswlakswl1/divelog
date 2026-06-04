from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/progress")
def progress():
    with open("progress.md", "r") as f:
      content = f.read()
    return {"content":content}