#include <stdio.h>

#include <math.h>

int hasFactors(int num) {
    int count = 0;
    for (int factor = 1; factor <= num; factor ++) {
        if (num % factor == 0) {
            count ++;
        }
    }
    return count;
}


int main(int argc, char **argv) {
    int theNum = 35;
    int theNumHasFactors = hasFactors(theNum);
    printf("%d has %d factors", theNum, theNumHasFactors);
    return 0;
}