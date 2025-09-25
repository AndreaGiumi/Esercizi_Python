def num_primo(n:int):
    for i in range(n - 1, 1, -1):
        if n % i == 0:  
            return False
        
    return True



print(num_primo(5))