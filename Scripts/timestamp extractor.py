import os
import csv

# Get the current directory
current_dir = os.getcwd()

# Find all CSV files in the current directory
csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]

# Print the list of CSV files with their corresponding numbers
print("Available CSV files:")
for i, file in enumerate(csv_files, start=1):
    print(f"{i}. {file}")

# Prompt the user to select a file
file_choice = int(input("Enter the number of the CSV file you want to process: "))

# Get the selected file name
selected_file = csv_files[file_choice - 1]

def extract_info(row):
    note = row['Notes']
    timestamp = row['Record In']
    if note and timestamp:
        # Extract the minutes and seconds from the timestamp
        time_parts = timestamp.split(':')
        minutes, seconds = time_parts[1], time_parts[2]
        time_str = f"{minutes}:{seconds}"
        return f"{note} {time_str}"

with open(selected_file, 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = list(reader)

results = []
for row in data:
    result = extract_info(row)
    if result:
        results.append(result)

# Print the results to the console
print("\nResults:")
for result in results:
    print(result)

# Prompt the user to enter a filename for the output
output_filename = input("\nEnter a filename for the output (e.g., output.txt): ")

# Open the output file in write mode
with open(output_filename, 'w') as output_file:
    # Write each result to the output file
    for result in results:
        output_file.write(result + '\n')

print(f"Results have been written to {output_filename}")