# !/bin/bash

# Script:                       Ops 301 Challenge 05
# Author:                       Jeremy Burks
# Date of latest revision:      05/02/22
# Purpose:                      Display & clear syslog/wtmp/auth logs. Menu system for user to select different options  

# Variables--for text color 
RED='\033[0;31m'
NC='\033[0m' 

# While loop that keeps the user in the menu until they enter "0"
while [[ $user_in != "0" ]]
do
    echo -e "${RED}*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*${NC}"
    echo -e "${RED}ATTENTION!!YOU MUST BE ROOT/SUPERUSER TO CLEAR LOGS${NC}"
    echo -e "${RED}*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*${NC}"
    echo "Press 1 to view and clear the syslog"
    echo "Press 2 to view the cleared syslog"
    echo "Press 3 to view and clear the wtmp log"
    echo "Press 4 to view cleared wtmp log"
    echo "Press 5 to view auth.log"
    echo "Press 6 to clear auth.log"
    echo "Press 0 to exit the menu"
    read user_in

    if [ $user_in == "1" ]; then
    echo "syslog contents: "
    cat /var/log/syslog
    echo "Clearing syslog..."
    cat /dev/null > /var/log/syslog 
    fi
    if [ $user_in == "2" ]; then
    echo "syslog contents: "
    cat /var/log/syslog
    fi
    if [ $user_in == "3" ]; then
    echo "wtmp contents: "
    cat /var/log/wtmp
    echo "clearing wtmp contents..."
    cat /dev/null > /var/log/wtmp
    fi
    if [ $user_in == "4" ]; then
    echo "wtmp contents: "
    cat /var/log/wtmp
    fi
    if [ $user_in == "5" ]; then
    echo "auth.log contents: "
    cat /var/log/auth.log
    fi
    if [ $user_in == "6" ]; then
    echo "Clearing auth.log..."
    cat /dev/null > /var/log/auth.log
    fi
    if [ $user_in == "0" ]; then
    echo "Exiting the menu"
    fi
done

# syslog track data about status, events, diagnostics within the system. It is an important logging sytem that can help identify events and their severity.
# wtmp keeps a record of all logins and logouts. This log is important for analysis if there is suspicious activity in the system.
# auth.log keeps a record of all authentications information, including user logins and authentication machinsm that were used. The importance of this log implied within its contents.