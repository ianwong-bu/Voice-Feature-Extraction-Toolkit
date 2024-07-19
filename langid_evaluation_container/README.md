# Usage
1. Mount a writable volume to `/output`
2. Start the container
```bash
docker run <this container's image> (evaluate|report|both) <model_id> <dataset_id> <dataset_config_name> <dataset_split>
```

`dataset_config_name` and `dataset_split` are specific to each dataset.
Look at a dataset's card on HuggingFace for supported values.

A quick example:
```bash
docker run <this container's image> both sanchit-gandhi/whisper-medium-fleurs-lang-id PolyAI/minds14 all 'train[:20]'
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