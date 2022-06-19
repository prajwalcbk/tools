#!/bin/bash

for i in `seq 1 254`; do ping -c 1 192.168.43.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & done

