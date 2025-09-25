class MovieCatalog:

    
    '''
    attributi della classe MouviCatalog
    self.catalog: dict[str, list[str]]

    '''
    # inizzializzare un oggetto della classe MovieCatalog
    def __init__(self) -> None:
        self.setCatalog()

    def __str__(self) -> str:
        string = ""
        for key,value in self.catalog.items():
            temp = "/n" + key + ":" + str(value)


    # metodo setter

    # metodo che imposta il valore dell'attributo self.catalog

    def setCatalog(self) -> None:   
        self.catalog: dict[str, list[str]] = {}

    
    # metodo getter

    # metodo che ritorna il valore dell'attributo self.catalog

    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    

    # metodi della classe MovieCatalog

    # metodo che aggiunge una lista di film al catalogo

    def add_movie(self, director_name: str, movies: list[str]) -> None:
        # check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per il regista.")
            # check valore valido di movies
        elif not movies:
            print("Fornire una lista di film che non sia vuota")
            # e se i dati forniti sono validi
        else:
            # se il regista è già presente in self.catalog, aggiungi i film 
            if director_name in self.catalog:
                # aggiungere film al catalogo
                for movie in movies:
                # controlliamo se i film della lista movies siano già stati inseriti nel catalogo
                # self.catalog [director_name]   è la lista dei film prodotti dal regista director_name
                # dove self.catalog è un dizionario
                # director_name è la chiave
                # self.catalog [director_name] è il valore corrispondente alla chiave director_name
                    if movie in self.catalog[director_name]: 
                        # dizionario[key] -> ritrna il valore corrispondente alla chiave key
                        print(f"Il film {movie} è già nel catalogo")
                    # un film della lista movie non è già presente nel catalogo
                    else:
                        # aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)

            # se il regista non è presente nel catalogo , creare un nuovo record che ha come chiave il nome del regista
            # e come valore la lista di film movies
            else:
                self.catalog[director_name] = movies


    # metodo che rimuove un film dal catalogo
    def remove_movie(self, director_name: str, movie: str) -> None:
        # check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per il regista.")
            # check valore valido di movies
        elif not movie:
            print("Fornire una lista di film che non sia vuota")
            # e se i dati forniti sono validi
        else:
            # se il regista è già presente in self.catalog, aggiungi i film e check se il film da rimuovere è presente nella lista dei film prodotti dal regista
            if director_name in self.catalog and movie in self.catalog[director_name]:
                # rimuovere il film dalla lista 
                self.catalog[director_name].remove(movie)
            # se la lista dei film è vuota, rimuovere il regista dal catalogo 
            if not self.catalog[director_name]:
                # rimuovere il regista dal catalogo
                del self.catalog[director_name]
    
    def list_directors(self) -> list[str]:
        return list(self.catalog.keys())
    


    def  get_movies_by_director(self, director_name) -> list[str]:
        return self.catalog[director_name]
    

    def  search_movies_by_title(self,title):
        