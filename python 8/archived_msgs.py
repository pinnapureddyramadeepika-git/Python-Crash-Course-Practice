def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Python is fun!", "Keep learning!"]
sent_messages = []

# Pass a copy of the list using [:]
send_messages(messages[:], sent_messages)

print("Original messages:", messages)
print("Sent messages:", sent_messages)
