#include <stdio.h>

int index(int arr[], int value, int size){
    for (int i = 0; i < size; i++) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}

int main(void)
{
    int fib8[] = {0, 1, 1, 2, 3, 5, 8, 13};

    int s = index(fib8, 3, 8);

    printf("%d\n", s);
}