#!/bin/bash

# Author - Jeremy Burks
# Last Revised - 04/21/2022
# Purpose - Copies syslog to a file in the current working directory and time stamps it

# variables 
d=$(date +%m-%d-%Y_%T)
t=$(date +%T)

# Copies syslog into working directory and appends current date and time to file name
echo "Copying syslogs to current directory at $t"
cp /var/log/syslog syslog_$d