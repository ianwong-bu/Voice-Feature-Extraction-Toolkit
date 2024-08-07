# Usage
Mount writable volume to `/output`.

Run container:
```bash
docker run -it <image_id> -v container-output:/output <model_id> <dataset_id> <dataset_config_name> <dataset_split>
```

Example:
```bash
docker run -it <image_id> NbAiLabBeta/nb-whisper-medium-verbatim amaai-lab/DisfluencySpeech default train[:5]
```

The container's output will be JSON files in the output volume