FROM huggingface/transformers-pytorch-gpu:latest

RUN python3 -m pip --no-cache install datasets transformers evaluate jiwer soundfile librosa

WORKDIR /app
COPY src/. .

ENTRYPOINT ["python3", "/app/asr.py"]