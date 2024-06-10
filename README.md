# Timestamp Extractor

This Python script allows you to extract timestamps and notes from CSV files containing video editing data from DaVinci Resolve. The script provides a user-friendly interface for selecting a CSV file from the current directory, processing the data, and optionally generating an output file with the desired information.

## Features

- List available CSV files in the current directory
- Select a CSV file to process
- Extract timestamps and notes from the selected file
- Strip unnecessary characters from timestamps (e.g., hours, frames)
- Combine notes and stripped timestamps into a formatted string
- Print the results to the console
- Optionally generate an output file with the extracted information

## Usage

1. Create a folder for the CSV files.
2. Place the executable within this folder.
3. Export Edit Index CSV files to this folder.
4. Select the CSV file you want to process from the list of available files
5. Enter a filename for the output file (e.g., `output.txt`)
6. The script will process the selected CSV file and generate the output file in the same directory

![Step 1](https://i.imgur.com/61Zdtsa.png)
![Step 2](https://i.imgur.com/A1GzcdI.png)
![Step 3](https://i.imgur.com/1lHH7OO.png)

## Requirements

- If running the script, Python 3.x
- No external dependencies

## How to Export Timestamps CSV in DaVinci

- Video Guide Coming Soon
![Export CSV](https://i.imgur.com/qw3xKwr.png)

- Use a consistent marker color for timeline chapters. I personally use RED markers. Red for YouTube. How original.
- Enable the Index Pane in DaVinci Resolve
- Click the 3 horizontal dots in the top right corner of the Index Pane
- Hover over "Show Markers"
- Choose the marker color that represents your chapter markers
- Once more click the 3 horizontal dots
- Select Export Edit Index at the very bottom of the list.
- Save this file within the same folder/directory as the .exe or script files.

## Notes

I have included an example timestamp CSV file which you can test from.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
