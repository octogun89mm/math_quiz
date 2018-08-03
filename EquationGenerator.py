from random import randint as rdm


class EquationGenerator:
    """
    This class build a equation out the parameter we give

    Equation("<sym>",<level>)


    # Attributes #

        -sym > Symbol (+ or - or * or /)
        -level > Level
            1: Easy (1,10)
            2: Medium (10,20)
            3: Hard (20,30)
        -a > First number of the random range
        -b > Second number of the random range
        -rdm_0 > Random number #0
        -rdm_1 > Random number #1
        -answer > Answer of the equation (Integer)
        -equa > The question (String that contains the equation)
    """

    def __init__(self, sym, level):
        self.sym = sym # Operand used in the equation
        self.level = level # The level of dificulty of the equation (1, 2 or 3)

        # Define the range of the 2 integer used in the equation
        if self.level == 1:
            self.a, self.b = 1, 10
        elif self.level == 2:
            self.a, self.b = 10, 20
        elif self.level == 3:
            self.a, self.b = 20, 30

        # Calls the random.randint() method to intialise 2 randoms
        # integers within a range described in the "__init__" method
        self.rdm_0, self.rdm_1 = rdm(self.a, self.b), rdm(self.a, self.b)

        # Defines the operator used in the equation
        if self.sym == "+":
            self.answer = self.rdm_0 + self.rdm_1
        elif self.sym == "-":
            self.answer = self.rdm_0 - self.rdm_1

    def test_equa(self):
        """
        Function that returns the full equation with the answer
        (For test purposes only)
        """
        return"{0} {1} {2} = {3}".format(self.rdm_0, self.sym, self.rdm_1, self.answer)

    def get_equa(self):
        """
        Function that returns the equation without the answer
        """
        return"{0} {1} {2} = ".format(self.rdm_0, self.sym, self.rdm_1)

    def get_answer(self):
        """
        Function that returns the answer of the equation
        """
        return self.answer

    def get_rdm_num(self, num):
        """
        Funtion that returns the 2 integers used in the equation
        """
        if num == 0:
            return self.rdm_0
        if num == 1:
            return self.rdm_1
