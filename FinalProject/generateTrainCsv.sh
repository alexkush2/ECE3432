#!/bin/bash

rm data/list/train_1.csv
echo image >> data/list/train_1.csv

find data -name '*.jpg' | shuf -n 5000 >> data/list/train_1.csv