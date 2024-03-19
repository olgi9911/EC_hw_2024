import subprocess
import numpy as np
import os

test_num = 30

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def run_test(executable, args):
    process = subprocess.run([executable] + args, capture_output=True, text=True)
    return float(process.stdout.strip())

def test_student_code(test_input_file, test_output_file, executable):
    with open(test_input_file, 'r') as f:
        params = f.readline().strip().split()

    with open(test_output_file, 'r') as f:
        expected_mean = float(f.readline().strip())
        expected_std_dev = float(f.readline().strip())

    fitness_values = [run_test(executable, params) for _ in range(test_num)]

    calculated_mean = np.mean(fitness_values)

    lower_bound = expected_mean - 2 * expected_std_dev
    upper_bound = expected_mean + 2 * expected_std_dev
    if lower_bound <= calculated_mean <= upper_bound:
        result = f"{test_input_file:<10} {GREEN}Correct{RESET}"
        # print(f"Test {test_input_file}: {result} (Calculated Mean: {calculated_mean}, Expected Mean: {expected_mean}, Std Dev: {expected_std_dev})")
    else:
        result = f"{test_input_file:<10} {RED}Wrong (Calculated Mean: {calculated_mean}, Expected Mean: {expected_mean}, Std Dev: {expected_std_dev}){RESET}"
        # print(f"Test {test_input_file}: {result} (Calculated Mean: {calculated_mean}, Expected Mean: {expected_mean}, Std Dev: {expected_std_dev})")
    print(result)

executable = ".main" if os.path.exists("./main") else "python3 main.py"

for i in range(1, 11):
    test_input_file = f"testcase/{i:02d}.in"
    test_output_file = f"testcase/{i:02d}.out"
    test_student_code(test_input_file, test_output_file, executable)
