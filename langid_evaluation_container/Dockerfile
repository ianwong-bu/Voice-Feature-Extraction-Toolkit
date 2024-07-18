FROM python:3.10.12-slim-bullseye

WORKDIR /app/

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt pip install --no-cache-dir -r /tmp/requirements.txt

COPY src/. /app/

RUN for script in mapping_scripts/{datasets,models}/*/*/make_id_mappings.py; do python3 "$script"; done

ENTRYPOINT ["/app/run.sh"]