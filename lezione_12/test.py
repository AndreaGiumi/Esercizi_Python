# dal modulo esercizio_12_1 importo la classe MovieCatalog
from esercizio_12_1 import MovieCatalog

#  creo un oggetto della classe MovieCatalog

catalog: MovieCatalog = MovieCatalog()

# aggiungiamo un regista e dei film al catalogo
catalog.add_movie("Andrea", ["Ciao", "Ciao1"])


print(catalog.getCatalog())


# aggiungere un altro film di Andrea al catalogo

catalog.add_movie("Andrea", ["Ciao3"])


print(catalog.getCatalog())

catalog.add_movie("Andrea1", ["Ciao4", "Ciao5"])
print(catalog.getCatalog())


catalog.remove_movie("Andrea", "Ciao")
print(catalog.getCatalog())



print(catalog.list_directors())


print(catalog.get_movies_by_director("Andrea"))