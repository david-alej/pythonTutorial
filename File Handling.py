# File handling is important part of any web application. Python can create, read, update, and delete a file. We can open a file using the the open() function;

f = open('./directory/imaginarytextfile.txt', 'rt')

#where the first argument is the name of the file with its type of file( text in this ccase) and the second is mode which can be :
# r - read: Opens a file for reading, error if the files does not exist
# a - Append: Opens a file for appending, creates the file if it does not exist
# w - Write: Opnes a file for writting, cretes the file if ti does not exist
# x - Create: the specififed file, returns an error if the files exists
#you can also specify how it should be handled:
# t - Text: Defalt value. Text mode
# b - Binary: Ninary mode(e.g. images)

# After openning a file you can read its contents with the read() method:

print(f.read())

#you can also specify what to read by adding a number to the second argument to give back the number first characters of the file
#Another function is the write() to write to an existing file. 
f.write('hi')
f.close()

#Its is good practice to close a file when you are donw with it.


# You cna delete a file by using os.remove() function.

import os

os.remove('./direcotry/imaginarytextfile')

# You can check if a file exist by:

if os.path.exist('demofile.txt'):
  os.remove('demofile.txt')
  

# we can remove a direcotry by using function:

os.rmdir('myfolder')

