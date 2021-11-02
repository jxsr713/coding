#include "stdio.h"
#include "isBigEndian.h"

int check_big_endian(void)
{
  union w
 {
   int a;  //4 bytes
   char b; //1 byte
  } c;
  c.a=1;
  if (c.b==1)
  printf("It is Little_endian!\n");
  else
  printf("It is Big_endian!\n");
  return 1;
}

#ifndef _MAIN_CODE_
int main(void){
    check_big_endian()
}
#endif
