print("=" * 40)
print("🤖 Smart AI Chatbot")
print("Type 'bye' to exit")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: My name is SmartBot, your AI assistant.")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: Current time is {current_time}")

    elif "date" in user:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "python" in user:
        print("Bot: Python is a popular programming language used in AI and Machine Learning.")

    elif "machine learning" in user:
        print("Bot: Machine Learning enables computers to learn from data and make predictions.")

    elif "artificial intelligence" in user or "ai" in user:
        print("Bot: Artificial Intelligence is the simulation of human intelligence by machines.")

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome! 😊")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")