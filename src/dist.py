import json
import subprocess
import sys

# Load the JSON data from logs/test_result.json into a dictionary
with open('logs/test_result.json', 'r') as file:
    test_result = json.load(file)

# Check if the "percent_correct" is greater than or equal to 97.0
if test_result.get("percent_correct", 0) >= 97.0:
    try:
        # Execute the src/build_dist.sh script
        subprocess.run(['bash', 'src/build_dist.sh'], check=True)
        print("Build script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the build script: {e}")
else:
    # Raise an error if the condition is not met
    raise ValueError(f"Test result does not meet the required threshold: {test_result['percent_correct']}%")
