#!/bin/bash



service NetworkManager stop
ifconfig wlan0 down
macchanger -e wlan0
ifconfig wlan0 up
service NetworkManager start
