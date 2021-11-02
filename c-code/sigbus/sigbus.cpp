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
#include <stdlib.h>
/*************************************************************************
    > File Name: sigbus.cpp
    > Author: weihong
    > Mail:  
    > Created Time: 2021年10月21日 星期四 09时13分43秒
 ************************************************************************/

#include<iostream>
#include<cstdlib>

using namespace std;


void  enable_align_check(void)
{
#if defined( __GNUC__ )
#if defined( __i386__ )
	/*  enable alignment checking on x86 */
	asm( "pushf\n\torl $0x40000,(%esp)\n\tpopf" );
#elif defined( __x86_64__ )
	/*  enable alignment checking on x86_64 */
	asm( "pushf\n\torl $0x40000,(%rsp)\n\tpopf");
#endif
#endif

	return;
}


int main(int argc, char * argv[]){
	unsigned int i = 0x12345678;
	unsigned int *q = NULL;
	unsigned char *p = (unsigned char *)&i;
	
	cout << "q:" << (void *)q << endl;
	cout << "p:" << (void *)p << endl;

	*p = 0x0;
	q = (unsigned int *)(p + 1);
	*q = 0x0;
	
	cout << "q:" << (void *)q << endl;
	cout << "p:" << (void *)p << endl;
	//if enable unaligned error in MSR, the code gen sigbus
	//otherwise gen sigsegv
	int *pc1 = (int *) 0x00001111;
	*pc1 = 20;
	
	char *pc2 = (char *) 0x00001111;
	*pc2 = 20;

	cout << " OVER" << endl;
	return 1;
}



