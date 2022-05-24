#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/23/2022
# Purpose - File manipulation with python

import os

# this function takes three strings as arguements, creates a .txt file and writes each of the strings to a separate line
def write_lines(line1, line2, line3):
    with open("test.txt","w") as outfile:
        outfile.write(line1+"\n"+line2+"\n"+line3)

# this function prints the first line of the .txt file to the screen
def print_first_line(inputfile): 
    with open(inputfile,"r") as readfile:
        line1 = readfile.readline()
        print(line1)

# this function utilizes the os module to remove the file.
def remove_file(inputfile):
    os.remove(inputfile)

# this function takes in user input and assigns it to varibles then uses the write_lines function to create the text file and write the user input into 3 different lines in the created file. 
def user_input():
    name = input("What is your name? ")
    color = input("Favorite color: ")
    pineapple = input("Pineapple on pizza.. yes or no: ")
    write_lines(name,color,pineapple)

# declaration of functions 
user_input()
print_first_line("test.txt")
remove_file("test.txt")
