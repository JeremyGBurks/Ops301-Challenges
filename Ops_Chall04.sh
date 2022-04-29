# !/bin/bash

# Script:                       Ops 301 Challenge 04
# Author:                       Jeremy Burks
# Date of latest revision:      04/27/22
# Purpose:                      Menu that accepts user input, uses conditionals to evaluate and execute commands.


while true; do
    echo "________________________________________________"
    echo "|                                              |"
    echo "|*~*~*~*Welcome to the conditionals Menu~*~*~*~|"
    echo "|                                              |"
    echo "| Please select an option from the menu below  |"
    echo "| 1. Print a familiar test message             |"
    echo "| 2. Ping myself?                              |"
    echo "| 3. What is my IP info?                       |"
    echo "| 4. Exit                                      |"
    echo "|                                              |"
    echo "________________________________________________"
    
    read user_in
    if [[ $user_in == "1" ]]; then
    echo "*~*~*~*Hello, World!*~*~*~*~"
    fi
    if [[ $user_in == "2" ]]; then
    echo "*~*~*~*PING!*~*~*~*"
    ping -c 5 127.0.0.1
    fi
    if [[ $user_in == "3" ]]; then
    echo "I found my IP info!"
    ip a 
    fi
    if [[ $user_in == "4" ]]; then
    echo "Leaving so soon?"
    exit 0
    fi   
done
