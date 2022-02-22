// compiled: gcc -g vsyscall.c -o vsyscall
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void backdoor();

int maian()
{
    char buf[0x100];
    read(0, buf, 0x100 - 1);
    // 直接跳转到buf
    asm("jmp  %0" :  : "m" (buf));

    return 0;
}


//compiled: gcc test.c -g -o test
int main()
{
    asm(// str: /bin/sh
				"mov $0x0068732f6e69622f, %rax\n"
				"push %rax\n"

				"mov %rsp, %rdi\n"
				"mov $59, %rax\n" // #define __NR_execve 59
				"mov $0, %rsi\n"
				"mov $0, %rdx\n"

				"mov $0xFFFFFFFFFF600000, %rbx\n"
				"jmp %rbx\n");
		return 0;
}

void backdoor()
{
    execve("/bin/sh", NULL, NULL);
}
