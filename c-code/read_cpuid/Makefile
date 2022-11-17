CC = gcc
CFLAGS = -Wall -O -g
SOURCE_FILES = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SOURCE_FILES))
TARGET = cpuid rd_cpuid-1 rd_cpuid-2
#TARGET = check_feature

#$.o : %.c %.h
#	$(CC) -c $(CFLAGS) $< -o $@
all: $(TARGET)
	echo $(SOURCE_FILES)
	echo $(OBJS)


check_feature : check_feature.c
	  $(CC) -o check_feature check_feature.c


$.o : %.c
	echo "$(CC) -c $(CFLAGS) $< -o $@"
#	$(CC) -c $(CFLAGS) $< -o $@

$(TARGET) : $(OBJS)
	echo "===$(CC) $^ -o $@"
	$(CC) $^ -o $@

.PHONY:clean

clean:
	rm -rf $(TARGET) $(OBJS)


