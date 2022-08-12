#include <stdio.h>
#include <stdlib.h>	//incluede itoa
#include <string.h>
#include <getopt.h>

#if defined(__GNUC__)    // GCC
		#include <cpuid.h>
#else
		#error Only supports GCC.
#endif    // #if defined(__GNUC__)

#define BUF_LEN 64


struct opt_cpuid {
	unsigned int eax;
	unsigned int ebx;
	unsigned int ecx;
	unsigned int edx;
	unsigned char index;
	unsigned char offset;
};

const char cpuid_name[4][4]={"EAX", "EBX", "ECX", "EDX"};

char * itob(unsigned long long v, char* buf, int len) {
		
		memset(buf, '0', len);
		if (0 == v) {
				return buf;
		}
		char* dst = buf + len - 1;
		while (v) {
				char ch = (v & 1) + '0';
				*dst = ch;
				dst--;
				v = v >> 1;
		}
		return buf;
}

void print_binary(char *buf, int len, char intval){
	char *ptr, *tmp;
	int intv_cnt = (len / 4);

	tmp = ptr = (char *)malloc(sizeof(char) *(len + intv_cnt));
	memset(ptr, 0, len + intv_cnt);
	
	for(int i = 0; i < len; i++){
		if(i > 0){
			if(i % 4 == 0){
				*ptr = intval;
				ptr++;
			}
		}

		*ptr = buf[i];
		ptr++;
	}

	printf("%s\n", tmp);
	free(tmp);
	return;
}

// print the value of cpuid: eax, ebx, ecx, edx
void dump_cpuid(unsigned int cpuid[4]){

	printf("###############:31--- ---- ---- ----|---- ---- ---- ---0\n");
	
	for(int i = 0; i < 4; i++) {
		unsigned int val = cpuid[i];
		char binStr[32];

		itob(val, binStr, 32);

		printf("[%s] %08x :", cpuid_name[i], val);
		print_binary(binStr, 32, ' ');
	}

	return;
}


/* infotyp => eax; ecxvalue=>ecx; eax/ebx/ecx/edx=>cpuinfo */
void getcpuidex(unsigned int CPUInfo[4], unsigned int InfoType, unsigned int ECXValue)
{
	printf("%s\n", __func__);
    __cpuid_count(InfoType, ECXValue, CPUInfo[0],CPUInfo[1],CPUInfo[2],CPUInfo[3]);
}

/* infotype => eax no ecx */
void getcpuid(unsigned int CPUInfo[4], unsigned int InfoType)
{
    __cpuid(InfoType, CPUInfo[0],CPUInfo[1],CPUInfo[2],CPUInfo[3]);
		//dump_cpuid(CPUInfo);
}

/* infotyp => eax; ecxvalue=>ecx; eax/ebx/ecx/edx=>cpuinfo */
void fetch_cpuid(struct opt_cpuid *opt, unsigned int CPUInfo[4])
{
	if(opt->ecx > 0)
		getcpuidex(CPUInfo, opt->eax, opt->ecx);
	else
		/* infotype => eax no ecx */
		getcpuid(CPUInfo, opt->eax);
}


// 取得CPU厂商（Vendor）.
//
// result: 成功时返回字符串的长度（一般为12）。失败时返回0.
// pvendor: 接收厂商信息的字符串缓冲区。至少为13字节.
int cpu_getvendor(char* pvendor)
{
    unsigned int dwBuf[4];
    if (NULL==pvendor)    return 0;
    // Function 0: Vendor-ID and Largest Standard Function
    getcpuid(dwBuf, 0);
    // save. 保存到pvendor
    *(unsigned int *)&pvendor[0] = dwBuf[1];    // ebx: 前四个字符.
    *(unsigned int *)&pvendor[4] = dwBuf[3];    // edx: 中间四个字符.
    *(unsigned int *)&pvendor[8] = dwBuf[2];    // ecx: 最后四个字符.
    pvendor[12] = '\0';
    return 12;
}

// 取得CPU商标（Brand）.
//
// result: 成功时返回字符串的长度（一般为48）。失败时返回0.
// pbrand: 接收商标信息的字符串缓冲区。至少为49字节.
int cpu_getbrand(char* pbrand)
{
    unsigned int dwBuf[4];
    if (NULL==pbrand)    return 0;
    // Function 0x80000000: Largest Extended Function Number
    getcpuid(dwBuf, 0x80000000U);
    if (dwBuf[0] < 0x80000004U)    return 0;
    // Function 80000002h,80000003h,80000004h: Processor Brand String
    getcpuid((unsigned int *)&pbrand[0], 0x80000002U);    // 前16个字符.
    getcpuid((unsigned int *)&pbrand[16], 0x80000003U);    // 中间16个字符.
    getcpuid((unsigned int *)&pbrand[32], 0x80000004U);    // 最后16个字符.
    pbrand[48] = '\0';
    return 48;
}

//check the value of feature from cpuid
int check_feature(unsigned int cpuid[4], unsigned int idx){
		int index = idx / 32;
		if(index > 4)
				return 0;

		int val = cpuid[index];
		int offset = idx % 32;
		int ret = (val >> offset) & 1 ;
		//rintf("%x %x ===>%x\n", val, (1 << offset), ret);
		printf("Index:%d [%s] val: 0x%08x offset:%d\n", index,
			cpuid_name[index], val, offset);
		return ret ;

}
char szBuf[64];
unsigned int dwBuf[4];
int idx=0;

static void parse_parameter(struct opt_cpuid * opt, int argc, char **argv)
{
	int32_t c = 0;
	const char *option_string = "a:b:c:d:i:o:h";
	while ((c = getopt(argc, argv, option_string)) != -1)
	{
		switch (c) {
			case 'a':
				opt->eax = strtoul(optarg, NULL, 16);
				break;
			case 'b':
				opt->ebx = strtoul(optarg, NULL, 16);
				break;
			case 'c':
				opt->ecx = strtoul(optarg, NULL, 16);
				break;
			case 'd':
				opt->edx = strtoul(optarg, NULL, 16);
				break;
			case 'i':
				opt->index = strtoul(optarg, NULL, 10);
				printf("index:%x\n", opt->index);
				idx = 1;
				break;
			case 'o':
				opt->offset = strtoul(optarg, NULL, 10);
				break;
			default:
				exit(1);
		}
	}

}



int main(int argc, char* argv[])
{
	struct opt_cpuid opt;
	//unsigned int eax = 0, ebx = 0, ecx = 0, edx = 0;
	unsigned int cpuid[4];
  // test
	memset(&opt, 0, sizeof(opt));
	parse_parameter(&opt, argc, argv);

	printf("====== Get cpuid. eax: 0x%x ecx: 0x%x=======\n", opt.eax, opt.ecx);

	fetch_cpuid(&opt, cpuid);

	dump_cpuid(cpuid);

	printf("===================================================\n");
	if (idx == 1) {
		int ret = 0;
		int p = opt.index * 32 + opt.offset;
		//printf("index:%d off:%d\n", opt.index, opt.offset);
		ret = check_feature(cpuid, p);
		printf("Check %d: ret %d\n", p, ret);

	}

	return 0;

/*
  cpu_getvendor(szBuf);
  printf("CPU Vendor:\t%s\n", szBuf);

  cpu_getbrand(szBuf);
  printf("CPU Name:\t%s\n", szBuf);

  return 0;
  */
}
