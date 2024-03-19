CXX = g++
CXXFLAGS = --std=c++17 -O3 -Wall
SRC = main.cpp parser.cpp ga.cpp
TARGET = main

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
