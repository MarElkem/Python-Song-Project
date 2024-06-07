import pandas as pd

#1 
# This function finds the songs that contain the given name and writes the result to an output file
def findName(name,outputFile):
  # Read the CSV file using Pandas
  df = pd.read_csv('allNames.csv', sep='\t')

  # Filter out to find the given name
  df = df[df['name'] == name]

  # Drop duplicate rows in the dataframe
  df = (df.drop_duplicates()
  .sort_values(by = "artist")
  .astype({"year":"int64"})) #Get rid of decimals in years

  # Save the resulting dataframe to a CSV file
  df.to_csv(outputFile, columns=['song', 'artist', 'year'])

#6 lines vs 14 

#2 
def repeatnames(threshold, outputfile):
  file = pd.read_csv("allNames.csv", sep = "\t")
  file = (file[file["nonPerson"].isna()][["artist", "song", "name", "highestRank"]]
  .groupby(["artist", "song", "name"])
  .count())
  file =(file[file["highestRank"] >= threshold]
  .rename(columns = {"highestRank":"times"})
  .sort_values(by = "times", ascending = False))
  file.to_csv(outputfile)
#9 lines vs 21 

  #3
def findUniqueNameSongs(thresh, outputFile):
    # Read the CSV file using Pandas
    df = pd.read_csv("allNames.csv", sep="\t")

    # Group the rows by artist and song and count the number of unique names and filter out the rows with less than the specified number of unique names
    df = df[['artist', 'song', 'name']].groupby(["artist", "song"]).nunique()
    df = df[df['name'] >= thresh]

    # Sort the dataframe in descending order of the number of unique names
    df = df.sort_values(by='name', ascending=False)

    # Save the resulting dataframe to a CSV file
    df.to_csv(outputFile)
#6 lines vs 20 
  #4 
def countNameDecades(name, outputfile):
  file = pd.read_csv("allNames.csv", sep = "\t", parse_dates = True)
  file["decade"] = (file["year"] - file['year']%10)
  file = (file.query("year > 1969 and nonPerson.isna() and name ==    @name")
  .astype({"decade":"int64"}) #removing decimals
  .groupby(["decade"])[["decade", "year"]]
  .count()
  .rename(columns = {"year":"count"})["count"])
  file.to_csv(outputfile)


#9 lines vs 21 

# 5
def getFirstLetterFreq(data, sep = ","):
  # Read the data file using pandas
  file = pd.read_csv(data, sep = sep)

  # Select the "name" column, drop duplicates, and sort the values
  namesInfo = (file[["name"]]
  .drop_duplicates() 
  .sort_values(by="name"))

  # Create a new column called "firstLetter" with the first letter of each name
  namesInfo["firstLetter"]=namesInfo["name"].str[0]

  # Group the names by first letter and calculate the number of names in each group
  letterInfo = (namesInfo
  .groupby(["firstLetter"], as_index=False)
  .count())

  # Rename the "name" column to "num"
  letterInfo.rename(columns={"name":"num"}, inplace=True)

  # Calculate the frequency of each letter by dividing the number of names by the total number of names
  letterInfo["freq"] = letterInfo["num"]/letterInfo["num"].sum()*100

  # Return the result as a dataframe with the first letter and frequency columns
  return letterInfo[["firstLetter","freq"]]

# This function calculates the difference in the frequency of the first letters
# of names in two data files and writes the result to an output file
def countStartLetter(outputfile):
  # Calculate the frequency of the first letters in the "allNames" file
  freqAllNames = getFirstLetterFreq("allNames.csv", sep = "\t")

  # Calculate the frequency of the first letters in the "onlyNames" file
  freqOnlyNames = getFirstLetterFreq("onlyNames.csv", sep = "\t")

  # Merge the two dataframes on the "firstLetter" column
  allFreqs=pd.merge(freqAllNames, freqOnlyNames,how="inner",
                    on="firstLetter")

  # Calculate the difference between the two frequencies
  allFreqs["diff"] = (allFreqs["freq_x"] - allFreqs["freq_y"]).round(2)

  # Write the result to the output file, including only the "firstLetter" and "diff" columns
  allFreqs.to_csv(outputfile, index = False, columns =
                 ["firstLetter", "diff"])


#countStartLetter("name.start.csv")
def getLastLetterFreq(data):
  file = pd.read_csv(data, sep = "\t")
  namesInfo = (file[["name"]]
  .drop_duplicates() 
  .sort_values(by="name"))
  namesInfo["lastLetter"]=namesInfo["name"].str[-1] #taking the last part of the string 
  letterInfo = (namesInfo
  .groupby(["lastLetter"], as_index=False)
  .count())
  letterInfo.rename(columns={"name":"num"}, inplace=True)
  letterInfo["freq"] = letterInfo["num"]/letterInfo["num"].sum()*100
  letterInfo = (letterInfo[["lastLetter","freq"]]
  .set_index("lastLetter")) #this turns letters into the column, and lets us manipulate it, using loc
  if data == "allNames.csv": #adding missing letters in allNames 
    letterInfo.loc["j"] = 0 
    letterInfo.loc["q"] = 0
  letterInfo.loc["v"] = 0
  return letterInfo
  
def countEndLetter(outputfile):
  freqAllNames = getLastLetterFreq("allNames.csv")
  freqOnlyNames = getLastLetterFreq("onlyNames.csv")
  allFreqs=pd.merge(freqAllNames, freqOnlyNames,how="inner",
                    on="lastLetter")
  allFreqs = allFreqs.sort_values(by = "lastLetter")
  allFreqs["diff"] = (allFreqs["freq_x"] - 
  allFreqs["freq_y"]).round(2)
  allFreqs.to_csv(outputfile, columns =
                 ["diff"])

#47 lines vs 87 

def main():
  
  #1
  findName("Mary", "tests/mary.csv")
  findName("Jack", "tests/jack.csv")
  findName("Peter", "tests/peter.csv")
  #2 
  repeatnames(20, "tests/repeat.20.csv")
  repeatnames(30, "tests/repeat.30.csv")
  repeatnames(40, "tests/repeat.40.csv")
  #3
  findUniqueNameSongs(15, "tests/unique.15.csv")
  findUniqueNameSongs(20, "tests/unique.20.csv")
  #4
  countNameDecades('Joe', "tests/joe.decades.csv")
  countNameDecades('Mary', "tests/mary.decades.csv")
  countNameDecades('Jesus', "tests/jesus.decades.csv") #our name of choice is Jesus because it is a really cool name 
  #5 
  countEndLetter("tests/names.end.csv")
  countStartLetter("tests/names.start.csv")
if __name__=="__main__":
    main() 
