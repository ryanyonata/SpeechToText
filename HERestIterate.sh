#!/bin/bash

HMM0_PATH=$1
FIRST_ITERATION=$2
LAST_ITERATION=$3
CONFIG_PATH=$4
PHONES_PATH=$5
TRAINSCP_PATH=$6
MONOPHONES_PATH=$7

for (( i = $FIRST_ITERATION; i <= $LAST_ITERATION; i++ )); do
    echo "Iteration: $i"
    mkdir hmm$i
    HERest -C $CONFIG_PATH -I $PHONES_PATH -t 250.0 150.0 1000.0 -S $TRAINSCP_PATH -H hmm$((i-1))/macros -H hmm$((i-1))/hmmdefs -M hmm$i $MONOPHONES_PATH
done
