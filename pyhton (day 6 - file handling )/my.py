"""

1. open a file.
2. read/write
3. close file.

file opening modes.
r read
w write if exist / create a new file 
a append on existing file / not exist = create a new file
r+
w+
a+

"""
import os

# using with keyword

def write_file(filename):
    try:
        with open(filename,'w+') as f:
            f.write("this is file handling & (with) keyword")
            print("file created successfully")
    except:
        print("file not found")


def main():
    write_file("file.txt")

main()