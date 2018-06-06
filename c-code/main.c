#include <stdio.h>
#include <string.h>

int main(int argv, char* argc[])
{
    int i;
    int a[4]={0};
    char* args = argc[1];
    int len;
    if(argv < 2) {
        printf ("need parameter\n");
        return -1;
    }

    for( i = 0; args[i];  i++){
        switch (args[i]){
            case '(':
                a[0]++;
                break;
            case ')':
                a[1]++;
                break;
            case '{':
                a[2]++;
                break;
            case '}':
                a[3]++;
                break;
        }
    }

    if(a[0] == a[1] && a[2]==a[3]) {
        printf("matched \n");
        return 1;
    }
    else {
        printf("not matched \n");
        return 0;
    }

    return 0;
}
