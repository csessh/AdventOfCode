
SRC_FILES = $(wildcard *cpp)
OBJ_FILES = $(patsubst %.cpp, %.o, $(SRC_FILES))
BIN_FILES = $(patsubst %.cpp, %, $(SRC_FILES))

INCLUDES = $(wildcard include/*cpp)
INC_OBJ_FILES = $(patsubst %.cpp, %.o, $(INCLUDES))

CFLAG := -g -Wall -Werror -O2 -std=c++14

all: $(BIN_FILES)

$(BIN_FILES): %: %.o helper.o
	g++ $(CFLAG) $< helper.o -o bin/$@

$(OBJ_FILES): %.o: %.cpp
	g++ $(CFLAG) -c $< -I include

$(INC_OBJ_FILES) %.o: include/%.cpp
	g++ $(CFLAG) -c $<

clean:
	rm -f *.o bin/*