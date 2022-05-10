#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/05/2022
# Purpose - Runs a bash commands from inside python3


import subprocess 

# "whoami" was returning a value with a letter 'b' at the beginning of the string. I googled and found on stackoverflow that the b meant python was assuming the value being returned from the command was a byte data type. The solution on stack overflow was to add the .decode() method to the command to tell python that the return value would be in a string format "utf-8" is a character encoding, it's what is telling it that it is not a byte.

username = subprocess.check_output("whoami").strip().decode("utf-8")
ipadd = subprocess.check_output("ip a", shell=True)
hardware = subprocess.check_output("lshw -short", shell=True)


print(username, "is the user on")
print(ipadd, "is the IP info of")
print(hardware, "is the hardware info for")