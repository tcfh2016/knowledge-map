CC = g++
CFLAGS = -g -c

all:calculator.o target

calculator.o : calculator.cpp
	$(CC) $(CFLAGS) $^

target : calculator.o
	$(CC) $^ -o $@

clean:
	rm calculator.o target

