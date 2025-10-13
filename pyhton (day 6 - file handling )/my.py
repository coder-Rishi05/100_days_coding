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


    
# append data to file
def append_to_file(filename,data):
    f=open(filename,"a")
    f.write(data)
    print("data appended successfully")


def main():
    
    name=input("Enter your data to append : ")
    append_to_file("file1.txt",name)
    print("file create successfully")


main()