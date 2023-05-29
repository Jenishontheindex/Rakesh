import random

# Define a list of greetings and corresponding responses
greetings = ["hello", "hi", "hey", "greetings"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define a list of basic questions and corresponding answers
basic_questions = ["how are you?", "what can you do?"]
basic_responses = ["I'm good, thank you!", "I can help you with various technological issues. Just let me know what you need assistance with!"]

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
def generate_response(user_input, user_name):
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
        return f"I'm sorry, {user_name}, I don't understand. Can you please rephrase your question?"

# Main program loop
def main():
    user_name = input("Rakesh: Hi there! What's your name? ")
    print("Rakesh: Nice to meet you, " + user_name + "!")
    
    while True:
        user_input = input(user_name + ": ")
        response = generate_response(user_input, user_name)
        print("Rakesh: ", response)

if __name__ == '__main__':
    main()
