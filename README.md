# bluey-llm

Training a (very smol) large language model to write Bluey episodes.

Objectives:

* Demonstrate how to scrape and clean a simple data-set from scratch
* Experiment with model sizes and training parameters
* Have fun!

## Scrape and clean

`scrape.py` downloads Episode transcripts from https://blueypedia.fandom.com/

`clean.py` processes the downloaded data and writes our training dataset, `bluey.txt` now contains `330516` tokens

## nanoGPT

Make sure you have the nanoGPT submodule `git submodule init`

Create `train.bin` and `val.bin` with `nanogpt-prepare.py`

Modify `nanogpt-bluey.py` as needed, specifically set `device = 'cpu'` if you do not have a GPU available.

Execute `nanogpt-train.sh` to create the model, it will be written to `nanoGPT/bluey-nano-192x256-v2`

### Run Inference 

Execute `nanogpt-generate.sh` to generate 10 random completions

## GGML

Grab the latest llama.cpp: https://github.com/ggerganov/llama.cpp

See `ggml-train.sh` for an example invocation and pay attention to these parameters:

Context size: `--predict 128 --ctx 128`

Attention head and embedding sizes: `--embd 192 --head 1 --layer 8`

Checkpoint and model outputs:

```
    --checkpoint-out chk-bluey-256x16-run1.bin \
    --model-out ggml-bluey-256x16-f32-v1.bin \
```

Batch configuration: `-t 4 -b 8 -n 32 --seed 1`

Threads (set to number of physical CPU you have), contexts-per-example (batches) and number of examples.

This will consume `ctx*batch*n` tokens (32k with parameters above) from the training set and output a checkpoint snapshot and a GGML model.

### Run Inference 

You can then run inference with this model:

```
./main -m ggml-bluey-256x16-f32-v1.bin -n 128
```