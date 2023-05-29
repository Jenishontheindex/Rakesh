import random
import requests

# Define a list of greetings and corresponding responses
greetings = ["hello", "hi", "hey", "greetings"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define a list of basic questions and corresponding answers
basic_questions = ["how are you?", "what is your name?", "what can you do?"]
basic_responses = ["I'm good, thank you!", "My name is Rakesh, your AI assistant.", "I can help you with various technological issues. Just let me know what you need assistance with!"]

# Define a list of technological topics and corresponding assistance
technological_topics = ["programming", "networking", "hardware", "software"]
technological_responses = [
    "I can assist you with programming-related queries and offer guidance on various programming languages and concepts.",
    "For networking issues, I can help troubleshoot network connectivity problems and provide network configuration assistance.",
    "If you have hardware-related problems, I can provide guidance on troubleshooting hardware issues and offer general hardware knowledge.",
    "For software-related queries, I can assist with software installation, troubleshooting, and provide information about different software tools and applications."
]

# Define a list of farewell messages
farewells = ["bye", "goodbye", "see you later", "take care"]
farewell_responses = ["Goodbye!", "See you later!", "Take care!"]

# Function to handle user input and generate response
def generate_response(user_input):
    user_input = user_input.lower()
    
    if user_input in greetings:
        return random.choice(greeting_responses)
    elif user_input in basic_questions:
        return random.choice(basic_responses)
    elif user_input in technological_topics:
        return random.choice(technological_responses)
    elif user_input in farewells:
        return random.choice(farewell_responses)
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"
    
    # Function to handle user input and generate response
def generate_response(user_input):
    user_input = user_input.lower()
    
    if user_input in greetings:
        return random.choice(greeting_responses)
    elif user_input.startswith("tell me about"):
        query = user_input.replace("tell me about", "").strip()
        response = get_wikipedia_summary(query)
        return response
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Function to retrieve a summary from Wikipedia
def get_wikipedia_summary(query):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query
    response = requests.get(url)
    data = response.json()
    if "extract" in data:
        return data["extract"]
    else:
        return "Sorry, I couldn't find any information about that."
# Define a list of forbidden words
forbidden_words = ["arsehole, asshole, arse, ass, arsehead, bastard, bitch, bullshit, cock, cunt, dick, fuck, motherfucker, nigga, nigger, pussy, piss, shit, slut, son of a bitch, twat, wanker, whore, hoe"]

# Function to check if input contains profanity
def contains_profanity(input_text):
    for word in forbidden_words:
        if word in input_text.lower():
            return True
    return False

# Function to handle user input and generate response
def generate_response(user_input):
    user_input = user_input.lower()
    
    if user_input in greetings:
        return random.choice(greeting_responses)
    elif contains_profanity(user_input):
        return "I'm sorry, but I cannot respond to that."
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Main program loop
def main():
    user_name = input("Rakesh: Hi there! What's your name? ")
    print("Rakesh: Nice to meet you, " + user_name + "!")
    
    while True:
        user_input = input(user_name + ": ")
        response = generate_response(user_input)
        print("Rakesh: ", response)

if __name__ == '__main__':
    main()
