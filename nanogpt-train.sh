#!/bin/bash

git submodule init
ln -sf `pwd` nanoGPT/data/bluey

cd nanoGPT
python3 train.py ../nanogpt-config.py $*
cd -