import pandas as pd
 
def findUniqueNameSongs(thresh, outputFile):
    # Read the CSV file using Pandas
    df = pd.read_csv("allNames.csv", sep="\t")
 
    # Group the rows by artist and song and count the number of unique names anilter out the rows with less than the specified number of unique names

    df = df[['artist', 'song', 'name']].groupby(["artist", "song"]).nunique()
    df = df[df['name'] > thresh]
 

    # Save the resulting dataframe to a CSV file
    df.to_csv(outputFile)


def main():
  findUniqueNameSongs(15, "tests/unique.15.csv")
  findUniqueNameSongs(20, "tests/unique.20.csv")

  
if __name__=="__main__":
    main() 
