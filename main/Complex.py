
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
        
    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.real() + other.real(), self.imag() + other.imag())
        else:
            return Complex(self.real() + other, self.imag())
    
    def __mul__(self, other):
        num = other
        if type(other) is not Complex:
            num = Complex(other, 0)
        return Complex(self.real()*num.real() - self.imag()*num.imag(), self.real()*num.imag() + self.imag()*num.imag())
    
    def __sub__(self, other):
        num = other
        if type(other) is not Complex:
            num = Complex(other, 0)
        return self + (-1 * num)
    
    def __div__(self, other):
        num = other
        if type(other) is not Complex:
            num = Complex(other, 0)
        return 1/num.norm() * self * other.conjugate()
    
    def __str__(self):
        space = ""
        if(self.imag() > 0):
            space = "+"
        return str(self.real()) + space + str(self.imag()) + "i"
    
    