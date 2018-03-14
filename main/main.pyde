from Complex import *

def setup():
    a = Complex(3.0, 13.0)
    b = Complex(7.0, 17.0)
    print(a / b)
    print(a.scale(2))
    size(640, 360)
    fill(255, 126)
    
def draw():
    background(0)