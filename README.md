# EC_hw_2024
**If you encounter any issues or have any questions regarding this repository, please don't hesitate to open an issue!**
## Latest Announcement
1. (3/25) When you run judger, please set 0.2 instead of 0.5 as the alpha of whole arithmetic. But you can test other values as your experiment and write the result and analysis in your report.
2. (3/24) The `testcase/*.out` is released, and here's a typo in `09.in` and `judger.py`, please pull the new version using:
    ```bash
    git pull origin main
    ```

#### Archived Announcement
(3/19) The release of `testcase/*.out` files will be delayed. Expected upload date: March 24.

## Sample Code Usage
Clone this repository to your local machine,
```bash
git clone https://github.com/fffchameleon/EC_hw_2024.git
cd EC_hw_2024
```
If you choose to write this assignment in C++,
```bash
cd cpp/ && make
./main -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500 -d
```
If you prefer to use Python, use,
```bash
cd py
python3 main.py -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500 -d
```
Both commands should output the following information,
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
./main -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500
```
If written in Python, your main.py file will be executed directly.
```bash
python3 ./main.py -n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500
```
The following context is `01.in`. 
1. The first line contains the parameters we will use for testing
2. The second line is a configuration table. If you do not use `-d` or `--debug`, it will not be printed.
```
-n 10 -r binary -p 100 -u 0 -c 0.9 -m 0.1 -g 500
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
```
### Output
**Remember, when uploading your code, ensure that your code only print the configuration table when -d, --debug is added.**

Please directly print the best fitness of the final generation.

For example, with `01.in`, suppose I finally find the best solution `430 420 419 432 426 419 415 417 414 429`, and the fitness of my solution is 50.5991.
Then just print 50.5991.
- Sample output:

  In `testcase/*.out`, the first line contains two values: the first value is the mean best fitness running by TAs with 120 trials, and the second value is the standard deviation.
  
  We will run your code for 30 trials and if your mean fitness is within two standard deviations, it is considered correct. 
#### Judger Usuage
Place your executable and the judger in the same directory, and run them using `python3 judger.py`. 

It may take a long time to run judge (each testcse will run 30 trials), so be patient!

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
      - executable file: main or main.py
      - report: report.pdf

- Report (70%)