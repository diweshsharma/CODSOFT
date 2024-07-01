
user_queries = ['Hi', 'Hello', 'How are you?']
bot_responses = ['Hello!', 'Hi there!', 'I am doing great, thanks!']

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitivity
    for query, response in zip(user_queries, bot_responses):
        if query.lower() in user_input:
            return response
    return "I'm sorry, I didn't understand that."


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
