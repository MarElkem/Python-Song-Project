# Analysis of Name Trends in Songs

## Overview

This Python project provides a collection of functions to analyze name occurrences in songs, leveraging a dataset that lists songs with specific names. The functions cover a variety of tasks from finding specific names in songs to analyzing the popularity of name initials over decades. The code is structured to efficiently process and summarize large datasets using pandas.

## Features

- **Name Search**: Locate all songs containing a specific name.
- **Repeat Names Analysis**: Identify names that appear frequently across different of songs.
- **Unique Names in Songs**: Find songs with a high count of unique names.
- **Decade Frequency Analysis**: Analyze the frequency of names across different decades.
- **Initial Letter Frequency Analysis**: Compute the frequency of the initial letters of names in songs.
- **Final Letter Frequency Analysis**: Assess the distribution of the final letters of names in songs.

## Files

- `main.py`: Main script containing all the function definitions and the main execution logic.
- `allNames.csv`: Primary dataset used for the analysis. *(Note: This file should be placed in the project directory for the scripts to function correctly.)*

## Setup and Execution

1. Ensure that Python and pandas are installed on your system.
2  Place the `allNames.csv` data file in the same directory as the script.
3. Run the script from the command line:
   ```bash
   python main.py
