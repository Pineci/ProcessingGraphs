from Complex import *
from CoordinatePlane import *

WIDTH = 600
HEIGHT = 600


def setup():
    """a = Complex(3.0, 13.0)
    b = Complex(7.0, 17.0)
    print(a / b)
    print(a.scale(2))"""
    
    size(WIDTH, HEIGHT)
    global graph
    graph = CoordinatePlane(True)
    graph.SetCenter(0.0, 0.0)
    graph.SetXWindowRadius(2.0)
    
    stroke(0)
    fill(0)
    
def draw():
    background(255)
    #translate(width/2, height/2)
    graph.Point(0, 0)
    graph.Circle(1.0, 1.0, 1.0)
    #graph.Line(-1, 0, 0, 1)