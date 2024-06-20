from sentence_transformers import SentenceTransformer

from . import config

def load_model():
    path = config.get_home()
    model_name = config.get_model_name()
    return SentenceTransformer(model_name, cache_folder=path)


def embed(model, text):
    return model.encode(text)
