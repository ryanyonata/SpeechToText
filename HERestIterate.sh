#!/bin/bash

HMM0_PATH=$1
NUM_OF_ITERATIONS=$2
CONFIG_PATH=$3
PHONES0_PATH=$4
TRAINSCP_PATH=$5
MONOPHONES0_PATH=$6

for (( i = 1; i <= $NUM_OF_ITERATIONS; i++ )); do
    echo "Iteration: $i"
    mkdir hmm$i
    HERest -C $CONFIG_PATH -I $PHONES0_PATH -t 250.0 150.0 1000.0 -S $TRAINSCP_PATH -H hmm$((i-1))/macros -H hmm$((i-1))/hmmdefs -M hmm$i $MONOPHONES0_PATH
done
