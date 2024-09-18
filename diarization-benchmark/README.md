Docker container for https://github.com/Picovoice/speaker-diarization-benchmark

Currently, no new models or datasets have been added. All benchmarks are from upstream.

Uses the [Voxconverse](https://github.com/joonson/voxconverse) dataset

# Usage
```bash
python3 benchmark.py \
--type (ACCURACY | CPU | MEMORY) \
--dataset VoxConverse \
--data-folder (/data/voxconverse/wav/dev | /data/voxconverse/wav/test) \
--label-folder /data/voxconverse/labels/ \
--engine <engine> \
<arguments depending on engine>
```

For the additional arguments required for each engine, see the [upstream documentation](https://github.com/Picovoice/speaker-diarization-benchmark?tab=readme-ov-file#data)

## Example
An example using pyannote is given because Pyannote is free

To use Pyannote, you must first accept the conditions at its [Huggingface page](https://huggingface.co/pyannote/speaker-diarization), then create a Huggingface token.

```bash
python3 benchmark.py \
--dataset VoxConverse \
--data-folder /data/voxconverse/wav/test \
--label-folder /data/voxconverse/labels/ \
--engine PYANNOTE \
--pyannote-auth-token <HUGGINGFACE_TOKEN>
```
