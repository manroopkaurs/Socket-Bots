# Code for Bot 3 - Valerie

import random
import re

def ucertainity():
    response = ["I am not quite sure what you mean",
                "Are you sure thats a word?",
                "I do not know what you are asking"][random.randrange(3)]
    return response


# Calculates the probability of the response that will be given to the clients message
def probability(user_message, recognised_words, single_response=False, required_words=[]):
    certainity = 0
    has_required_words = True

    # Using a for-loop to recognize text/words to find the correct reply
    for word in user_message:
        if word in recognised_words:
            certainity += 1

    # Calculates the percentage of recognised text/words
    percentage = float(certainity) / float(len(recognised_words))

    # Checking if the required words are in included in the clients message
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # The precentage will help give the best response further down in the code
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


# Function to check all messages
def check_msg(messages):
    prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal prob_list
        prob_list[bot_response] = probability(messages, list_of_words, single_response, required_words)

    # Valerie's responses:
    response('Ciao', ['hello', 'hi', 'sup', 'heyo', 'hey'], single_response=True)  # Response to greeting
    response('Amazing!', ['how', 'are', 'you'], required_words=['how', 'are'])  # Response to question 1
    response('Do or do not. There is no try from Star Wars', ['what', 'your', 'quote' 'favourite', 'movie'],
             required_words=['movie', 'quote', 'favourite'])  # Response to question 2
    response('Billy Jean by Michael Jackson', ['what', 'your', 'current', 'favourite', 'song'],
             required_words=['song', 'favourite'])  # Response to question 3

    # Finding the best response to the clients message
    best_match = max(prob_list, key=prob_list.get)
    return ucertainity() if prob_list[best_match] < 1 else best_match


# Checks the message from the client.
def find_response(client_msg):
    split_message = re.split(r'\s+|[,;?!.-]\s*', client_msg.lower())
    response = check_msg(split_message)
    return response