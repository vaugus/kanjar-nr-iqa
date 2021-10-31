#!/bin/bash

cmd="python fssf.py "
path="/home/victor/Documents/msc-image-database/KADID/kadid10k/images/"
mask_path="mask_kadid.png"
param=1000

# $cmd $path $mask_path 100 $(./command_gen 1 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 2 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 3 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 4 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 5 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 6 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 7 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 8 81 9) &
# $cmd $path $mask_path 100 $(./command_gen 9 81 9) &

# wait

$cmd $path $mask_path $param $(./command_gen 1 81 9) &
$cmd $path $mask_path $param $(./command_gen 2 81 9) &
$cmd $path $mask_path $param $(./command_gen 3 81 9) &
$cmd $path $mask_path $param $(./command_gen 4 81 9) &
$cmd $path $mask_path $param $(./command_gen 5 81 9) &
$cmd $path $mask_path $param $(./command_gen 6 81 9) &
$cmd $path $mask_path $param $(./command_gen 7 81 9) &
$cmd $path $mask_path $param $(./command_gen 8 81 9) &
$cmd $path $mask_path $param $(./command_gen 9 81 9) &

wait
