/*
 * =====================================================================================
 **       Filename:  test_sigbus.c
 **   Description:
 **        Version:  1.0
 *       Created:  2022年10月27日 15时08分42秒
 *       Revision:  none
 *       Compiler:  gcc
 **         Author:  YOUR NAME (),
 *   Organization:
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include<stdio.h>

int unalign_access(void)
{
#if defined( __GNUC__ )
#if defined( __i386__ )
        asm( "pushf\n\torl $0x400a00,(%esp)\n\tpopf" );
#elif defined( __x86_64__ )
        asm( "pushf\n\torl $0x40000,(%rsp)\n\tpopf" );
#endif
#endif
        char buff[9] = {0};

        int * pi = (int *)(buff + 3);

        *pi = 100;

        printf("Get %d\n", *pi);
        return 0;
}

int stack_fault(void)
{
        int a=10,b=3;
        printf("汇编处理前b=%d\n",b);
        __asm__(
                "movl $5, %%eax;"
                "movl %%eax, %0;"
                :"=r"(b)          /*输出部*/
                :"r"(a)           /*输入a部*/
                :"%eax"           /*修正部*/
        );
        printf("汇编处理后b=%d a %d\n", b, a);
        // __asm__("movl %rbp,0x400000000000000\n");
        //         "mov rzx,[rbp]\n"
        //         "ud2\n");
        return 0;
}

int read_cr4(void)
{
	long unsigned int cr0;
	long unsigned int cr4;
	asm volatile("mov %%cr0, %0": "=b"(cr0));
	asm volatile("mov %%cr4, %0": "=b"(cr4));
	printf("CR0:%x  CR4:%x\n", cr0, cr4);
	return 0;

}

int main(void)
{
	read_cr4();

	return 0;
        stack_fault();
        char *p = 0x400000000000000;
        *p = 0x1;
        return 0;
}



