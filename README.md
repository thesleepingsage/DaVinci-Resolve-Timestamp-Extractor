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

## Download

### <p align='center'> Windows Version <br> <p align='center'> [<img src="https://img.shields.io/badge/Free-Download-blue?style=plastic&logo=windows&logoColor=white&label=Free" width="300">](https://github.com/thesleepingsage/DaVinci-Resolve-Timestamp-Extractor/releases/download/v2.5/Release_Windows.zip)</p>

### <p align='center'> macOS Version <br> <p align='center'> [<img src="https://img.shields.io/badge/Free-Download-blue?style=plastic&logo=apple&logoColor=white&label=Free" width="300">](https://github.com/thesleepingsage/DaVinci-Resolve-Timestamp-Extractor/releases/download/v2.5/Release_macOS.zip)</p>

### <p align='center'> **SOURCE CODE** <br> <p align='center'> [<img src="https://img.shields.io/badge/Python_Version-informational?style=flat&logo=python&logoColor=blue&color=eaea4a" width=200 height=40>](hhttps://github.com/thesleepingsage/DaVinci-Resolve-Timestamp-Extractor/releases/download/v2.5/Scripts.zip)</p>

### Don't forget to leave a ⭐

## How to Export Timestamps CSV in DaVinci Resolve

- Video Guide Coming Soon
![Export CSV](https://i.imgur.com/qw3xKwr.png)

- Use a consistent marker color for timeline chapters. I personally use RED markers. Red for YouTube. How creative.
1. Enable the Index Pane in DaVinci Resolve
2. Click the 3 horizontal dots in the top right corner of the Index Pane
3. Hover over "Show Markers"
4. Choose the marker color that represents your chapter markers
5. Once more click the 3 horizontal dots
6. Select Export Edit Index at the very bottom of the list.
7. Save this file within the same folder/directory as the .exe or script files.

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

## Example CSV

I have included an example timestamp CSV file which you can test from.

## Requirements

- If running the script, Python 3.x
- No external dependencies

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Disclaimer

This software is provided free of charge on an as-is basis. Any monetary contributions made in relation to this software are considered voluntary donations and do not constitute a sale or purchase. The author retains all rights to the software and make no warranties, express or implied, regarding its use or performance.

## Donations

While this software is distributed free of charge, voluntary contributions are appreciated. If you find this project valuable and wish to make a donation, please visit: https://ko-fi.com/s/35e059b0ac

Please note that donations are entirely optional and do not confer any additional rights, privileges, or entitlements with respect to the software. All contributions are gratefully acknowledged.

## License

This project is licensed under the [MIT License](LICENSE).