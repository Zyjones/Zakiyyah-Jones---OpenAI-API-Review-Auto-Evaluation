from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    This function is the comprehensive pipeline that  opens the json files with reviews, extracts it, 
    and get the lists of sentiments and plots a graph.
    
    Argument: 
    This function takes in filepath for the json reviews.

    Return:
    This function will return the list of sentiments you've generated from your OpenAI API call.
    """
    # open the json object
    with open('data/raw/reviews.json') as j:
        reviews_file = json.load(j)
        #print(reviews_file)

    # extract the reviews from the json file
    reviews = reviews_file["results"]
    #print(reviews)

    # get a list of sentiments for each line using get_sentiment
    list_sentiments = get_sentiment(reviews)[0:50]
    #print(list_sentiments)

    #test checking to see accuracy of open ai (lines 32-43)
    #review_specific = reviews_file["results"][32]
    #review_specific2 = reviews_file["results"][46]
    #list_sentiments1 = get_sentiment(review_specific)
    #list_sentiments2 = get_sentiment(review_specific2)

    #print("Review10: ", review_specific)
    #print("Sentiment: ",list_sentiments1)

    #print("Review50: ", review_specific2)
    #print("Sentiment: ",list_sentiments2)

    #print("Length of reviews", len(list_sentiments))

    # plot a visualization expressing sentiment ratio
    make_plot(list_sentiments)

    # return sentiments
    return list_sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
