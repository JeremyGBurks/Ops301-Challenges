#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/23/2022
# Purpose - a Python script that fetches cpu information using Psutil

import psutil

print(psutil.cpu_times(), file=open("output.txt", "a"))