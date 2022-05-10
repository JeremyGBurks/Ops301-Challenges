#!/usr/bin/env python3

import subprocess

username = subprocess.check_output("whoami").strip().decode("utf-8")
print(username)