#!/bin/bash

arm_means=(0.5 0.9)
arm_nums=(100 200 300 400 500)

for mean in "${arm_means[@]}"
do
    for num in "${arm_nums[@]}"
    do
        mean_str="${mean/./\.}"
        filename="setups/N100_${mean/./}X${num}.json"
        sed "s/\[${mean_str}\], \"repeat\": \[1\]/[${mean}], \"repeat\":[${num}]/g" setups/default.json > ${filename}

        python3 main.py --setup=${filename} --policy=UCB
    done
done
