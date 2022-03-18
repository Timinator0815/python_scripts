################################################
# Renaming files that match a specific pattern #
#                                              #
# Author: Tim                                  #
# Date: 18.03.22                               #
################################################

import sys, glob, os
import pathlib, subprocess

current_path = pathlib.Path(__file__).parent.absolute() #get working path

pattern = '/**/*.cbz' #pattern the files have to match (/**/ needed for recursive search)

files = glob.glob(str(current_path) + pattern,recursive=True) #get all files in current and subfolders


for file in files:
#loop through all found files

    path = os.path.dirname(file) #base path of the file
    filename = os.path.basename(file) #base name of the file

    if filename.split("v"):

        check_v = filename.split("v")
        bool_rename = False

        #check if the filename contains a version index v
        for x in check_v:
            try:
                int(x[0])
                bool_rename = True
            except:
                print("file " + file + " not in suitable format")

        if bool_rename == True:
            #cut every char after (Digital) off filename
            filename = filename.split("(Digital)")
            filename = filename[0] + "(Digital).cbz" 

            filename_lenght = len(filename) #lenght of the filename
            split = filename_lenght-17 #splitpoint to cut out the v of v01,v02...
            new_filename = filename[0:split] + filename[split+1:filename_lenght] #construct new filename
            new_file = path + "/" + new_filename #full path of new named file
            command = "mv \"" + file + "\" \"" + new_file + "\""#shell command
            
            print("renaming " + filename + " to " + new_filename)

            subprocess.run([command],check=True,capture_output=True,shell=True) #run command
