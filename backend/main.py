import hypercorn

if __name__ == "__main__":
    hypercorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

# conda activate bvik-env
# Ovaa komanda pisi ja vo wsl terminal uvicorn --reload --host=0.0.0.0 --port=8080 app.api:app