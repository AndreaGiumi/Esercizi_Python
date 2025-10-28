class AppointemntSchedule:
    def __init__(self, appointments: dict[str, dict[str, bool | str]] = {}):
        
        self.appointments = appointments

    
    def schedule_appointemt(self, app_id: str, data: str) -> str | dict:
        if app_id in self.appointments:
            return "Errore: appuntamento già esistente"
        self.appointments[app_id] = {"Programmato": True, "Data" : data}
        return self.appointments[app_id]
    

    def reschedule_appointemnt(self, app_id: str, nuova_data: str) -> str | dict:
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato"
        self.appointments[app_id]["Data"] = nuova_data
        return self.appointments[app_id]

    def cancel_appointment(self, app_id: str) -> str | dict:
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato"
        self.appointments[app_id]["Programmato"] =  False
        return self.appointments[app_id]

    def remove_appointemnt(self, app_id: str) -> str | dict:
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato"
        return self.appointments.pop(app_id)
    
    def list_appointemnt(self) ->list[str]:
        return list(self.appointments.keys())
    
    def get_appointment(self, app_id :str) -> str | dict:
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato"
        return self.appointments[app_id]
    


if __name__=="__main__":

    dizionario_app = {"45AS":{"Programmato":True, "Data": "25/04/25"}, "46AS" : {"Programmato" : True, "Data" : "14/05/25"}, "47AS" : {"Programmato" : True, "Data" : "19/05/26"}}

    appuntamenti: AppointemntSchedule = AppointemntSchedule(dizionario_app)

    appuntamenti.schedule_appointemt("4475", "14/08/25")
    print(dizionario_app)
    appuntamenti.reschedule_appointemnt("45AS","17/11/25")
    print(dizionario_app)
    appuntamenti.cancel_appointment("45AS")
    print(dizionario_app)
    appuntamenti.remove_appointemnt("47AS")
    print(dizionario_app)
    
    print(appuntamenti.list_appointemnt())
    print(appuntamenti.get_appointment("4477"))
    