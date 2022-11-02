print("Q 1. Write a Python program to read a file line by line store it into a variable")
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')
print("Q 2. copy the contents of a file to another file")
from shutil import copyfile
copyfile('test.txt', 'abc.txt')
