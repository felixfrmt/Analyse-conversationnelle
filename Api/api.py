from fastapi import FastAPI
import uvicorn

app = FastAPI(title="API Deployment", description="API Deployment on github.com", version="1.0")


@app.get("/")
def root():
    return {"msg": "Hello World"}



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
