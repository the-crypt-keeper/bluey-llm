import os
import requests
import tiktoken
import numpy as np

# load the cleaned bluey dataset
input_file_path = os.path.join(os.path.dirname(__file__), 'bluey.txt')
with open(input_file_path, 'r') as f:
    data = f.read()

# 90%/10% split training and validation
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode(train_data, disallowed_special=())
val_ids = enc.encode(val_data, disallowed_special=())
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train has 297,023 tokens
# val has 33,493 tokens