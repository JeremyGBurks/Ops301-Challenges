#!/bin/bash 

# Author - Jeremy Burks
# Last Revised - 04/25/2022
# Purpose - Prompts user for input directory path, Prompts user for input permissions number
# Navigates to the directory input by the user and changes all files inside it to the input setting
# Prints to the screen the directory contents and the new permissions settings of everything in the directory

# 7 = rwx
# 6 = rw
# 5 = rx
# 4 = r 

read -p "Which directory path would you like to modify permissions for? " user_path
read -p "Please enter permissions number: " user_permission
cd $user_path 
chmod -R $user_permission $user_path
ls -l $user_path
