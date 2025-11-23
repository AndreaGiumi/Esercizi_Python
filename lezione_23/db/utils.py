import json
import os
from lezione_23.data_model.nazione import Nazione
from lezione_23.data_model.citta import Citta

current_dir = os.path.curdir
MOCKUP_DB_INIT_JSON_FILENAME = os.path.join(current_dir, "db", "mockup_db_init.json")
MOCKUP_DB_JSON_FILENAME = os.path.join(current_dir, "db", "mockup_db.json")

def load_data_from_db() -> dict:
    with open(MOCKUP_DB_JSON_FILENAME) as f:
        return json.load(f)

def store_data_on_db(data) -> None:
    with open(MOCKUP_DB_INIT_JSON_FILENAME, "w+") as f:
        json.dump(data, f)

result: dict[str, Nazione] = {}
def load_nazione() -> dict[str, Nazione]:
    with open(MOCKUP_DB_JSON_FILENAME) as f:
        data = json.load(f)
    nazioni_data = data["nazioni"]
    for nazione_nome, nazione_data in nazioni_data.items():
        nazione: Nazione = Nazione(nazione_data["nome"])
        result[nazione_nome] = nazione
    return result


def store_nazione(nazione: Nazione) -> None:
    # devo controllare se la nazione c'è già
    dati = load_data_from_db
    nazioni_dict = dati["Nazione"]
    if nazione.nome() in nazioni_dict:
        nazioni_dict.pop(nazione.nome())
    nazione_info = nazione.info()
    nazioni_dict[nazione.nome()] = nazione_info
    store_data_on_db(dati)

    
def load_citta(nazioni: dict[str, Nazione]) -> dict[str, Citta]:
    dati = load_data_from_db
    all_citta_data = dict[str, dict[str, int | str]] = dati["citta"]

    result_citta: dict[str, 'Citta'] = {}
    for citta_data in all_citta_data.values():
        nazione: Nazione = nazioni[citta_data["nazione"]]
        citta: Citta = Citta(
            nome=citta_data["nome"],
            abitanti=citta_data["abitanti"],
            nazione=nazione
        )
        result_citta[citta.nome()] = citta
    return result_citta