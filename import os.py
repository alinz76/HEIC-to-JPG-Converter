import os
import datetime

# specify the path to your directory
directory = os.getcwd()

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    # check if the path is a file and does not end with .py
    if os.path.isfile(filepath) and not filename.endswith('.py'):
        # get the time of last modification
        timestamp = os.path.getmtime(filepath)
        # convert the timestamp into a readable format
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        # format the datetime object into the desired string format
        new_filename = dt_object.strftime("%Y-%m-%d_%H-%M-%S") + os.path.splitext(filename)[1]
        new_filepath = os.path.join(directory, new_filename)
        # rename the file
        os.rename(filepath, new_filepath)
