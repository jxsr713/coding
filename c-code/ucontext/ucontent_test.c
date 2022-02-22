/*
 * =====================================================================================
 *
 *       Filename:  test.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年12月06日 11时33分26秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ucontext.h>

int print(int i){
		printf("%s:::: %d\r\n", __FUNCTION__, i);
		return 0;
}
int main()
{
		int i = 0;
		ucontext_t ctx;//定义上下文结构体变量
		
		getcontext(&ctx);//获取当前上下文
		printf("i = %d\n", i++);
		sleep(1);
		if(i < 10)
				setcontext(&ctx);//回复ucp上下文		
		printf("%s: end!\r\n", __FUNCTION__);

		print(i);
		return 0;
}

