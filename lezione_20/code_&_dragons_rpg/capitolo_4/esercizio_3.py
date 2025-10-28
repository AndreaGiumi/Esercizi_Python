def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed