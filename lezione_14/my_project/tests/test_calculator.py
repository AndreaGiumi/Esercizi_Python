from my_project.calculator import Calculator

def test_addition():
    calculation: Calculator = Calculator(10, 5)
    assert calculation.addition() == 13, "The sum is wrong"


def test_subtraction():
    calculation: Calculator = Calculator(10,5)
    assert calculation.subtraction() == 5, "The subtraction is wrong"


def test_moltiplication():
    calculation: Calculator = Calculator(10,5) 
    assert calculation.multiplication() == 50, "The moltiplication is wrong"

def test_division():
    calculation: Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, "The quotient is wrong"