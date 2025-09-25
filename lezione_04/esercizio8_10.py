def show_messages():
    messages: list[str] = ["Ciao!", "Come stai?", "Tutto bene"]
    print(messages)


def send_messages():
    messages: list[str] = ["Ciao!", "Come stai?", "Tutto bene"]
    sent_messages: list[str] = []
    for i in range(len(messages)):
        message = messages.pop(0)
        sent_messages.append(message)
    print(messages)
    print(sent_messages)


show_messages()
send_messages()