import transformers

def load():
    transcriber = transformers.pipeline("automatic-speech-recognition", model="NbAiLabBeta/nb-whisper-medium-verbatim", trust_remote_code=True)

    def transcribe_function(audio):
        return transcriber(audio, generate_kwargs={'task': 'transcribe', 'language': 'en'})
    
    return transcribe_function