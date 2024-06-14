import os
from typing import List, Dict, Optional
import csv

def find_csv_files(directory: str) -> List[str]:
    """Find all CSV files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def extract_info(row: Dict[str, str]) -> Optional[str]:
    """Extract the note and timestamp from the given row."""
    note = row['Notes']
    timestamp = row['Record In']
    if note and timestamp:
        try:
            time_parts = timestamp.split(':')
            minutes, seconds = time_parts[1], time_parts[2]
            time_str = f"{minutes}:{seconds}"
            return f"{note} {time_str}"
        except (IndexError, ValueError):
            # Handle cases where the timestamp format is different from the expected format
            return f"{note} {timestamp}"
    return None

def process_csv_file(file_path: str) -> List[str]:
    """Process the given CSV file and extract notes with timestamps."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        data = list(reader)

    results = [extract_info(row) for row in data]
    return [result for result in results if result]

def main() -> None:
    # Get the current directory
    current_dir = os.getcwd()

    # Find all CSV files in the current directory
    csv_files = find_csv_files(current_dir)

    selected_file = None
    while selected_file is None:
        # Print the list of CSV files with their corresponding numbers
        print("Available CSV files:")
        for i, file in enumerate(csv_files, start=1):
            print(f"{i}. {file}")
        print("0. Exit")

        # Prompt the user to select a file or exit
        choice = input("Enter the number of the CSV file you want to process (or 0 to exit): ")
        if choice == '0':
            return
        try:
            file_choice = int(choice)
            if 1 <= file_choice <= len(csv_files):
                selected_file = csv_files[file_choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        # Process the selected file
        results = process_csv_file(selected_file)

        # Print the results to the console
        print("\nResults:")
        for result in results:
            print(result)

        # Prompt the user for the next action
        choice = input("\nEnter 1 to go back to the CSV file list, 2 to perform file output, or 3 to exit: ")

        if choice == '1':
            # Go back to the CSV file list
            selected_file = None
            break
        elif choice == '2':
            # Perform file output
            output_filename = input("\nEnter a filename for the output (e.g., output.txt): ")
            with open(output_filename, 'w') as output_file:
                for result in results:
                    output_file.write(result + '\n')
            print(f"Results have been written to {output_filename}")
        elif choice == '3':
            # Exit the program
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()