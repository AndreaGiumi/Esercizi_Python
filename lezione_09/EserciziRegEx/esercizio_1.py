import re
def is_integer(s:str):
   string = bool(re.fullmatch(f"-?\d+", s))
   return string

    


print(is_integer("54.4"))