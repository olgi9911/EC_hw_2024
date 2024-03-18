#include "parser.h"
// #include "config.h"
#include "ga.h"
#include <iostream>

int main(int argc, char *argv[]) {
    Configuration config;
    
    if (parse_cmd(argc, argv, config)) {
        std::cerr << "Error when parsing.\n";
        return 0;
    }
    if (config.debug) {
        config.print_configuration();
    }
    // TODO: write your GA program
    // GA(config);
    
    return 0;
}
