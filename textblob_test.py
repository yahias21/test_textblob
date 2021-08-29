import test_twitter as twitter
import imdb
import rotten_tomatto as movies
# TODO IMPLEMENT ACCURACY METRICS
# TODO USE SCIKIT LIBRARY FOR CHECKS
if __name__ == "__main__":
    # [accuracy,count] for each dataset
    accuracy= []
    accuracy.append(movies.sentiment())
    accuracy.append(imdb.sentiment())
    accuracy.append(twitter.sentiment())
    avg,count=0,0
    for ds in accuracy:
        count+=ds[1]
        avg+=ds[1]*ds[0]
    avg/=count
    # accuracy metric is calculated using (TP+TN)/PP method
    print(f"Acuracy for rotten tomato dataset: {accuracy[0][0]}")
    print(f"Acuracy for Imdb dataset: {accuracy[1][0]}")
    print(f"Acuracy for twitter airlines dataset: {accuracy[2][0]}")
    print(f"The weighted average accuracy for the sentiment library: {avg}")
