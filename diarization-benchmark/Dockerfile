FROM python:3.10.12-slim-bullseye

WORKDIR /app/

RUN git clone --depth=1 https://github.com/Picovoice/speaker-diarization-benchmark.git /app/

# TODO: Verify cache directory
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt --mount=type=cache,target=/root/.cache pip install -r /tmp/requirements.txt

ENTRYPOINT ["/app/benchmark.py"]