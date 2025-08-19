# 8-9. Messages
def show_messages(messages):
    """Print each message from the list."""
    for message in messages:
        print(message)

# List of messages
text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "See you at the gym later.",
    "Lunch tomorrow?"
]

# Call the function to display messages
print("Showing messages:")
show_messages(text_messages)
print("\n")

# 8-10. Sending Messages
def send_messages(messages, sent_messages):
    """
    Print each message, and move it to the sent_messages list.
    """
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Copy of messages for sending
messages_to_send = text_messages[:]
sent_messages = []

# Send messages
send_messages(messages_to_send, sent_messages)

# Print both lists to verify
print("\nMessages to send (should be empty):", messages_to_send)
print("Sent messages:", sent_messages)
print("\n")

# 8-11. Archived Messages
# Send messages again using a copy to preserve the original
messages_to_send_copy = text_messages[:]
sent_messages_archive = []

send_messages(messages_to_send_copy, sent_messages_archive)

# Print lists to show original is unchanged
print("\nOriginal messages (unchanged):", text_messages)
print("Sent messages archive:", sent_messages_archive)
