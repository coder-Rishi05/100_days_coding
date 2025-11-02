"""

print first natural number (1-n).
1. assume that desired recursion function already created.
2. create a recursive case. (formula to solve the problem).
3. Base case : to stop recursion.

ex: 

f1(n)
1. f1(n) ->> 1......n
2. f1(n-1) ->> to print smaller number n-1
3. base case if n==1  return 1. 
"""

def f1(n):
    if n==0:return
    print(n)
    f1(n-1)

f1(0)