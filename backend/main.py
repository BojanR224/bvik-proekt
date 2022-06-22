import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

# conda activate bvik-env
# Ovaa komanda pisi ja vo wsl terminal uvicorn --reaload --host=0.0.0.0 --port=8080 app.:app