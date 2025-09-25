from typing import Callable

sum:Callable[[float,float],float] = lambda a,b:a+b


print(sum(23,7))