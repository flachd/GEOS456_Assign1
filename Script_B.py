'''
GEOS 455 Basics of Python Assignment 2
Author: Darren Flach
Assignment
Date Created: June 13, 2017
Script Purpose:
The script you will write for Part B will create copies of the files created in Part A.
The reasoning behind this portion is to create an archive replica of the folders created above for use.
It is assumed that this script will be executed in IDLE and the directories will be created in the following location: D:\GEOS455\A2.
To create the directories use the ‘copyfile’ python command in the shutils module.
To walk through a file tree structure use the ‘walk’ python command in the os module. To deal with paths use the os.path functions.
1. Ask the user for the path of the project folder with subfolders you are interested in creating an archive of.
Create a new main folder called “Archive”.
2. Copy all folders created in Part A into the newly created “Archive” folder and append “_archive” to all folders and sub folder names.
3. Inform user that all folders have been successfully copied to the “Archive” folder.
'''


#This installs the os and shutil modules into the script. Which are necessary for some of the functions
import os, shutil

# 1. Ask the user to name the main project folder created in the location mentioned above.
proj_fold = raw_input("Please name the main project folder: ");

# This produces a prompt for the user to add input
# The user's input is stored in the 'proj_fold' variable
# The folder is changed to the folder where the 'proj_fold' variable will be named to.
os.chdir(r"D:/GEOS455/Assign2")

#os.getcwd() retrieves the current working directory. It is put into PathName variable 
PathName = os.getcwd()

#This variable is printed to show the user which directory is currently the root directory
print " "
print "Your folder name and path: {}".format(PathName)+ os.sep + proj_fold
print "\n"

#This creates two variables. path1 and path2. path1 is the project folder that the user wants to archive
#path2 is the path and foldername of the new archive folder before adding _archive
path1=("D:" + os.sep + "GEOS455" + os.sep + "Assign2" + os.sep + proj_fold)
path2=("D:" + os.sep + "GEOS455" + os.sep + "Assign2" + os.sep + "Archive" + os.sep + proj_fold)


#This copies the project folder that the user entered (stored in proj_folder variable) into a newly created Archive folder.
shutil.copytree(path1,path2)


#This changes the working directory to the Archive folder
os.chdir(r"D:\GEOS455\Assign2\Archive")

# This function 'walks' through the entire directory structure and for every directory it comes across, it appends a _archive to it
# Reference: https://www.tutorialspoint.com/python/os_walk.htm" & https://www.tutorialspoint.com/python/os_rename.htm
for root, dirs, files in os.walk("D:\GEOS455\Assign2\Archive",topdown=False):
    
    for name in dirs:
        newname=(name + "_archive")
        os.rename(os.path.join(root, name),os.path.join(root, newname))
        
#This displays the newly created archive folders to confirm to the user that the directories have been created        
print "Here is a list of your newly created Archive folders:\n "
for root, dirs, files in os.walk("D:\GEOS455\Assign2\Archive",topdown=True):
    for name in dirs:
        print(os.path.join(root, name))

#This prints out confirmation that the directories were created succesfully    
print "\nAll folders have been successfully copied to ""Archive"" folder. \nProgram has completed"

