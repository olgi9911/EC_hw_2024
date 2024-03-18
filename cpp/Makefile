CXX = g++
CXXFLAGS = --std=c++17 -O3 -Wall
SRC = main.cpp parser.cpp ga.cpp
TARGET = hw_sch

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
