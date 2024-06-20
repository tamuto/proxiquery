import numpy as np
from fastapi import FastAPI
from fastapi import Body

from .embed import load_model
from .embed import embed

from .vector import load_index
from .vector import make_index

app = FastAPI()
model = load_model()
vec, map = load_index()


@app.get("/reindex")
def reindex():
    global vec, map
    vec, map = make_index(model)
    return {'status': 'done'}


@app.post("/query")
def query(body=Body(...)):
    """
    Query the model with a text.
    """
    text = body['text']
    emb = np.array([embed(model, text)])
    D, idx = vec.search(emb, 10)  # type: ignore
    results = [{'Q': map[i]['Q'], 'A': map[i]['A'], 'distance': str(d)} for i, d in zip(idx[0], D[0]) if d < 60]  # type: ignore
    return {'status': 'OK', 'items': results}  # TODO Result
