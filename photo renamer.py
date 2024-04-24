# Rename Images with Date Photo Taken

# Purpose: Renames image files in a folder based on date photo taken from EXIF metadata

# Author: Matthew Renze

# Usage: python.exe rename.py input-folder
#   - input-folder = (optional) the directory containing the image files to be renamed

# Examples: python.exe rename.py C:\Photos
#           python.exe rename.py

# Behavior:
#  - Given a photo named "Photo Apr 01, 5 54 17 PM.jpg"  
#  - with EXIF date taken of "4/1/2018 5:54:17 PM"  
#  - when you run this script on its parent folder
#  - then it will be renamed "20180401-175417.jpg"

# Notes:
#   - For safety, please make a backup of your photos before running this script
#   - Currently only designed to work with .jpg, .jpeg, and .png files
#   - If you omit the input folder, then the current working directory will be used instead.

# Import libraries
import os
import sys
from datetime import datetime
import pathlib

# Set list of valid file extensions
valid_extensions = [".jpg", ".jpeg", ".png", ".heic", ".mp4", ".mov"]
photos = [".jpg", ".jpeg", ".png", ".heic"]
videos = [".mp4", ".mov"]
# If folder path argument exists then use it
# Else use the current running folder
folder_path = r"c:\Users\aline\OneDrive\Desktop\New folder"

# Loop through each file
for path in os.listdir(folder_path):
    file_extension = os.path.splitext(path)[1]
    ctime = os.path.getctime(path)
    if file_extension in valid_extensions:
        continue
    date_created = datetime.fromtimestamp(ctime).strftime("%Y%m%d-%H%M%S")
    if file_extension in photos:
        new_file_name = "IMG_" + date_created + file_extension
        # os.rename(path, new_file_name)
    if file_extension in videos:
        new_file_name = "VID_" + date_created + file_extension
    # Rename the image
        # os.rename(path, new_file_name)

    print(new_file_name)