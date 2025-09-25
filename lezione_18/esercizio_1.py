import math
def safe_sqrt(number):
    try:
        mathsq = math.sqrt(number)
        print(mathsq)
    except ValueError as error:
        print(error)


safe_sqrt(25)
safe_sqrt(-25)