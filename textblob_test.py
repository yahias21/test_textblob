import test_twitter as twitter
import imdb
from textblob import TextBlob
import rotten_tomatto as movies
# TODO IMPLEMENT ACCURACY METRICS
# TODO USE SCIKIT LIBEARY FOR CHECKS
if __name__ == "__main__":
    # accuracy metric is calculated using (TP+TN)/PP method
    imdb.sentiment()
    print("Acuracy for rotten_tomato dataset: ")