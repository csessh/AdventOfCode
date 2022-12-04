
SRC_FILES = $(wildcard *cpp)
OBJ_FILES = $(patsubst %.cpp, %.o, $(SRC_FILES))
BIN_FILES = $(patsubst %.cpp, %, $(SRC_FILES))

CFLAG := -g -Wall -Werror -O2 -std=c++14

all: $(BIN_FILES)

$(BIN_FILES): %: %.o
	g++ $(CFLAG) $< -o bin/$@

$(OBJ_FILES): %.o: %.cpp
	g++ $(CFLAG) -c $<

clean:
	rm -f *.o bin/*