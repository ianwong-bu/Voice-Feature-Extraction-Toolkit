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
docker run -it -v output:/output <this container's image> both sanchit-gandhi/whisper-medium-fleurs-lang-id PolyAI/minds14 all 'train[:5]'
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

# Global IDs
The mapping scripts use "global ids" for each language since `datasets` work better with numerical ids
rather than text ids.
Global ids are based on iso639 part 3 language codes.
The codes are created by treating the code as a 3-digit base-26 number, with a = 0 and z = 25.
So a language code of `yue` has a global id 25 * 26^2 + 20 * 26 + 4