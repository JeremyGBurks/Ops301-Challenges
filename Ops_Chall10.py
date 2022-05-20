#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/19/2022
# Purpose - Conditionals in python

# Conditional to evaluate if two integers are equal
def equals(a,b):
    if a == b:
        print("It's equal!!")

# Conditional to evaluate if two integers are not equal
def not_equals(a,b):
    if a != b:
        print("It's not equal!!")

# Conditional to evaluate if "a" is less then "b" added an else statement to handle both outcomes
def less_than(a,b):
    if a < b:
        print(str(a) + " is less than " + str(b))
    else:
        print(str(a) + " is less than " + str(b))

# Conditional to evaluate if "a" is less than or equal to "b"
def less_than_or_equal(a,b):
    if a <= b:
        print(str(a) + " is less than or equal to " + str(b))

# Conditional to evaluate if "a" is greater than "b"
def greater_than(a,b):
    if a > b:
        print(str(a) + " is greater than " + str(b))

# Conditional to evaluate if an interger is greater than or equal to another
def greater_than_or_equal(a,b):
    if a >= b:
        print(str(a) + " is greater than or equal to " + str(b))

# Conditional to evaluate if "a" is greater than "b" with an elif to evaluate the opposite
def this_that_or_elif(a,b):
    if a > b:
        print(str(a) + " is greater than " + str(b))
    elif b > a:
        print(str(b) + " is greater than " + str(a))

# Conditional to evaluate if "a" is less than "b" with an elif and else statement to catch other outcomes
def this_else_elif(a,b):
    if a < b:
        print(str(a) + " is less than " + str(b))
    elif a > b:
        print(str(a) + " is greater than " + str(b))
    else:
        print(str(a) + " is equal to " + str(b))

# STRETCH GOALS:
def this_and_that(a,b,c):
    if (a > b) and (c != b):
        print("Weird conditionals are met!")

def this_or_that(a,b,c):
    if (a < b) or (c == a):
        print("More weird conditionals have been met!")

def if_then_if(a,b,c):
    if (a == b):
        if (b > c):
            print("You've been nested")

def if_else_pass(a):
    if isinstance(a,int):
        print("It's a number!")
    else:
        pass

# this function takes user input and evaluates it, it has error handling so that if a string is entered the user is prompted again.
# The try block lets me test a code block for errors. The except block lets me handle the errors.
def less_than_input():
    try:
        first_num = int(input("Pick your first number: "))
        second_num = int(input("Pick your second number: "))
        less_than(first_num, second_num)
    except:
        ValueError
        print("Please enter a number not a string!")
        less_than_input()


# Declaration of functions
equals("ball", "ball")
not_equals("3", "5")
less_than_or_equal(5, 9)
greater_than(9, 2)
greater_than_or_equal(1452, 3)
this_that_or_elif(558, 4)
this_else_elif(57, 3389)
this_and_that(52, 3, 900)
this_or_that(5, 87, 5)
if_then_if(89, 89, 2)
if_else_pass("potato")
less_than_input()
