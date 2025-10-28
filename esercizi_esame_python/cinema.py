from esercizi_esame_python.ticket import Ticket
from esercizi_esame_python.viewer import Viewer

class Cinema(Ticket, Viewer):
    def __init__(self, ticket_id: str, movie: str, seat: str, is_booked: bool, viewer_id: str, name: str, booked_tickets: list[Ticket], 
                 tickets: dict[str, Ticket] = {}, viewers: dict[str, Viewer] = {}) -> None:
        Ticket().__init__(ticket_id, movie, seat, is_booked)
        Viewer().__init__(viewer_id, name, booked_tickets)

        self.tickets = tickets
        self.viewers = viewers

    def add_ticket(self, ticket_id: str, movie: str, seat: str) -> None:
        if ticket_id in self.tickets:
            print(f"Il biglietto con ID '{ticket_id}' esiste già.")
        else:
            self.tickets[ticket_id] = Ticket(ticket_id, movie, seat)


    def register_viewer(self, viewer_id: str, name: str) -> None:
        if viewer_id in self.viwers:
            print(f"Lo spettatore con ID '{viewer_id}' è già registrato.")
        else:
            self.viwers[viewer_id] = Viewer(viewer_id, name)
    

    def book_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id not in self.viwers and ticket_id not in self.tickets:
            print("Spettatore non trovato")
        else:
            viewer = self.viewers[viewer_id]
            ticket = self.tickets[ticket_id]

            viewer.book_ticket(ticket)

    
    def cancel_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id not in self.viewers and ticket_id not in self.tickets:
            print("Spettatore non trovato")
        else:
            viewer = self.viewers[viewer_id]
            ticket = self.tickets[ticket_id]

            viewer.cancel_ticket(ticket)

    
    def list_available_tickets(self) -> list[str]:
        lista_id = []
        for ticket_id, ticket in self.tickets.items():
            if not ticket.is_booked:
                lista_id.append(ticket_id)
        return lista_id
    

    def list_viewer_bookings(self, viewer_id: str) -> list[str] | str:
        lista_ticket = []
        if viewer_id in self.viewers:
            viewer = self.viewers[viewer_id]
            for ticket in viewer.booked_tickets:
                lista_ticket.append(ticket.ticket_id)
            return lista_ticket
        else:
            return "Errore: spettatore non trovato!"



