print("Q 1. Write a Python program to get the file size of a plain file.")
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))
print("\nQ 2. Write a Python program to extract characters from various text files and puts them into a list.")
import glob
char_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       char_list.append(f.read())
print(char_list)
