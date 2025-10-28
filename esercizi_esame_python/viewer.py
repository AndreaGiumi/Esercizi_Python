from esercizi_esame_python.ticket import Ticket
class Viewer:
    def __init__(self, viewer_id: str, name: str, booked_tickets: list[Ticket] = []):
        
        self.viewer_id = viewer_id
        self.name = name
        self.booked_tickets = booked_tickets

    
    def book_ticket(self, ticket: Ticket) -> None:
        if ticket.is_booked:
            print(f"Il biglietto per '{ticket.movie}' non è disponibile.")
        else:
            self.booked_tickets.append(ticket)
            ticket.book()
    

    def cancel_ticket(self, ticket: Ticket) -> None:
        if not ticket.is_booked:
            print(f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore.")
        else:
            self.booked_tickets.remove(ticket)
            ticket.cancel()

    
            
