def make_album(artist:str,s_title:str,n_songs=None):
    result = {"name" : artist, "title" : s_title, "songs": n_songs}
    if n_songs == None:
        return {"name" : artist, "title" : s_title}
    else:
        return result


print(make_album("Andri", "Sono carino"))
print(make_album("Andri", "Sono carino", 13))

