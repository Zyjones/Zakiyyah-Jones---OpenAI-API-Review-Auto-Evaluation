from openai import OpenAI



def get_sentiment(text: list) -> list:
    """
    This function will analyze a list of string reviews and turn it into a list of sentiments using gpt-4o-mini language model. 
    
    Argument: 
        a list of string reviews 

    Returns:
        return the output of the large language model expressed as a list of sentiments 
    """
    
    #Defensive Guard
    for i in text: #loop through the list to check if each element in list is strings
        if type(i) != str:
            return "Wrong input. text must be an array of strings."
    if not text: #checking if string is empty
        return "Wrong input. text must be an array of strings."
    
    
    #Defining the behavior of how we want the language model to react; Setting up environment for the developer
    system_prompt = """
    You are a helpful assistant that categorizes text reviews into sentiment categories.
    The categories are positive, neutral, negative, and irrelevant. The response can only have one sentiment per review. 
    There should only be 50 items in the list. There should no more than 50 or less than 50 responses in the list.
    For example, if a review has only negative connonations such as using words like "stinks" or "don't recommend", then that will be negative
    If a review has mostly positive connotations such as "love"  or "will buy again", then that would be a postive response.
    If a review has about the same amount of postive and negative connotations or has "okay" and neutral words, then the review should return neutral
    If a review has nothing to do with coconut water, then the response should come back as irrelevant.
    Thank you helpful assistant. 

    """
    # Add this to the system prompt to do additional data analysis
    #   Output the most common word in the negative reviews that is not "cocunut" or prepositions
    #   Output how many times plastic is used in the reviews

    #Telling OpenAI to do this prompt, now that we are in that enviroment
    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """

    client = OpenAI()
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        #messages is the list of key value pairs. There are 2 dict. in each 
        messages = [
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
   
    
    #returning the list of sentiments based on the reviews and removing new line characters
    return completion.choices[0].message.content.split() 
   
    
