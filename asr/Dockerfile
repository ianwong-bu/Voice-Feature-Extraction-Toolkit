FROM huggingface/transformers-pytorch-gpu:latest

RUN python3 -m pip install datasets

WORKDIR /app
COPY asr.py .

ENTRYPOINT ["python3", "asr.py"]