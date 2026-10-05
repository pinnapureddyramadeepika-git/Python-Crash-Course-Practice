# Exercise 8-9 program (starting point)
def show_messages(messages):
    for message in messages:
        print(message)

# Exercise 8-10: Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # remove from original list
        print(current_message)             # print the message
        sent_messages.append(current_message)  # move to sent_messages

# Example usage
messages = ["Hello!", "How are you?", "Python is fun!", "Keep learning!"]
sent_messages = []

print("Original messages:")
show_messages(messages)

print("\nSending messages...")
send_messages(messages, sent_messages)

print("\nFinal lists:")
print("Messages:", messages)
print("Sent messages:", sent_messages)
 
 
