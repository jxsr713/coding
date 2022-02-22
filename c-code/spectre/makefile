CFLAGS = -std=c99

PROGRAM = spectre spectreAttack
SOURCE  = spectre.c
     
all: $(PROGRAM)
     
#$(PROGRAM): $(SOURCE) ; 
#	$(CC) $(CFLAGS) -g -o $(PROGRAM) $(SOURCE)

$(all):
	$(CC) $(CFLAGS) -g -o $@ $<

clean: ; rm -f $(PROGRAM)
