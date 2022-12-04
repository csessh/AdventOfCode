all: day1 day2 day3

day1: day1.o
	g++ day1.o -o bin/day1

day2: day2.o
	g++ day2.o -o bin/day2

day3: day3.o
	g++ day3.o -o bin/day3

day1.o: day1.cpp
	g++ -std=c++20 -c day1.cpp

day2.o: day2.cpp
	g++ -std=c++20 -c day2.cpp

day3.o: day3.cpp
	g++ -std=c++20 -c day3.cpp

clean:
	rm -f *.o bin/*