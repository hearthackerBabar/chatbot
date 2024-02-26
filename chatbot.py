from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

# Create a new chat bot
chatbot = ChatBot('TermuxBot')

# Create a new trainer for the chat bot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chat bot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Custom styles of conversation
styles = {
    "casual": [
        "Hey, how's it going?",
        "What's up?",
        "Nice weather we're having, huh?",
    ],
    "professional": [
        "Good day, how may I assist you?",
        "Greetings. How can I help you today?",
        "Hello, what can I do for you?",
    ],
    "friendly": [
        "Hi there! How can I make your day better?",
        "Hey friend! What's on your mind?",
        "Hello! Ready to chat?",
    ]
}

# Start the conversation loop
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Randomly choose a conversation style
    style = random.choice(list(styles.keys()))
    print("TermuxBot:", random.choice(styles[style]))

    # Get a response from the chatbot
    response = chatbot.get_response(user_input)
    print("TermuxBot:", response)
