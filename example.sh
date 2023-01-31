#!/bin/bash

setupnames=(
    "N100_05X100"
    "N100_05X200"
    "N100_05X300"
    "N100_05X400"
    "N100_05X500"

)

for i in "${setupnames[@]}"
do
    python3 main.py --setup=setups/${i}.json --policy=UCB
done
