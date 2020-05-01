#!/bin/bash

# number of images to add to training file
num=5000

# if argument is given then use that as the number of images to use
if [ $# = 1 ]
then 
    num=$1
fi

# see if data/images exists
if [ ! -d data/images/ ]
then
    # if not download images
    mkdir data/images
    cd data
    echo 'downloading images'
    svn checkout https://github.com/lbaitemple/race-car/trunk/data/images > /dev/null 2>&1
    cd ..
fi


# see if data/list exists
if [ -d data/list/ ]
then
    # if it does then does the csv file exist?
    if [ -e data/list/train_1.csv ]
    then
        # if yes, remove csv
        rm data/list/train_1.csv
    fi
# if not make directory
else
    mkdir data/list
fi

# add the word 'image' to top of file
echo image >> data/list/train_1.csv

# add $num number of random images to the file
find data -name '*.jpg' | shuf -n $num >> data/list/train_1.csv