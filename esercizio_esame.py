class TaskManager:

    def __init__(self, tasks:  dict[str, dict[str, bool | str]] = {}) -> None :

        self.tasks:  dict[str, dict[str, bool | str]] = tasks


    def create_task(self, task_id:  str, descrizione:  str) -> dict | str :

        if task_id in self.tasks :
            return "Errore Chiave Già Esistente"
        else :

            temp_dict:  dict[str, dict[str, bool | str]] = {"descrizione" : descrizione,
                                                            "completato" :False}
            
            self.tasks[task_id] = temp_dict

        return temp_dict
        
    def complete_task(self, task_id:  str) -> dict | str: 

        if task_id not in self.tasks :
            return "Chiave non esistente"
        else :

            if self.tasks[task_id]["completato"] :
                return "Il task è già completato"
            
            self.tasks[task_id]["completato"] = True

            return self.tasks[task_id]
        
    
    def update_description(self, task_id:  str, nuova_descrizione: str) -> dict | str: 

            if task_id not in self.tasks :
                return "Il task non è nel dizionario!"
            else :
                self.tasks[task_id]["descrizione"] = nuova_descrizione

                return self.tasks[task_id]
            
    def remove_task(self, task_id:  str) -> dict | str :
        if task_id not in self.tasks: 
            return "Task non presente"
        else :
            return self.tasks.pop(task_id)
        

    def list_tasks(self) -> list[str] :
        # con il ciclo for

        # lista_chiavi : list[str] = []

        # for key in self.tasks.keys(): 
        #     lista_chiavi.append(key)

        # return lista_chiavi

        return list(self.tasks.keys()) # altro metodo più veloce
    

    def get_task(self, task_id:  str) -> dict | str: 
        if task_id not in self.tasks :
            return "Task non presente"
        else :
            return self.tasks[task_id]
        




