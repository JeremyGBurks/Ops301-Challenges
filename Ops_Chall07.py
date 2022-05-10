#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/09/2022
# Purpose - Intake a filepath from a user and print out the contents and save the contents into a txt file

# Import libraries
import os

# User input for filepath 
file_path=input("Please enter a filepath to print out: ")

# Creation of function
def print_path(brody):
    #create a file called "testfile.txt" and gives it write access
    with open("./testfile.txt", "w") as outfile:
        for (root, dirs, files) in os.walk(brody):
            print("Root directory: ")
            print(root)
            outfile.write(root)
            print("Directories: ")
            # dirs returns a list. Loop through list and print out the value at each index into the file we created
            for idx in dirs:
                print(idx)
                outfile.write(idx)
                outfile.write("\n")
            print("Files within the directory: ")
            for fls in files:
                print(fls)
                outfile.write(fls)
                outfile.write("\n")
print_path(file_path)

# End

# /home/irondruid/Ops201-Lab-02/Ops301-Challenges-/pythontest