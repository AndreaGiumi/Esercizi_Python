class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    def evaluate(self, x):
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result