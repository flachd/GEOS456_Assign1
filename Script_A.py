# -*- coding: cp1252 -*-
'''
GEOS 456 Assignment 1: Python Fundamentals
Author: Darren Flach
Date Created: May 26th, 2018

Script Purpose:
The purpose of this assignment is to write a program using high-level programming (HLP) language.
You will use various Python commands for file and directory management, which are important
components of managing geographic information system (GIS) data and information.

Create Directories of Folders
Write a script to create one or more directories based on names that the user will be asked to enter.
Assume that this script will be executed in IDLE and the directories will be created in the
following location: D:\GEOS455\Assign1. To create the directories, use the mkdir Python command.

Oh and now I am testing this code in GitHub

The logical flow for the script is outlined below:
1.
Ask the user to name the main project folder created in the location
mentioned above.

2.
Ask the user if they want to create the standard 3 sub folders:
one for data storage, one for .mxd storage and one for data output storage.
If yes, create a data folder named “Data”, and mxd folder named “Maps”
and an output folder named “Results”.

3.
Ask the user whether they would like to add another sub folder:
    a. If the response is negative tell the user the program is ending and quit the execution of the script.
    b. If the response is positive ask the user to name the new folder they wish to create:
        i Create the folder with the name entered by the user and inform the user that the folder was successfully created.
        ii Re-ask if they would like to create another custom folder.
    c. If the response is anything other than “Yes” or “No”, repeat the question until the user has entered either “Yes” or “No”.

4.
Before exiting the script, the program must inform the user that the folders
have been successfully created.

'''

#This installs the os module into the script
import os

# 1.
# Ask the user to name the main project foldder created in the location mentioned above.
# This produces a prompt for the user to add input
# The users input is stored in the 'proj_fold' variable
proj_fold = raw_input("Please name the main project folder: ")


# The folder is changed to the folder where the 'proj_fold' variable will be named to.
os.chdir("D:/GEOS456/Assign1")

# And the folder name the user entered is added as a folder name
os.mkdir(proj_fold)

# And the directory is changed to the new folder
os.chdir(proj_fold)

# A display of this folder is printed to screen
PathName = os.getcwd()
print " "
print "Your folder name and path: {}".format(PathName)


# 2.
# Ask the user if they want to create the standard 3 sub folders: One for data storage, one for .mxd storage and one for data output storage.
# If yes, create a data folder named "Data", and mxd folder named "Maps" and an output folder named "Results".
# Found this on wiki.python.org/moin/WhileLoop:
# This compacts the whole thing into a piece of code managed entirely by the while loop.
# Having True as a condition ensures that the code runs until it's broken by n equaling 'Yes' or 'No'.
print " "
print"Do you want to create Project subfolders - Data, Maps, Results?"
while True:
    n = raw_input("Please Enter 'Yes' or 'No': ")
    if n == 'Yes' or n == 'No':
        break

#If the answer is yes, three subdirectories are created under the newly named project directory
if n == 'Yes':
    print " "
    os.mkdir("Data")
    os.mkdir("Maps")
    os.mkdir("Results")

#Got this from effbot.org! http://effbot.org/librarybook/os.htm.
#It lists the contents of a directory
    print "Here is a list of your newly created subdirectories: "
    for file in os.listdir(PathName):
        print file

#This asks the user if they want to make another directory
print " "
print "Do you want to make another folder? "

#What the user enters will go through an error checking while loop and will keep looping until the user enters Yes or No specifically
while True:
    n = raw_input("Please Enter 'Yes' or 'No': ")
#If No is entered, the loop is broken and the next line of code outside the loop is executed.
    if n == 'No':
        break

#If the answer is yes,
#   Sets directory path to new project folder
#   Prompts user to name the new folder
#   Prints the folder that has been created.
#   User is asked if they want to make another folder.
    if n == 'Yes':
        print " "
        print " "
        sub_fold = raw_input("Please name the subfolder you would like to create: ")
        os.mkdir(sub_fold)
        print " "
        print "{} Has been created".format(sub_fold)+ (" in your folder path: {}").format(PathName)
        print " "
        print "Do you want to make another folder?"

# Once the user enters No, the program halts and displays the following message
print " "
print"Thank you ... program has now ended"




