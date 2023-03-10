"""
Round 0: Problem Statement:

Question:
Input: Polynomial in standard algebraic notation
Main Output: First Derivative

Possible Implementation:
- A Polynomial Class 
- Contructor that in a, b, c etc. such that ax^2 + bx + c
- Print function takes in any polynomial's underlying data structure and prints it in the algebraic format.

Lets ignore the code for a second now, and come back to the logical aspect of the problem.

Round 1.0 - Brainstorm:
1. Input a polynomial
- Underlying structure could be a list, where index is power of X and value is the constant.
- Shortcoming of this method would be that if the polynomial is ax^100 + b, then the list would have 101 items. Highly wasteful. Should maybe use dictionary (hashmap). 
- Dictionary is also pretty intuitive. Key = Power and Value = Constant. We also need to consider that if key is not in dict then power is not None but 0.
2. Calculate it's derivative
- You take derivative by multiplying the power of x with it's constant part and decrease power by 1.

Round 1.1 - Brainstorm 2:
1. Hashmap/Dictionary to store a polynomial values.
2. A function that calculates derivative and returns a new polynomial instance.
3. Custom __str__() function might do the formatting job.

Round 2 - Pseudocode:

class Polynomial:
    __init__(powers, variable):
        # dict = {power: coeff, power: coeff}
        # E.g.: dict = {2: 10, 1: 12, 0: -1}, variable = x : 10x^2 + 12x -1
        self.dict = dict
        self.variable = variable
    
    __str__(self):
        return {formatted polynomial}

    calc_derivative(self, dict, variable):
        derivative = {}
        for power in dict.keys:
            if power != 0:
                new_power = power - 1
                new_coeff = dict[power] * power
                derivative[new_power] = new_coeff
            
        return Polynomial(derivative, variable)


Round 3 - Edge Cases and Traps:
    Positive: Default Behaviour
    Negative: 
        Power is Negative: {-2: 5, 1: 6} => 5x^-2 + 6x
        Constant is Negative: {2: 10, 1: -3} => 10y^2 -3y
    Zero:
        Power is Zero:
        Constant is Zero:
    Empty:
        Dictionary is Empty
    Very Very Large: 
        1. Large polynomial: {1: 2, 5: 10, 4: 15}
        2. Large Values
    Types:
        Dictionary: Everything should be integers
        Variable should be String


Ruond 4 - Simulating:

my_polynomial = Polynomial(dict = {5: 2, 0: 3}, variable = 'z') # 2z^5 + 3
d1 = my_polynomial.calc_derivitive()
print(d1) # 10z^4

"""

