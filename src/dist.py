import json
import subprocess
import sys
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Check if percent_correct meets a threshold and execute a build script if it does.")
parser.add_argument('--threshold', type=float, default=50.0, help='The percentage threshold to check against.')

# Parse the arguments
args = parser.parse_args()

# Load the JSON data from logs/test_result.json into a dictionary
with open('logs/test_result.json', 'r') as file:
    test_result = json.load(file)

# Check if the "percent_correct" is greater than or equal to the specified threshold
if test_result.get("percent_correct", 0) >= args.threshold:
    try:
        # Execute the src/build_dist.sh script
        subprocess.run(['bash', 'src/build_dist.sh'], check=True)
        print("Build script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the build script: {e}")
else:
    # Raise an error if the condition is not met
    raise ValueError(f"Test result does not meet the required threshold: {test_result['percent_correct']}%")
