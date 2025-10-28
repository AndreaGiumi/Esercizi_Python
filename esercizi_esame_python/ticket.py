class Ticket:
    def __init__(self, ticket_id: str, movie: str, seat: str, is_booked: bool) -> None:

        self.ticket_id = ticket_id
        self.movie = movie
        self.seat = seat
        self.is_booked = is_booked

    
    def book(self) -> None:
        if not self.is_booked:
            print(f"Il biglietto per '{self.movie}'posto '{self.seat}' è già prenotato!")
        else:
            self.is_booked = True

    def cancel(self) -> None:
        if self.is_booked:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' non risulta prenotato.")
        else:
            self.is_booked = False