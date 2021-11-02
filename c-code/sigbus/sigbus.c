/*
 * =====================================================================================
 *
 *       Filename:  sigbus.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年10月21日 09时13分43秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
/*************************************************************************
    > File Name: sigbus.cpp
    > Author: weihong
    > Mail:  
    > Created Time: 2021年10月21日 星期四 09时13分43秒
 ************************************************************************/

#include <stdlib.h>
#include <stdio.h>



int main(int argc, char * argv[]){
	unsigned int i = 0x12345678;
	unsigned int *q = NULL;
	unsigned char *p = (unsigned char *)&i;
	
	printf("q:0x%p\n", q);
	printf("p:0x%p\n", p);

	*p = 0x0;
	q = (unsigned int *)(p + 1);
	*q = 0x0;
	printf("q:0x%p\n", q);
	printf("p:0x%p\n", p);
	
	//the code gen sigbus;
    __asm__("mov rbp,0x400000000000000\n"
			            "mov rax,[rbp]\n"
						            "ud2\n");
	//char *pc = (char *) 0x00001111;
	//the code gen sigsegv error
	int *pc = (int *) 0x00001111;
	printf("pc:0x%p\n", pc);
	*pc = 20;

	return 1;
}



