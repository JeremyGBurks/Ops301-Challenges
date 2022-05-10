#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/05/2022
# Purpose - Runs a bash commands from inside python3

import os

print()
print("Here is your system specs: ")
print()
computerinfo = os.system("lshw -short")
print()
print("Here is your Network info: ")
print()
ipinfo = os.system("ip a")
print()
print("Who is running this script: ")
print()
userinfo = os.system("whoami")