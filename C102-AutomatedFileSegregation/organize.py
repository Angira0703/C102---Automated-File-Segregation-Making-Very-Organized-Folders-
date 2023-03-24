#importing os and shutil

import os
import shutil

#defining the source and destination 

from_dir = "C:/Users/aviji/Downloads"
to_dir = "C:/Users/aviji/OneDrive/Desktop/VERY-ORGANIZED-FOLDER"
list_of_files = os.listdir(from_dir)

#move all image files from downloads to another folder

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == " ":
        continue
    if extension in [".jpg", ".jpeg", ".png", ".gif", ".jfif"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name

        #print("path1", path1)
        #print("path3", path3)
        #print("path2", path2)

# check if folder or directory path exists before moving
# else make a new folder or directory, then move

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")

            # move from path1 --> path3

            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")

            shutil.move(path1, path3)




