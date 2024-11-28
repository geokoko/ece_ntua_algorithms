import subprocess
import sys
import os
import filecmp
import glob

def run_tests(program_name):
    INPUT_FILES = f"{program_name}_tests/input*.txt"
    OUTPUT_FILES = f"{program_name}_tests/output*.txt"
    RESULTS_DIR = f"{program_name}_tests/actual_results"

    os.makedirs(RESULTS_DIR, exist_ok=True)

    input_files = sorted(glob.glob(INPUT_FILES), key=lambda x: int(os.path.basename(x).split("input")[1].split(".")[0]))
    output_files = sorted(glob.glob(OUTPUT_FILES), key=lambda x: int(os.path.basename(x).split("output")[1].split(".")[0]))

    if not input_files or not output_files:
        print(f"❌ No test files found for {program_name}!")
        return

    if len(input_files) != len(output_files):
        print(f"❌ Mismatch in number of input and output files for {program_name}!")
        sys.exit(1)

    all_passed = True  # Start assuming all tests will pass

    for input_file, expected_output_file in zip(input_files, output_files):
        test_number = os.path.basename(input_file).split(".")[0].split("input")[1]
        actual_output_file = os.path.join(RESULTS_DIR, f"output{test_number}.txt")

        print(f"Running test {test_number} for {program_name}...")
        try:
            with open(input_file, "r") as infile, open(actual_output_file, "w") as outfile:
                subprocess.run([f"./{program_name}.o"], stdin=infile, stdout=outfile, check=True)

            if filecmp.cmp(expected_output_file, actual_output_file, shallow=False):
                print(f"  ✅ Test {test_number} passed!")
            else:
                print(f"  ❌ Test {test_number} failed!")
                print(f"     Expected output: {expected_output_file}")
                print(f"     Actual output: {actual_output_file}")
                all_passed = False

        except subprocess.CalledProcessError:
            print(f"  ❌ Test {test_number} failed to execute!")
            all_passed = False
        except FileNotFoundError:
            print(f"  ⚠️ File not found for {program_name}. Ensure {input_file} or {expected_output_file} exists.")
            sys.exit(1)

    if all_passed:
        print(f"✅ All tests passed for {program_name}!")
    else:
        print(f"❌ Some tests failed for {program_name}.")

# Run tests for each program
run_tests('linemarket')
run_tests('bicriteriamst')

