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