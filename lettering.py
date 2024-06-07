
def getFirstLetterFreq(data, sep = ","):
  file = pd.read_csv(data, sep = sep)
  namesInfo = (file[["name"]]
  .drop_duplicates() 
  .sort_values(by="name"))
  namesInfo["firstLetter"]=namesInfo["name"].str[0]
  letterInfo = (namesInfo
  .groupby(["firstLetter"], as_index=False)
  .count())
  letterInfo.rename(columns={"name":"num"}, inplace=True)
  #Calculate frequencies
  letterInfo["freq"] = letterInfo["num"]/letterInfo["num"].sum()*100
  return letterInfo[["firstLetter","freq"]]
def countStartLetter(outputfile):
  freqAllNames = getFirstLetterFreq("allNames.csv", sep = "\t")
  freqOnlyNames = getFirstLetterFreq("onlyNames.csv", sep = "\t")
  allFreqs=pd.merge(freqAllNames, freqOnlyNames,how="inner",
                    on="firstLetter")
  allFreqs["diff"] = (allFreqs["freq_x"] - allFreqs["freq_y"]).round(2)
  allFreqs.to_csv(outputfile, index = False, columns =
                 ["firstLetter", "diff"])

#countStartLetter("name.start.csv")