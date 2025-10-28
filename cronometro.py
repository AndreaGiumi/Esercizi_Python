import time

def cronometro(fun):
    def wrapper(*args):
        start = time.time()

        fun(*args)

        print(time.time() - {start})

    return wrapper


@cronometro
def ciao():
    print("Hello")

@cronometro
def square(num: int):
    print(num**2)

if __name__=="__main__":
    ciao()
    square(22)