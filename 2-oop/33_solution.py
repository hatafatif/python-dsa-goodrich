class Polynomial:
    """
    Implementation of Algebraic Polynomials using a Dictionary    
    """
    def __init__(self, data: dict, var: str = 'x'):
        """
        data and var are used to describe a polynomial. 
        For example, for the polynomial: 5x^2 - 34x + 2 
        data: {2: 5, 1: -34, 0: 2}
        var: 'x'
        """
        self._data = data
        self._var = var
        print(self)

    def __str__(self):
        formatted = ''
        for i, power in enumerate(self._data):
            if i != 0:
                if self._data[power] >= 0:
                    formatted += '+'
            formatted += str(self._data[power])
            formatted += str(self._var) + '^'
            formatted += str(power)
        return formatted

    
    def derivative(self):
        derivative = {}
        for power in self._data:
            if power != 0:
                derivative[power-1] = self._data[power]*power

        return Polynomial(data = derivative, var = self._var)

    
my_polynomial = Polynomial({2: -5, 1: -10})
d1 = (my_polynomial.derivative())
d2 = (d1.derivative())



