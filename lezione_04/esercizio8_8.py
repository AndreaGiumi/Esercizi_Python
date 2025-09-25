while True:
    artist:str = str(input("Inserisci artista: "))
    s_title:str = str(input("Inserisci titolo album: "))
    n_songs:int = int(input("Inserisci numero canzoni: "))
    break

def make_album(artist, s_title, n_songs):
    result = {"name" : artist, "title" : s_title, "songs": n_songs}
    if n_songs == None:
        return {"name" : artist, "title" : s_title}
    else:
        return result


print(make_album(artist, s_title, n_songs))