import pandas as pd
import csv
import os
from textblob import TextBlob as tb
def preprocessing():
    directory = '/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/IMDP'
    header=['phrase','sentiment']
    count=0
    db= open('/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/Imdb.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(db)
    writer.writerow(header)
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            count += 1
            f = open(f, "r")
            text=f.read()
            ind=filename.find('_')+1
            num=filename[ind:len(filename)-4]
            data=[text,num]
            writer.writerow(data)
            f.close()
    print(count)
def sentiment():
    path = "/media/anubis21/PROJECTS/Interns/Incorta/repos/Test textblob/Datasets/imdb2.csv"
    analytics = []
    tested = []
    count = 0
    dataSet = pd.read_csv(path)
    text = dataSet["phrase"]
    pol = dataSet["sentiment"]
    for i in range(text.shape[0]):
        analytics.append(tb(text.at[i]).polarity)
        tested.append((pol.at[i] - 5.5) / 4.5)
        if (tested[i] > 0 and analytics[i] > 0) or (tested[i] < 0 and analytics[i] < 0) or (
                tested[i] == 0 and analytics[i] == 0):
            count += 1
    print(count * 100 / len(tested))
    print(count)