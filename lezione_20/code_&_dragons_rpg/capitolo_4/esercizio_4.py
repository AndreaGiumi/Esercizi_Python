def curry_add(n):
    def add_n(x):
        return x + n
    return add_n