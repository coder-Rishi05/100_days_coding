import subprocess


print("Enter 3 numbers")
a,b,c=input(),input(),input()
subprocess.run(['./c_code',a,b,c])