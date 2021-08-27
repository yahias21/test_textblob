from textblob import TextBlob as tb
import pandas as pd
def test_twitter():
    Path = "/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/Tweets.csv"
    analytics = []
    tested = []
    count = 0
    dataSet = pd.read_csv(Path)
    text = dataSet["text"]
    pol = dataSet["airline_sentiment"]
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        if pol.at[i] == "positive":
            tested.append(1)
        elif pol.at[i] == "negative":
            tested.append(-1)
        else:
            tested.append(0)
    for i in range(len(tested)):
        if not (tested[i] < 0 or analytics[i] < 0) or (tested[i] < 0 or analytics[i] > 0):
            count += 1
    return count * 100 / len(tested)
