import os

# join the passed arguments in os format
print(os.path.join('folder1', 'folder2'))

# return the absolute path of provided argument
print(os.path.abspath('file_handling.py'))
print(os.path.abspath('../../Selenium'))

# check if the provided path is absolute or not
print(os.path.isabs('/Users/Kingslayer/Downloads/Selenium'))
print(os.path.isabs('../../Selenium'))

# return the relative path
print(os.path.relpath('/Users/Kingslayer/Downloads/Selenium'))

# get the dir name ( the part before the last slash)
print(os.path.dirname('/Users/Kingslayer/Downloads/Selenium'))

# get the last part of the path
print(os.path.basename('/Users/Kingslayer/Downloads/Selenium'))

# check existence of file
print(os.path.exists('/Users/Kingslayer/Downloads/PythonLearning/Python_Basics'))

# check if the provided path is a file or not
print(os.path.isfile('/Users/Kingslayer/Downloads/PythonLearning/Python_Basics'))
print(os.path.isfile('/Users/Kingslayer/Downloads/PythonLearning/Python_Basics/exit.py'))

# check if the provided path is a dir or not
print(os.path.isdir('/Users/Kingslayer/Downloads/PythonLearning/Python_Basics'))
print(os.path.isdir('/Users/Kingslayer/Downloads/PythonLearning/Python_Basics/exit.py'))

# get size of directory/folder
print(os.path.getsize('/Users/Kingslayer/Downloads/Document.pdf'))

# get directory structure
print(os.listdir('/Users/Kingslayer/Downloads/'))

# create new folder
os.mkdir('/Users/Kingslayer/Downloads/PythonLearning/test')
