CC = g++
CFLAGS = -g -c

all:secretary.o main.o target

secretary.o : secretary.hpp secretary.cpp
	$(CC) $(CFLAGS) $^

main.o : secretary.hpp stockobserver.hpp nbaobserver.hpp main.cpp
	$(CC) $(CFLAGS) $^

target : secretary.o main.o
	$(CC) $^ -o $@

clean :
	rm secretary.o main.o
