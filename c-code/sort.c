#include <stdio.h>
#include <stdlib.h>

int shellsortLF(int *p,int n)
{
    int op=0;
    int h,i,j,temp;

#if 0


    int k,gap, length;
    length = n;
    for(gap = length/2; gap > 0;gap = gap/2){
        for(i= 0;i<gap;i++){
            printf("[%d]:%d",i, array[i]);
            for(j = i + gap; j < length; j = j+gap){
                if(array[j] < array[j - gap]){
                    temp = array[j];
                    k = j-gap;
                    while(k>=0 && array[k]>temp){
                        array[k + gap] = array[k];
                        k = k - gap;
                    }
                    array[k + gap] = temp;
                }
            }   
        }
    }
    printf("==",array);
    return 1;
#else
    for(h=n/2;h>0;h=h/2)
    {
        if(h%2==0)
            h--;
        printf("==========>>>>%d\n", h);
        for(i=h;i<n;i++){
            temp=p[i];
            printf("i:%d [%d]\n", i, temp);
            for(j=i-h;j>=0&&p[j]>temp;j-=h){
                printf(":::::::j:%d[%d] h:%d\n", j, p[j], h);
                if(p[j] > temp){
                    p[j+h]=p[j];
                    op++;
                }
                printArray(p, n);   
            }
            p[j+h]=temp;
            op++;
            printf("==>>>>");
            printArray(p, n);   
        }
        printArray(p, n);   
    }
    return op;
#endif
}

void printArray(int *p, int n){
    int i = 0;
    for(i = 0; i < n; i++){
        printf(" %d ", p[i]);
    }
    printf("\n");
    return;
}

void main(int argc, char *argv[] )
{
    int i = 0;
    int size = 9;
    int p[9]= {12,32,45,11,22,1,78,98,4};
    printf("argc:%d", argc);
    if(argc == 2) {
            if (!strcmp("test", argv[1])){
                printf("test111\n");
                    }
            else{
                        goto usage;
                    }
        }else if (argc > 3) {
                if (!strcmp("set", argv[1])){
                            int ledidx, mod;
                            char * pEnd;
                            ledidx = strtoul(argv[2], &pEnd, 10);
                            mod = strtoul(argv[3], &pEnd, 10);
                
                            printf("Idx:%d mod:%d\n", ledidx, mod);
                
                        }
                else{
                
                            goto usage;
                        }
        
            }
        else{
                goto usage;
            }
            return;
usage:
    printf("Usage\n");
    return;


    printArray(p, size);   
    shellsortLF(p, size);
    printArray(p, size);   
    return;
}
