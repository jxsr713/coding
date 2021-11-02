#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

#define ZWH1 1
#define ZWH1
void printIntList(int * s, int len){
    int i = 0;
    for(i=0; i < len; i++){
        printf("[%d]:%d  ", i, s[i]);
    }
    printf("\n");

    return;
}

void printCharList(char * s, int len){
    char ch;
    int i = 0;
    for(i=0; i < len; i++){
        printf("[%d]:%c  ", i, s[i]);
    }
    printf("\n");

    return;
}

void printData(int *is, char *cs, char * os, int len){
    printIntList(is, len);
    printCharList(cs, len);
    printCharList(os, len);
    return;
}

int isValid(char * s)
{
    int len = strlen(s);
    char * posLst;
    int * idxLst;
    char matStr = 0;
    int ret = 0, matchPos = 0;
    int i = 0;

    if (len % 2)
        return 0;
    
    posLst = (char *)malloc(len * sizeof(char));
    memset(posLst, '0', len);
    idxLst = (int *)malloc(len * sizeof(int));
    memset(idxLst, 0 , len);

    for(i = 0; i < len; i++){
        ret = 0;
        posLst[i] = s[i];
        if(s[i] == '('){
            matchPos = i;
            matStr = ')';
            posLst[i] = matStr;
        } else if (s[i] == '{') {
            matchPos = i;
            matStr = '}';
            posLst[i] = matStr;
        } else if (s[i] == '[') {
            matchPos = i;
            matStr = ']';
            posLst[i] = matStr;
        } else {
            if(matStr == s[i]) {
                posLst[matchPos] = posLst[i] = '0';
                if( posLst[matchPos-1] == '0' ){
                    idxLst[i] = idxLst[matchPos] = idxLst[matchPos-1];
                    matchPos = idxLst[matchPos - 1];
                } else {
                    idxLst[matchPos] = idxLst[i] = matchPos-1;
                    matchPos = matchPos - 1;
                }
                matStr = posLst[matchPos];
                ret = 1;
            }
            else{
                break;
            }
        }
    }
    return ret;
}


int  main(int  argc ,char *argv[ ]) { 
    char * s = "{[]}[{()}]";
    int ret = 0;

    if( argc > 1)
        s = argv[1];

    ret = isValid(s);

    printf("Get ret:%d\n", ret);
    return 0;
}
