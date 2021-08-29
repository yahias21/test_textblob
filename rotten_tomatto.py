from textblob import TextBlob as tb
import pandas as pd
import accuracy_metrics
def sentiment():
    path="/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/rotten_tomattos/train.tsv"
    analytics=[]
    tested=[]
    dataSet = pd.read_csv(path, sep='\t')
    text=dataSet["Phrase"]
    pol=dataSet["Sentiment"]
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        tested.append((pol.at[i]-2)/2)
    return accuracy_metrics.accuracy(tested, analytics)
