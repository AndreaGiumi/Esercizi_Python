def show_messages():
    messages: list[str] = ["Ciao!", "Come stai?", "Tutto bene"]
    print(messages)


def send_messages():
    messages: list[str] = ["Ciao!", "Come stai?", "Tutto bene"]
    sent_messages: list[str] = []
    for i in messages:
        sent_messages.append(i)
    print(messages)
    print(sent_messages)
    
if __name__== "__main__":


    show_messages()
    send_messages()

