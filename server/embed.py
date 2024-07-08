from sentence_transformers import SentenceTransformer

from . import config


def load_model():
    path = config.get_home()
    model_name = config.get_model_name()
    local_files_only = config.get_local_files_only()
    return SentenceTransformer(
        model_name,
        cache_folder=path,
        local_files_only=local_files_only,
        device='cpu'
    )


def embed(model, text):
    return model.encode(text)
