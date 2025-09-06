
from typing import Union
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Endpoint pesado para teste de performance
@app.get("/heavy-counter")
def heavy_counter(n: int = 100_000_000):
    start = time.time()
    count = 0
    for i in range(n):
        count += i % 7  
    elapsed = time.time() - start
    return {"result": count, "elapsed_seconds": elapsed, "n": n}

