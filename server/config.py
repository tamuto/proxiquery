import os


def get_model_name():
    return os.getenv('PROXIQUERY_MODEL_NAME', 'stsb-xlm-r-multilingual')


def get_home():
    return os.getenv('PROXIQUERY_PATH', '/proxiquery')


def get_dataset():
    return os.getenv('PROXIQUERY_DATASET', 'dataset.json')


def get_vector_name():
    return os.getenv('PROXIQUERY_VECTOR_NAME', 'vector')
