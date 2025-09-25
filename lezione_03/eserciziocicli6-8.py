pets: list[dict] = [{"type": "dog", "prop": "Luca"}, {"type": "cat", "prop": "Simone"}, {"type": "bird", "prop": "Andrea"}]

for dict in pets:
    for key, value in dict.items():
        print(key, value) 