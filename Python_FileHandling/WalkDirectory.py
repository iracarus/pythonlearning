import os

for folderName, subFolders, fileNames in os.walk('/Users/Kingslayer/Downloads'):
    print('The folder is : ' + folderName)
    print('The subFolders in : ' + folderName + ' are : ' + str(subFolders))
    print('The filenames in ' + folderName + ' are : ' + str(fileNames))
    print()
    
