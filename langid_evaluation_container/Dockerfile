FROM python:3.10.12-slim-bullseye

WORKDIR /app/

COPY src/. /app/

# TODO: Verify cache directory
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt --mount=type=cache,target=/root/.cache pip install -r /tmp/requirements.txt

# Could replace with Bash brace expansion
RUN for script in mapping_scripts/datasets/*/*/make_id_mappings.py; do python3 "$script"; done
RUN for script in mapping_scripts/models/*/*/make_id_mappings.py; do python3 "$script"; done

ENTRYPOINT ["/app/run.sh"]