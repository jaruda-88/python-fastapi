from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def run():
    import uvicorn
    uvicorn.run(app)


if __name__ == "__main__":
    run()