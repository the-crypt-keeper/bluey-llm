# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

init_from = 'scratch'
eval_interval = 100 # keep frequent because we'll overfit
eval_iters = 50
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = True # override via command line if you like
wandb_project = 'bluey-nano'
wandb_run_name = '256x256'

out_dir = wandb_project+'-'+wandb_run_name

dataset = 'bluey'
gradient_accumulation_steps = 1
batch_size = 8
block_size = 256

# baby GPT model :)
n_layer = 8
n_head = 4
n_embd = 256
dropout = 0

learning_rate = 3e-3 # with baby networks can afford to go a bit higher
max_iters = 1000

decay_lr = True
lr_decay_iters = max_iters # make equal to max_iters usually
min_lr = 3e-4 # learning_rate / 10 usually
warmup_iters = 0 # not super necessary potentially

beta2 = 0.98 # make a bit bigger because number of tokens per iter is small

# on macbook also add
device = 'cuda'
compile = False
