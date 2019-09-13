import os
import sys
#create variable file name using Cmd terminal
folderName = str(sys.argv[1])

#function to create project folder
def makedirectory():
        #creates folder in new location
        os.mkdir(("C:/Users/Ignas/Documents/DjangoProjects/") + folderName)
if __name__ == '__main__':
    makedirectory()