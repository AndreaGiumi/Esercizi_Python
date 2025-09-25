glossary: dict[str] = {
    "Broadcast": "The message is intended for all computers on the network.",
    "Multicast": "The message is directed to a specific group of computers within the network",
    "Anycast": "The message can be received by any one of the computers in the network, typically the one nearest to the source.",
    "Unicast": "The message is distributed to every computer, only the recipient specified in the message’s address field processes it.",
    "Challenges": "Addressing cybersecurity threats and privacy concerns in an increasingly interconnected world."}

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"{meaning}\n")


