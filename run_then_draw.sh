#!/bin/bash

policy=$1
setupnames=(
    "N100_05X100"
    "N100_05X200"
    "N100_05X300"
    "N100_05X400"
    "N100_05X500"
)

for i in "${setupnames[@]}"
do
    python3 main.py --setup=setups/${i}.json --policy=${policy} \
    > log/${i}_${policy}.log 2>&1 &
    # You should make 'log' directory first
done

# Wait for all background jobs
for job in `jobs -p`
do
    wait $job
done

# After all jobs are done, draw fig using the results.
python3 draw_fig.py

