
class Complex(object):
    
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
        
    def real(self):
        return self.r
    
    def imag(self):
        return self.i
    
    def norm(self):
        return self.real() ** 2 + self.imag() ** 2
    
    def conjugate(self):
        return Complex(self.real(), -1 * self.imag())
    
    def scale(self, factor):
        return Complex(self.real() * factor, self.imag() * factor)
        
    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.real() + other.real(), self.imag() + other.imag())
        else:
            return Complex(self.real() + other, self.imag())
    
    def __mul__(self, other):
        ac = self.real() * other.real()
        bd = self.imag() * other.imag()
        term = (self.real() + self.imag()) * (other.real() + other.imag())
        return Complex(ac - bd, term - ac - bd)
    
    def __sub__(self, other):
        return self + (-1 * num)
    
    def __div__(self, other):
        result = self * other.conjugate()
        return result.scale(1/other.norm())
    
    def __str__(self):
        space = ""
        if(self.imag() > 0):
            space = "+"
        return str(self.real()) + space + str(self.imag()) + "i"
    
    