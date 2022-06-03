#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 6/02/2022
# Purpose - accepts user input and utilizes request library to apply HTTP methods to a URL

import requests
import sys

website = input("Please enter a URL: ")

def user_menu(url):
    try:
        method_menu = """
        **********************************
        **                              **
        *     Select an HTTP method      *
        *    1. GET                      *
        *    2. POST                     *
        *    3. PUT                      *
        *    4. DELETE                   *
        *    5. PATCH                    *
        *    6. OPTION                   *
        *    7. HEAD                     *
        *    8. Quit                     *
        **                              **
        **********************************
        """
        user_method = input(method_menu)
        url = "http://"+url
        print("You have chosen the " +user_method+ " for the URL: " +url)
        choice = input("Would you like to proceed? y/n: ")
        if choice.lower() == "y":
            if user_method == "1":
                response = requests.get(url)
            elif user_method == "2":
                response = requests.post(url)
            elif user_method == "3":
                response = requests.put(url)
            elif user_method == "4":
                response = requests.delete(url)
            elif user_method == "5":
                response = requests.patch(url)
            elif user_method == "6":
                response = requests.option(url)
            elif user_method == "7":
                response = requests.head(url)
            elif user_method == "8":
                sys.exit(0)
            else: 
                print("Please enter a number 1-8")
                user_menu()
        return response
    except KeyboardInterrupt:
        print ("Quitting")
        sys.exit(0)

response = user_menu(website)

if response:
    print("Success")
else:
    print("Error")

# https://www.javatpoint.com/python-sys-module
