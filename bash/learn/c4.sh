#!/bin/bash

p=(1 2 3 4 5)

echo "${p[0]}"
echo ${p[2]}
echo ${p[@]}

for (( i=0 ; i<=4; i++))
do
 echo ${p[i]}
done
