import random

# Define a list of greetings and corresponding responses
greetings = ["hello", "hi", "hey", "greetings"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define a list of basic questions and corresponding answers
basic_questions = ["how are you?", "what is your name?", "what can you do?"]
basic_responses = ["I'm good, thank you!", "My name is Rakesh.", "I will soon be able to give tech support but at the moment, my developer, Jenish, is currently working on teaching me for knowldge so I can help!"]

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
    elif user_input in farewells:
        return random.choice(farewell_responses)
    else:
        return "I can only currently respond to basic questions like Hello and what can you do"

# Main program loop
while True:
    user_input = input("User Input: ")
    response = generate_response(user_input)
    print("Rakesh Output:", response)
