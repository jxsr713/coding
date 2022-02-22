#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
 
#include "cpuid.h"
//#include "msr.h"
 
int main(void)
{
    char buffer[49] = {0};
    unsigned int version = 0;
    int cpuid_level;
    
    get_cpu_vendor(buffer, &cpuid_level);
    printf("vendor_id\t: %s\n", buffer);
    printf("cpuid level\t: %d\n", cpuid_level);
    
    get_cpu_name(buffer);
    printf("model name\t: %s\n", buffer);
    
    get_cpu_version(&version);
    
    int f,m,s;
    get_cpu_fms(&f, &m, &s);
    printf("cpu family\t: %d(0x%X)\n", f, f);
    printf("model\t\t: %d(0x%X)\n", m, m);
    printf("stepping\t: %d(0x%X)\n", s, s);
    
    int phy_bits = 0;
    int vir_bits = 0;
    get_address_bits(&vir_bits, &phy_bits);
    printf("address sizes\t: %d bits physical, %d bits virtual\n", phy_bits, vir_bits);
    
    return 0;
}