def repeatnames(threshold, outputfile):
  file = pd.read_csv("allNames.csv", sep = "\t")
  file = (file[file["nonPerson"].isna()][["artist", "song", "name", "highestRank"]]
  .groupby(["artist", "song", "name"])
  .count())
  file =(file[file["highestRank"] >= threshold]
  .rename(columns = {"highestRank":"times"}))
  file.to_csv(outputfile)

def main():
    repeatnames(20, "tests/repeat.20.csv")
    repeatnames(30, "tests/repeat.30.csv")
    repeatnames(40, "tests/repeat.40.csv")
if __name__=="__main__":
    main()  