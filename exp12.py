responses = {
    "hi": "Hello! How are you?",
    "hello": "Hi there!",
    "hey": "Hey! Nice to see you.",
    "how are you": "I'm a chatbot, I'm always good!",
    "what is your name": "I'm ChatPy, your simple chatbot.",
    "bye": "Goodbye! Have a nice day!",
    "good morning": "Good morning! Hope you have a great day!",
    "good night": "Good night! Sleep well!",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
    "what can you do": "I can chat with you and answer simple questions!",
    "who made you": "I was created by a Python programmer!",
    "tell me a joke": "Why did the computer show up at work late? It had a hard drive!",
    "what is python": "Python is a popular programming language that is easy to learn.",
    "how old are you": "I don't have an age, I exist in code!",
    "where are you from": "I live in your computer right now!",
    "help": "You can ask me simple questions like 'hi', 'what is your name', or 'tell me a joke'."
}

def chat_bot():
    print("AI: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You : ").lower()
        if user_input == "bye":
            print("AI: Goodbye!")
            return
        elif user_input in responses:
            print("AI:", responses[user_input])
        else:
            print("I don't understand that yet...")

chat_bot()