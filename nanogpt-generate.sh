#!/bin/bash
cd nanoGPT
python3 sample.py --out_dir='bluey-nano-192x256-v2' --max_new_tokens=128 --top_k=40 --start="Scene:" $*
cd -