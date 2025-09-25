studenti:list[dict] = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

media_studenti:list[dict] = sorted([p["media"] for p in studenti], reverse=True)

print(media_studenti)