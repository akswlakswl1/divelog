from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def parse_progress():
    with open("progress.md", "r") as f:
        content = f.read()
    lines = content.split("\n")

    project = {}
    for i, line in enumerate(lines):
        if "진행 중인 프로젝트" in line:
            project["name"] = lines[i+1].split(": ", 1)[1]
            project["last_step"] = lines[i+2].split(": ", 1)[1]
            project["next_step"] = lines[i+3].split(": ", 1)[1]

    error_log = []
    for line in lines:
        if line.startswith(("1.", "2.", "3.", "4.")):
            parts = line.split("|")
            error_log.append({
                "topic": parts[0].strip(),
                "next_review": parts[4].strip()
            })

    return {"project": project, "error_log": error_log}


@app.get("/progress")
def progress():
    return parse_progress()
