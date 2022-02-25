#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main( int argc, char *argv[]) {
    clock_t start_t, end_t;
    static int data[64*1024*1024];
	int numBits= atoi(argv[1]);	
	static int temp =0;
	int mod = (int)pow(2, numBits)-1;
        for (int a = 0; a < pow(2, 26); a++) {
        int index = (a<<4) & mod;
	    temp = data[index];
            data[index] = temp;
        }


}
