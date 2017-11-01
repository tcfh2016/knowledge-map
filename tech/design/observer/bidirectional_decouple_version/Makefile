CC = g++
CFLAGS = -g -c

all:subject.o main.o target

subject.o : subject.hpp subject.cpp
	$(CC) $(CFLAGS) $^

main.o : secretary.hpp boss.hpp stockobserver.hpp nbaobserver.hpp main.cpp
	$(CC) $(CFLAGS) $^

target : subject.o main.o
	$(CC) $^ -o $@

clean :
	rm subject.o main.o
