def letter_count(text: str) -> dict[str,int]:
    dizionario_min = {}
    new_text = text.lower()
    if not new_text:
        return {}
    else:
        for i in new_text.strip():
            if i.isdigit() or i.isalpha():
                dizionario_min[i] = 0
        for i in new_text.strip():
            if i in dizionario_min:
                dizionario_min[i] += 1
        return dizionario_min
    

if __name__=="__main__":

    print(letter_count("CIao ATutttiitE££££RE"))