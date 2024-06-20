import os
import json
import faiss
import numpy as np

from . import config
from .embed import embed


def load_index():
    path = config.get_home()
    name = config.get_vector_name()
    if not os.path.exists(f'{path}/{name}.db'):
        return None, None
    index = faiss.read_index(f'{path}/{name}.db')
    with open(f'{path}/{name}.map', 'r') as f:
        map = json.load(f)
    return index, map


def make_index(llm):
    path = config.get_home()
    inp = f'{path}/{config.get_dataset()}'
    with open(inp, 'r') as f:
        data = json.load(f)

    embeds = np.array([embed(llm, d['Q']) for d in data])
    index = faiss.IndexFlatL2(embeds.shape[1], )
    index.add(embeds)  # type: ignore

    name = config.get_vector_name()
    faiss.write_index(index, f'{path}/{name}.db')

    with open(f'{path}/{name}.map', 'w') as f:
        json.dump(data, f)

    return index, data
