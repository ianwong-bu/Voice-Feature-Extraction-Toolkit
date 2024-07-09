# Usage
1. Mount a writable volume to `/output`
2. Start the container
```bash
docker run <this container's image> <model_id> <dataset_id> (evaluate|report|both)
```

The model and dataset must have mapping scripts defined in `src/mapping_scripts`.
Mapping scripts enable translation between model- and dataset-specific ids,
allowing models to be evaluated on datasets that the models were not originally trained on.

3. View prediction output and/or generated report in the volume mounted to `/output`

# Supported models and datasets
## Models
- facebook/mms-lid-4017
- sanchit-gandhi/whisper-medium-fleurs

## Datasets
- PolyAI/minds14