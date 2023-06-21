# bluey-llm

Training a (very smol) large language model to write Bluey episodes.

## Scrape

`scrape.py` downloads Episode transcripts from https://blueypedia.fandom.com/

## Clean

`clean.py` processes the downloaded data and writes our training dataset.

## Train

`bluey.txt` is 6.7MB and contains `2305680` tokens

Grab the latest llama.cpp: https://github.com/ggerganov/llama.cpp

See `train.sh` for an example invocation and pay attention to these parameters:

### Context size
```
--predict 128 \
--ctx 128 \
```

### Attention head and embedding sizes 

```
    --embd 256 \
    --head 8 \
    --layer 16 \
```

### Checkpoint and model outputs

```
    --checkpoint-out chk-bluey-256x16-run1.bin \
    --model-out ggml-bluey-256x16-f32-v1.bin \
```

### Training configuration

```
    -t 4 -b 8 -n 32 --seed 1 \
```

Threads (set to number of physical CPU you have), contexts-per-example (batches) and number of examples.

This will consume `ctx*batch*n` tokens (32k with parameters above) from the training set and output a checkpoint snapshot and a GGML model.

## Run Inference 

You can then run inference with this model:

```
./main -m ggml-bluey-256x16-f32-v1.bin -n 128
```

To train with another 32k tokens, repeat with `--checkpoint-in chk-bluey-256x16-run1.bin` 