import os
import sys
#create variable file name using Cmd terminal
folderName = str(sys.argv[1])
#path to the location where project file will be created
path = (r'C:\\Users\Ignas\Documents\\')
#function to create project folder
def makedirectory():
        #redirects to your desired location to create project folder
        os.chdir(path) 
        #creates folder in new location
        os.mkdir(path + folderName)
if __name__ == '__main__':
    makedirectory()