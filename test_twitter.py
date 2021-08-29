from textblob import TextBlob as tb
import pandas as pd
import accuracy_metrics
def sentiment():
    Path = "/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/twitter airline/Tweets.csv"
    analytics = []
    tested = []
    dataSet = pd.read_csv(Path)
    text = dataSet["text"]
    pol = dataSet["airline_sentiment"]
    # map the sentiment from str to numbers
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        if pol.at[i] == "positive":
            tested.append(1)
        elif pol.at[i] == "negative":
            tested.append(-1)
        else:
            tested.append(0)
    return accuracy_metrics.accuracy(tested, analytics)
