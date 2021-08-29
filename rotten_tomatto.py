from textblob import TextBlob as tb
import pandas as pd
if __name__ == "__main__":
    path="/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/movies/train.tsv"
    analytics=[]
    tested=[]
    count=0
    dataSet = pd.read_csv(path, sep='\t')
    text=dataSet["Phrase"]
    pol=dataSet["Sentiment"]
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        tested.append((pol.at[i]-2)/2)

