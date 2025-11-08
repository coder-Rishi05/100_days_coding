# 31 day-31 (c code from python)

the reason we do this because python is very fast.

stpes:

1. create a c file ex: c_code.c
2. run the c file and make its exe. ex: c_code
3. create a python file ex: c.py
4. run the c code by this library
   ex:
   import subprocess

subprocess.run(['./c_code'])

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;
        printf("Argument count : %d", argc);
    for (i = 0; i < argc; i++)
    {
        printf("\n %d). %s", i, argv[i]);
    }
    // printf("Hello ");
    printf("\n");
    return 0;
}


```

```py
import subprocess


print("Enter 3 numbers")
a,b,c=input(),input(),input()
subprocess.run(['./c_code',a,b,c])

```

- homework

explore this function

subprocess.run(['./c_code',a,b,c])
