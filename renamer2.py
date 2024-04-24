
import os
from datetime import datetime
import time


# Set list of valid file extensions
photos = [".jpg", ".jpeg", ".png", ".heic"]
videos = [".mp4", ".mov"]
# If folder filename argument exists then use it
# Else use the current running folder
directory = r'C:\Users\aline\OneDrive\Desktop\New'

# Loop through each file
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath) and not filename.endswith(".py"):
        file_extension = os.path.splitext(filename)[1]
        file_extension.lower()
        timestamp = os.path.getmtime(filepath)
        date_created = datetime.fromtimestamp(timestamp).strftime("%Y%m%d-%H%M%S")
        if file_extension in photos:
            new_file_name = "IMG_" + date_created + file_extension
            new_filepath = os.path.join(directory, new_file_name)
            os.rename(filepath, new_filepath)
            

        if file_extension in videos:
            new_file_name = "VID_" + date_created + file_extension
            new_filepath = os.path.join(directory, new_file_name)
            os.rename(filepath, new_filepath)
            