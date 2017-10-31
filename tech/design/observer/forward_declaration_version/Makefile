CC = g++
CFLAGS = -g -c

all:secretary.o stockobserver.o main.o target

secretary.o : secretary.hpp secretary.cpp
	$(CC) $(CFLAGS) $^

stockobserver.o : stockobserver.hpp stockobserver.cpp
	$(CC) $(CFLAGS) $^

main.o : secretary.hpp stockobserver.hpp main.cpp
	$(CC) $(CFLAGS) $^

target : secretary.o stockobserver.o main.o
	$(CC) $^ -o $@

clean :
	rm secretary.o stockobserver.o main.o
