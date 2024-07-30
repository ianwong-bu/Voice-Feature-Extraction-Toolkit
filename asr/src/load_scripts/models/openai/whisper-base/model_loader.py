import transformers

def load():
    transcriber = transformers.pipeline("automatic-speech-recognition", model="openai/whisper-base")
    return transcriber