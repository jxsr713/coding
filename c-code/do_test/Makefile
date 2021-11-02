CC = gcc
CFLAGS = -wall -O -g
SOURCE_FILES = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SOURCE_FILES))
TARGET = c_code

$.o : %.c %.h
	$(CC) -c $(CFLAGS) $< -o $@


$.o : %.c
	$(CC) -c $(CFLAGS) $< -o $@

$(TARGET) : $(OBJS)
	$(CC) $^ -o $@

.PHONY:clean
	
clean:
	rm -rf $(TARGET) $(OBJS)


