ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell uname -s)
endif

CXX := g++
ifeq ($(detected_OS),Windows)
    CXX := g++
    CXXFLAGS := --std=c++17 -O3 -Wall
else
    CXXFLAGS := --std=c++17 -O3 -Wall
endif

SRC := main.cpp parser.cpp ga.cpp
TARGET := main
OBJ := $(SRC:.cpp=.o)

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
ifeq ($(detected_OS),Windows)
	del /f /q $(OBJ) $(TARGET).exe
else
	rm -f $(TARGET)
# rm -f $(OBJ) $(TARGET)
endif

.PHONY: all clean
