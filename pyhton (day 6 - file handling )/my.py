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


    
# reading data of file
def append_to_file(filename,data):
    f=open(filename,"a")
    f.write("\n") #for extra line
    f.write(data)
    print("data appended successfully")


def read_from_file(filename):
    try:
        f=open(filename,'r')
        data = f.read()
        print(data)
    except FileNotFoundError:
        print("file not found")

def main():
    # name=input("Enter your data to append : ")
    # append_to_file("file1.txt",name)
    # print("file create successfully")
    read_from_file("abc.txt")


main()