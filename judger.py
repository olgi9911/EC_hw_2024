import sys
import subprocess
import os
import glob

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def calculate_rmse(sample_answer, your_answer, rmse_limit):
    try:
        sample_answer_list = [float(num) for num in sample_answer.split()]
        your_answer_list = [float(num) for num in your_answer.split()]
    
        if len(sample_answer_list) != len(your_answer_list):
            return False, 0, "The number of elements in sample answer and your answer do not match."
    
        square_differences = [(a - b) ** 2 for a, b in zip(sample_answer_list, your_answer_list)]
        mean_square_difference = sum(square_differences) / len(square_differences)
        rmse = mean_square_difference ** 0.5
        
        if rmse <= rmse_limit:
            return True, rmse, ""
        else:
            return False, rmse, f"FAIL: RMSE is {rmse}, exceeds the limit of {rmse_limit}."
    except ValueError as e:
        return False, 0, f"Error: {e}"

def run_testcase(executable, testcase_input):
    with open(testcase_input, 'r') as f:
        first_line = f.readline().strip()
    process = subprocess.run(executable + ' ' + first_line, shell=True, capture_output=True, text=True)
    output = process.stdout.strip()
    return output

def main(language):
    if language not in ['cpp', 'py']:
        print(f"{RED}Invalid argument. Please specify 'cpp' or 'py'.{RESET}")
        return

    if language == 'cpp':
        os.system('make clean -C cpp/')
        os.system('make -C cpp/')
        executable = './cpp/hw_sch'
    else:
        executable = 'python python/main.py'

    testcases_in = sorted(glob.glob('testcase/*.in'))
    testcases_out = sorted(glob.glob('testcase/*.out'))

    for in_file, out_file in zip(testcases_in, testcases_out):
        your_output = run_testcase(executable, in_file)
        
        with open(out_file, 'r') as f:
            lines = f.readlines()
            sample_output = lines[0].strip()
            rmse_limit_line = lines[-1]
            rmse_limit = float(rmse_limit_line.split(':')[-1].strip())
        
        pass_fail, rmse, message = calculate_rmse(sample_output, your_output, rmse_limit)
        
        if pass_fail:
            print(f"{os.path.basename(in_file):<10} {GREEN}pass{RESET}")
        else:
            print(f"{os.path.basename(in_file):<10} {RED}fail (RMSE is {rmse}, {message}){RESET}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python judge.py [cpp/py]")
    else:
        main(sys.argv[1])
