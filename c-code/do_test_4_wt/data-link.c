/*
 * =====================================================================================
 *
 *       Filename:  data-link.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2021年11月01日 13时54分32秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <stdio.h>
#include <time.h>


//the new node insert into the begin of list
//get the node from the end of list 

///////////////////////////////////////////////////////////////
//record buffer saved sensor data
//the link used to maintain data which need to send and save to fs
typedef struct node{
	//pointer to buffer
	//char * buff;
	int buff;
	//the type of data
	int type;
	//the status of buffer
	int status;
	//timestamp for capture data_type
	time_t tstmp;
	struct node * next;

} data_node, * data_list;


//pointer to the list of data
static data_list  p_header = NULL;
static data_list  p_tailer = NULL;


data_list init_data_node(int buff, int type, time_t stmp){
	data_list p = (data_list)malloc(sizeof(data_node));
	if( p == NULL )
		return NULL;
	
	p->buff = buff;
	p->type = type;
	p->tstmp = stmp;
	p->status = 0;
	p->next = NULL;

	return p;
}


int init_list(void){
	if(p_header != NULL){
		printf("header is exist! refuse to init again!");
		return -2;
	}

	p_header = init_data_node(0, -1, time(NULL));
	if( p_header == NULL)
		return -1;
	
	return 0;

}

int insert_node(int buff, int type, time_t stmp){

	if(p_header == NULL){
		printf("Init header\n");
		if(init_list() != 0)
			return 1;
	}

	data_list p = init_data_node(buff, type, stmp);
	if( p == NULL)
		return 2;
	
	p->next = p_header->next;
	p_header->next = p;

	return 0;
}

data_list get_tailer(void){
	if(p_header == NULL)
		return NULL;

	data_list p = p_header->next;

	while( p && p->next){
		p = p->next;
	}

	return p;
}

int delete_tailer(void){
	if(! p_header || ! p_header->next)
		return 1;

	data_list post = p_header;
	data_list cur = p_header->next;
	data_list pre = cur->next;


	while(pre){
		post = cur;
		cur = pre;
		pre = cur->next;
	}

	
	printf("deleting buffer:%d  type:%d status:%d\n", cur->buff, cur->type, cur->status);
	//check the status, if the status is 100, then delete the node
	if(cur->status != 100)
		return 2;

	post->next = NULL;
	free(cur);
	cur = NULL;

	return 0;

}


int travel_list(void){
	if(! p_header )
		return 1;

	data_list p = p_header->next;

	while(p){
		printf("Travel::::: buffer:%d  type:%d status:%d\n", p->buff, p->type, p->status);
		p = p->next;
	}
	printf("Travel Done!\n");
	return 0;
}


int destroy_list(void){
	if(! p_header )
		return 1;

	data_list cur = p_header;

	while(cur){
		data_list p = cur;
		cur = cur->next;
		
		free(p);
		p = NULL;
	}

	return 0;
}



//this function called by send data function
//this function should be put in the tx callback of uart/lte
//if the data was send successfully, then need to update the status to send done
int send_callback(void){

	return 0;
}

/* *************************************** */
//test function
int get_opt(void){
	int ch;
	printf("\n\n\n=====Menu=====\n");
	printf("1: insert a new node!\n");
	printf("2: get tailer node!\n");
	printf("3: delete a node!\n");
	printf("4: travel list !\n");
	printf("5: initialize list !\n");
	printf("0: exit !\n");
	printf("Please select function:");
	scanf("%d", &ch);
	printf("=====opt: %d=====\n", ch);
	
	if(ch > 100)
		ch = 100;
	return ch;
}


int insert_test(void){
	int buff = rand();
	int type = rand() % 10;
	int ret = insert_node(buff, type, time(NULL));

	return ret;
}


int get_test(void){
	data_list p = get_tailer();
	if(!p)
		printf("No tailer!");
	else
		printf("buffer:%d  type:%d status:%d\n", p->buff, p->type, p->status);
	return 0;
}

int delete_test(void){
	int ret = 0;
	if( (ret = delete_tailer()) != 0 )
		printf("Error:%d\n", ret);
	else
		printf("Deleted the tailer node!\n");

	return 0;
}

int travel_test(void){
	travel_list();
}
/* *****************************************
 *
 * ****************************************/
int main(void){
	int opt = 200;
	while(opt != 0){
		opt = get_opt();
		switch (opt){
			case 1:
				insert_test();
				break;
			case 2:
				get_test();
				break;
			case 3:
				delete_test();
				break;
			case 4:
				travel_test();
				break;
			case 5:
				break;
			case 0:
				break;
			default:
				continue;
		}
		travel_list();
	}


	if( init_list() != 0)
		return 0;
	


	return 0;
}
