#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>
typedef struct Queue{
    int * PBase;
    int front;
    int rear;
}QUEUE;

void initQueue(QUEUE * pQ)
{
     
    pQ->PBase=malloc(sizeof(int)*6);
    pQ->front=0;
    pQ->rear=0;
}

bool isfull(QUEUE * pQ)
{
    if((pQ->rear+1)%6==pQ->front)
    {
        printf("队列已满，无法插入");
        return true;
    }
    return false;
}

bool isempty(QUEUE * pQ)
{
    if(pQ->front==pQ->rear)
    {
        printf("队列为空");
        return true;
    }
    return false;
}


bool insert(QUEUE *pQ,int val)
{
    if(isfull(pQ))
        return false;
    printf("before:::: f:%d, r:%d\n", pQ->front, pQ->rear);
    pQ->PBase[pQ->rear]=val;
    pQ->rear=(pQ->rear+1)%6;
    printf("in val:%d, f:%d, r:%d\n",val,  pQ->front, pQ->rear);
    return true;

}


void traverse(QUEUE * pQ)
{
    int i=pQ->front;
    printf("trave:====>");
    while(i!=pQ->rear)
    {
        printf("%d ",pQ->PBase[i]);
        i++;
        i=i%6;
    }
    printf("\n");
}

bool out_queue(QUEUE * pQ)
{
  if(isempty(pQ))
      return false;
  printf("out val:%d ", pQ->PBase[pQ->front]);
     pQ->front=(pQ->front+1)%6;
  printf("f:%d, r:%d\n",  pQ->front, pQ->rear);
}

int main(void)
{
    QUEUE Q;
    initQueue(&Q);

    insert(&Q,3);
    traverse(&Q);
    insert(&Q,4);
    traverse(&Q);
    insert(&Q,14);
    traverse(&Q);
    insert(&Q,41);
    traverse(&Q);
    insert(&Q,411);
    traverse(&Q);
    insert(&Q,45);
    traverse(&Q);
    insert(&Q,44);
    traverse(&Q);
    insert(&Q,43);
    traverse(&Q);
    insert(&Q,42);
    traverse(&Q);
    out_queue(&Q);
    traverse(&Q);
    return 0;
    insert(&Q,4);
    insert(&Q,5);
    insert(&Q,6);
    insert(&Q,7);
    insert(&Q,8);
    
    traverse(&Q);
    out_queue(&Q);
    out_queue(&Q);
    out_queue(&Q);
    out_queue(&Q);

traverse(&Q);
insert(&Q,2);
insert(&Q,9);
insert(&Q,0);
insert(&Q,1);
insert(&Q,11);
//insert(&Q,1);
//insert(&Q,9);
traverse(&Q);
return 0;
}
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    
    
    

    
    
    
    
    
    
    
    
