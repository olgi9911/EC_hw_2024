# EC_hw_2024
**If you encounter any issues or have any questions regarding this repository, please don't hesitate to open an issue!**
## Sample Code Usage
Clone this repository to local,
```bash
git clone https://github.com/fffchameleon/EC_hw_2024.git
cd EC_hw_2024
```
If you will write this assignment with C++,
```bash
cd cpp/ && make
./main -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 100 -d
```
If you prefer to use Python, use,
```bash
cd py
python3 main.py -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500 -d
```
Both should print the following,
```
-------------------------------------------
|Parameter           |Value               |
-------------------------------------------
|dimension           |10                  |
|representation      |binary              |
|population_size     |100                 |
|uniform_crossover   |false               |
|crossover_method    |2-point             |
|cross_prob          |0.9                 |
|mut_prob            |0.1                 |
|num_generations     |500                 |
-------------------------------------------
0.00145984
```
## Input/Output Format
We provide sample parser code for two languages (C++/Python). 

You can write your own parser, but it must be capable of accepting the following parameters, and your program must provide at least the following 8 options. 

p.s. You may add more options to make your experiments more convenient and complete.

| Options       | Description | Default |
| ------------- | ----------- | ------- |
| `-n, --dimension` | The dimension of Schwefel function | 10 |
| `-r, --representation`    | The representation to use. Binary or real-valued (binary, real) | binary |
| `-p, --population_size`	  |  Number of the population |100 |
| `-u, --uniform_crossover`  | The crossover method using uniform crossover (1) or not (0). If not, then for binary GA, it will use 2-point crossover and for real-valued GA will use whole arithmetic crossover | 0 |
| `-c, --pc` |	Probability for the crossover | $p_c$=0.9 |
| `-m, --pm` |	Probability for the mutation  |  $p_m$=0.1 |
| `-g, --generations`  |  Max number of generations to terminate | 500 |
| `-d, --debug`        | Turn on debug prints | false |

### Input
For example, with `testcase/01.in`, our judger will execute your executable file + the first line of configuration in `testcase/*.in`.

If written in C++, please remember to upload a Makefile, and the compiled executable should be named main.
```bash
./main -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 100
```
If written in Python, your main.py file will be executed directly.
```bash
python3 ./main.py -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 100
```
The following context is `01.in`. 
1. The first line contains the parameters we will use for testing
2. The second line is a configuration table. If you do not use `-d` or `--debug`, it will not be printed.
```
-n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 100
-------------------------------------------
|Parameter           |Value               |
-------------------------------------------
|dimension           |10                  |
|representation      |binary              |
|population_size     |100                 |
|uniform_crossover   |false               |
|crossover_method    |2-point             |
|cross_prob          |0.9                 |
|mut_prob            |0.1                 |
|num_generations     |100                 |
-------------------------------------------
```
### Output
**Remember, when uploading your code, ensure that your code only print the configuration table when -d, --debug is added.**

Please directly print the best fitness of the final generation.

For example, with `01.in`, suppose I finally find the best solution `421 421 421 421 421 421 421 421 421 421`, and the fitness of my solution is 0.00145984.
Then just print 0.00145984.
- Sample output:
  In `testcase/*.out`, the first line contains two values: the first value is the mean best fitness running by TAs with 100 trials, and the second value is the standard deviation.
  If your fitness is within two standard deviations, it is considered correct.
## Grading 
- Coding (30%)
  - Simple test: each failed testcase deducts 1 point (10%)
  - Parent Selection (3%)
  - Crossover (8%)
  - Mutation (6%)
  - Survivor Selection (3%)
  - Penalty
    - Compilation failure with Makefile (-5)
    - Not following input/output format (-5)
    - Incorrect filename (-3)
- Report (70%)
