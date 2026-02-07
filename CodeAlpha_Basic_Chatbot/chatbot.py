def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! Nice to meet you"

    elif user_input == "hi":
        return "Hello! How can I help?"

    elif user_input == "How are you":
        return "I am fine, thanks for asking!"

    elif user_input == "What is your name":
        return "I am a simple chatbot created using Python."

    elif user_input == "Bye":
        return "Goodbye! Have a great day"

    else:
        return "Sorry, I didn't understand that. Please try again."

print("===================================")
print("Welcome to CodeAlpha Chatbot")
print("Type 'bye' to exit the chat")
print("===================================")

while True:
    user_message = input("You: ")
    bot_reply = chatbot_response(user_message)
    print("Bot:", bot_reply)

    if user_message.lower == "bye":
        break
