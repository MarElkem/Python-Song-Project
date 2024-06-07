import csv
import pandas as pd
# This function finds the songs that contain the given name and writes the result to an output file
def findName(name,outputFile):
  # Read the CSV file using Pandas
  df = pd.read_csv('allNames.csv', sep='\t')

  # Filter out to find the given name
  df = df[df['name'] == name]

  # Drop duplicate rows in the dataframe
  df = df.drop_duplicates()

  # Save the resulting dataframe to a CSV file
  df.to_csv(outputFile, columns=['song', 'artist', 'year'])
def main():
    findName("Mary", "tests/mary.csv")
    findName("Jack", "tests/jack.csv")
    findName("Peter", "tests/peter.csv")
if __name__=="__main__":
    main()       