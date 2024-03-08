import subprocess
import sys
import os
import shutil
import platform

# User-configurable variable for Allure command path
# Windows example: r'C:\Path\To\Allure\bin\allure.bat'
# macOS/Linux example: '/usr/local/bin/allure'
ALLURE_COMMAND_PATH = None

def find_allure_executable():
    if ALLURE_COMMAND_PATH and os.path.exists(ALLURE_COMMAND_PATH):
        return ALLURE_COMMAND_PATH
    elif platform.system().lower() == 'windows':
        default_name = 'allure.bat'
    else:
        default_name = 'allure'
    for path in os.environ["PATH"].split(os.pathsep):
        allure_path = os.path.join(path, default_name)
        if os.path.exists(allure_path):
            return allure_path
    raise FileNotFoundError(f"{default_name} not found in the system's PATH. Please ensure Allure is installed and added to PATH or set ALLURE_COMMAND_PATH in the script.")

def clear_directory(directory):
    """Clears the specified directory by removing it if it exists, then recreating it."""
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def open_allure_report():
    report_dir = "allure-report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    # Use find_allure_executable to get the path to the Allure command
    subprocess.call([find_allure_executable(), 'serve', 'allure-results'])

def generate_allure_report():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    report_dir = os.path.join(base_dir, "allure-report")
    # Use find_allure_executable to get the path to the Allure command
    subprocess.call([find_allure_executable(), 'generate', results_dir, '-o', report_dir, '--clean'])

def run_tests_and_generate_report(headless=False):
    # Define the base directory for reports relative to this script's location
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    # Clear the allure-results directory to ensure fresh start
    clear_directory(results_dir)
    # Ensure the allure-report directory is cleared and ready for new report
    clear_directory(os.path.join(base_dir, "allure-report"))
    # Determine headless mode
    pytest_cmd = ['pytest', f'--alluredir={results_dir}']
    if headless:
        pytest_cmd.extend(['--headless'])
    # Run pytest with or without headless mode based on the headless argument
    subprocess.call(pytest_cmd)
    # Automatically generate the Allure report after tests have completed
    generate_allure_report()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'openReport':
            open_allure_report()
        elif command == 'testHeadless':
            run_tests_and_generate_report(headless=True)
        elif command == 'testNormal':
            run_tests_and_generate_report(headless=False)
        else:
            print(f"Unknown command: {command}")
    else:
        print("No command provided.")