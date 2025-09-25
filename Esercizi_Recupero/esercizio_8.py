class Movie:
    _movie_id:str
    _title:str
    _director:str
    _is_rented:str

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool) ->None:
        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._is_rented = is_rented


    def rent(self) ->bool:

        if self._is_rented == True:
            raise Exception(f"Il film {self._title} è già stato noleggiato!")
        else:
            return self._is_rented == False
        

    def return_movie(self) -> bool:
        if self._is_rented == False:
            raise Exception(f"Il film {self._title} non è stato noleggiato da questo cliente!")
        else:
            return self._is_rented == True
        
    
class Customer:
    _customer_id:str
    _name:str
    _rented_movies:list[Movie]

    def __init__(self,customer_id:str, name:str, rented_movies:list[Movie] = []) -> None:
        self._customer_id = customer_id
        self._name = name
        self._rented_movies = rented_movies


    def rent_movie(self, movie:Movie):
        if movie._is_rented == False:
            raise Exception(f"Il film {movie._title} è già stato noleggiato")
        else:
            self._rented_movies.append(movie)

    
    def return_movie(self, movie: Movie):
        
        if movie in self._rented_movies:
            self._rented_movies.remove(movie)
        else:
            raise Exception(f"Il film {movie._title} non è stato noleggiato da questo cliente!")
        


class VideoRentalStore:
    _movie:dict[str,Movie]
    _customers:dict[str,Customer]

    def __init__(self, movie:dict[str,Movie] = {}, customers:dict[str,Customer] = {}):
        self._movie = movie
        self._customers = customers

    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self._movie:
            movie:Movie = Movie(title, director)
        else:
            raise Exception(f"Il film: {movie} con ID: {movie_id} esiste già!")
        
        

    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self._customers:
            customer:Customer = Customer(customer_id, name)
        else:
            raise Exception(f"Il cliente: {customer} con ID: {customer_id} è già registrato!")
        



    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self._customers[customer_id] or movie_id not in self._movie[movie_id]:
            raise Exception(f"Cliente: {customer_id} o Film: {movie_id} non trovato!")
        else:
            (self._movie[movie_id] or self._customers[customer_id]).rent()


    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self._customers[customer_id] or movie_id not in self._movie[movie_id]:
            raise Exception(f"Cliente: {customer_id} o Film: {movie_id} non trovato!")
        else:
           (self._movie[movie_id] or self._customers[customer_id]).return_movie()


    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id not in  self._customers:
            return []
        else:
            return Customer._rented_movies