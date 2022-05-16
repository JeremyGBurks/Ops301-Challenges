#!/usr/bin/env python3

# Author - Jeremy Burks
# Last Revised - 5/15/2022
# Purpose - manipulating a list with python

# #Assign to a variable a list of ten string elements.
veggie=["kiwi","orange","celery","spinach","apple","banana","tomato","squash","cherry","radish"]

# Print the fourth element of the list.
def fourth_element(lst):
    print("The fourth element in the list is " + lst[3])

# Print the sixth through tenth element of the list.
def sixth_tenth(lst):
    print("6th through tenth elements in the list: ")
    for i in range(5,10):
        print(lst[i])

# Change the value of the seventh element to “onion”.
def onion(lst):
    print("Replacing " + lst[6] + " with onion: ")
    lst[6]="onion"
    print(lst)

# append()
def add_value(lst,str):
    lst.append(str)
    print("Adding "+ str + " to the list")
    print(lst)

# clear()
def clear_list(lst):
    print("Clearing the list")
    lst.clear()
    print(lst)

# copy()
def copy_list(lst):
    print("Creating an exact copy of the list")
    lst2=lst.copy()
    print(lst2)

# count()
def count_list(lst,str):
    print("Counting how many times "+ str +" is in the list")
    print(lst.count(str))

# extend()
def extend_list(lst):
    meats=["chiken","beef"]
    print("Adding elements to the list")
    lst.extend(meats)
    print(lst)

# index()
def index_list(lst,str):
    print("Printing which index "+ str +" is at in the list")
    print(lst.index(str))

# insert()
def insert_list(lst,str,int):
    print("Adding "+ str +" to the list at specified index")
    lst.insert(int,str)
    print(lst)

# pop()
def pop_list(lst):
    popped=lst.pop()
    print(popped +" just was removed from our list")
    print(lst)

# remove()
def remove_list(lst,str):
    print("Removes "+ str +" from the list")
    lst.remove(str)
    print(lst)

# reverse()
def reverse_list(lst):
    print("Reversing the list")
    lst.reverse()
    print(lst)

# sort()
def sort_list(lst):
    print("Sorting the list alphebetically!")
    lst.sort()
    print(lst)

fourth_element(veggie)
print()
sixth_tenth(veggie)
print()
onion(veggie)
print()
add_value(veggie,"pickle")
print()
copy_list(veggie)
print()
count_list(veggie, "kiwi")
print()
extend_list(veggie)
print()
index_list(veggie,"celery")
print()
insert_list(veggie, "grape", 4)
print()
pop_list(veggie)
print()
remove_list(veggie, "banana")
print()
reverse_list(veggie)
print()
sort_list(veggie)
print()
clear_list(veggie)
print()
