#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot to type an IP Address"
echo "Syntax: ./ping.sh 192.168.43"

else
for q in `seq 1 254` ; do for p in `seq 1 254` ; do ping -c 1 $1.$q.$p | grep -i "64 bytes"  & done done
fi
