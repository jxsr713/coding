#CFLAGS := -lpthread

LDFLAGS := -lpthread
CFLAGS := -Wall -g -lpthread

BINS := data-link
OBJS := data-link.o

all : $(BINS)

$(BINS) : $(OBJS)
	@echo "===== $(CC) -o $@ $^ "
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	        rm -f data-link *.o



