#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
 
#include "cpuid.h"
 
void get_cpu_vendor(char* cpu_vendor, int* cpuid_level)
{
	char vendor_name[16];
 
	vendor_name[0] = '\0'; /* Unset */
 
    int level = 0;
    struct cpuid_result result;
    result = cpuid(0x00000000); // eax为0表示读取vendor id，一共12字节，依次在ebx、edx、ecx。
    level    = result.eax;
    vendor_name[ 0] = (result.ebx >>  0) & 0xff;
    vendor_name[ 1] = (result.ebx >>  8) & 0xff;
    vendor_name[ 2] = (result.ebx >> 16) & 0xff;
    vendor_name[ 3] = (result.ebx >> 24) & 0xff;
    vendor_name[ 4] = (result.edx >>  0) & 0xff;
    vendor_name[ 5] = (result.edx >>  8) & 0xff;
    vendor_name[ 6] = (result.edx >> 16) & 0xff;
    vendor_name[ 7] = (result.edx >> 24) & 0xff;
    vendor_name[ 8] = (result.ecx >>  0) & 0xff;
    vendor_name[ 9] = (result.ecx >>  8) & 0xff;
    vendor_name[10] = (result.ecx >> 16) & 0xff;
    vendor_name[11] = (result.ecx >> 24) & 0xff;
    vendor_name[12] = '\0';
    //printf("vendor_name: %s\n", vendor_name);
    
    strcpy(cpu_vendor, vendor_name);
    *cpuid_level = level;
}
 
void get_cpu_version(unsigned int* version)
{
    unsigned int tmp = 0;
    tmp = cpuid_eax(0x00000001);
    
    *version = tmp;
}
 
struct cpuinfo_x86 {
	uint8_t	x86;		/* CPU family */
	uint8_t	x86_vendor;	/* CPU vendor */
	uint8_t	x86_model;  /* CPU model */
	uint8_t	x86_step;  /* CPU stepping */
};
 
// 参考IA32开发手册第2卷第3章。CPUID exa==0x01的图3-6
static inline void get_fms(struct cpuinfo_x86 *c, uint32_t tfms)
{
	c->x86 = (tfms >> 8) & 0xf;
	c->x86_model = (tfms >> 4) & 0xf;
	c->x86_step = tfms & 0xf;
	if (c->x86 == 0xf)
		c->x86 += (tfms >> 20) & 0xff;
	if (c->x86 >= 0x6)
		c->x86_model += ((tfms >> 16) & 0xF) << 4;
}
 
void get_cpu_fms(int* family, int* model, int* stepping)
{
    struct cpuinfo_x86 c;
    unsigned int ver = 0;
    
    ver = cpuid_eax(0x00000001);
    get_fms(&c, ver);
    
    *family = c.x86;
    *model = c.x86_model;
    *stepping = c.x86_step;
}
 
void get_cpu_name(char* processor_name)
{
	struct cpuid_result regs;
	char temp_processor_name[49];
	char* processor_name_start;
	unsigned int *name_as_ints = (unsigned int *)temp_processor_name;
	int i;
 
	/* 
	用cpuid指令，eax传入0x80000002/0x80000003/0x80000004，
	共3个，每个4个寄存器，每个寄存器4字节，故一共48字节。
	参考IA32开发手册第2卷第3章。
	*/
	for (i = 0; i < 3; i++) {
		regs = cpuid(0x80000002 + i);
		name_as_ints[i * 4 + 0] = regs.eax;
		name_as_ints[i * 4 + 1] = regs.ebx;
		name_as_ints[i * 4 + 2] = regs.ecx;
		name_as_ints[i * 4 + 3] = regs.edx;
	}
 
	temp_processor_name[49] = '\0'; // 最后的字节为0，结束
 
	/* Skip leading spaces. */
	processor_name_start = temp_processor_name;
	while (*processor_name_start == ' ')
		processor_name_start++;
 
	memset(processor_name, 0, 49);
	strcpy(processor_name, processor_name_start);
}
 
void get_address_bits(int* linear, int* physical)
{
    unsigned int tmp = 0;
    tmp = cpuid_eax(0x80000008);
    *linear = (tmp>>8) & 0xff;
    *physical = (tmp>>0) & 0xff;
    
}