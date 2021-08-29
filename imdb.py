import pandas as pd
import csv
import os
from textblob import TextBlob as tb
import accuracy_metrics
# dataset downloaded as single text file per review(plz refer to readme in Imdb)
# this func extract reviews and rating and append them in csv file
def preprocessing():
    directory = '/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/Imdb/text'
    header=['phrase','sentiment']
    db= open('/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/Imdb/imdb2.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(db)
    writer.writerow(header)
    # looping in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            f = open(f, "r")
            # read review
            text=f.read()
            # extract rating substring from file name
            ind=filename.find('_')+1
            num=filename[ind:len(filename)-4]
            # append the row
            data=[text,num]
            writer.writerow(data)
            f.close()
# function sentiment adjust data for comparison
def sentiment():
    path = "/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/Imdb/imdb2.csv"
    analytics = []
    tested = []
    dataSet = pd.read_csv(path)
    text = dataSet["phrase"]
    pol = dataSet["sentiment"]
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        tested.append((pol.at[i] - 5.5) / 4.5)
    return accuracy_metrics.accuracy(tested,analytics)