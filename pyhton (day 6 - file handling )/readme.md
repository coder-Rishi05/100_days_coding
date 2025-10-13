### File handling in python.

file handling used for storing data and performing operatins later.
as when we create programs all variable get memory when program finished then it all variables will loose the memory. there for we use file handling,

- basic operations

```
1. open a file.
2. read/write
3. close file.

file opening modes.
r  <=> read only reading/ if file not exist then error throw.
w  <=> write if exist / create a new file . it will erase previous data and create new one.
a  <=> append on existing file / not exist = create a new file
r+ <=> if file not exist will  create new file and then read.
w+ <=> work same as w.
a+ <=> work same as a.
```

types of file

1. binary
2. text : we usually handle text file.

code example:

# file creation function and writing

```

"""def write_to_file(filename,name):
    f=open(filename, 'w')
    f.write(name)"""


"""def main():

    name=input("Enter your name : ")
    write_to_file("file1.txt",name)
    print("file create successfully")"""
```

# append data to file

```

def append_to_file(filename,data):
    f=open(filename,"a")
    f.write("\n") #for extra line
    f.write(data)
    print("data appended successfully")


def main():
    
    name=input("Enter your data to append : ")
    append_to_file("file1.txt",name)
    print("file create successfully")


main()

```
