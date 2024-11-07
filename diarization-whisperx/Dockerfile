FROM python:3.10.12-slim-bullseye

RUN python3 -m pip --no-cache install git+https://github.com/m-bain/whisperx.git \
    && apt update \
    && apt install -y ffmpeg \
    && apt clean

VOLUME /data

ENTRYPOINT /usr/local/bin/whisperx
CMD ["--help"]
