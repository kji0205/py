#include <stdio.h>

main()
{
// printf ( " %d \n", 0x31 ) ;
// printf ( " %o \n", 0x31 ) ;
// printf ( " %x \n", 0x31 ) ;
    // printf("hello");
    fib(30);
}

int fib(int n) {
    if (n < 2)
        return n;
    else
        return fib(n-1) + fib(n-2);
}
