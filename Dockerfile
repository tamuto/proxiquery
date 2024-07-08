FROM python:3.11-slim-bullseye

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install \
    fastapi \
    uvicorn \
    faiss-cpu \
    packaging \
    transformers \
    tqdm \
    numpy \
    scikit-learn \
    nltk \
    sentencepiece \
    Pillow \
    datasets
RUN pip install --no-deps sentence-transformers

RUN mkdir /proxiquery \
&&  mkdir /app
WORKDIR /app
COPY server server

# portを開ける
EXPOSE 8000

# コンテナの実行コマンドを指定するインストラクション 最後に記述する
CMD python -m uvicorn server.main:app --host 0.0.0.0 --port 8000
