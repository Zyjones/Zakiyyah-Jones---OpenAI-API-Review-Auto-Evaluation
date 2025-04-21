import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    This function counts how many times each sentiment (positive, neutral, negative, and irrelevant) appears 
    and plots it into a bar graph. 

    Argument: 
        This function takes in a list of sentiments.

    Returns:
        This function is not required to return any values but outputs a graph to the images folder.  
    """
    
    #defensive guard
    if not sentiments:
        return "Error. No sentiments in list"


    #sentiment_labels =list(set(sentiments))  #the order kept changing
    sentiment_labels = ["positive", "neutral", "negative", "irrelevant"]

    #loop through sentiment_labels and for each step in the loop, count the sentiments and 
    # append the count to the sentiment count 
    sentiment_count = []

    for sentiment in sentiment_labels:
        x = sentiments.count(sentiment)
        sentiment_count.append(x)
    #print("Length of sentiment count", sentiment_count)
   
    #plot bar graph 
    #["positive", "neutral", "negative", "irrelevant"]
    fig, ax = plt.subplots()
    
    bar_labels = ['green', 'blue', 'red', 'orange']
    bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']
    ax.bar(sentiment_labels, sentiment_count,label=bar_labels, color=bar_colors )

    ax.set_ylabel('Counts of Sentiments')
    ax.set_title('Sentiments of Reviews')
    fig.savefig("images/sentiment reviews graph")
    plt.show()
