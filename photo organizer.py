import glob
import os
from shutil import move
import pathlib

#path
path = r'c:\Users\aline\OneDrive\Desktop\New\New'
os.chdir(path)

myphotos = [] #list

for name in os.listdir(path):
    if name.startswith('IMG_'):
        myphotos.append(name)
        

for file in myphotos:
    #print (file.split('PXL_')[1].split('_')[0])
    myyear = file.split('IMG_')[1].split('_')[0][:4]
    mymonth = file.split('IMG_')[1].split('_')[0][:6][-2:]
    myfolder = r'{}-{}'.format(myyear, mymonth)
    #print(myfolder)
    #create folder if does not exist
    if not os.path.exists(myfolder):
        os.makedirs(myfolder)
    #move files
    dst = myfolder
    move(file, os.path.join(dst, file))
    
