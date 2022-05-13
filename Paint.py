#Actividad 1 : Paint
#Alfaro González Arturo 
#Rodrigo Aldahir Rosete Flores

#Se importan las librerias correspondientes:
from turtle import *

from freegames import vector

#Función para dibujar líneas:
def line(start, end):
    #Dibuja una línea desde la posición del primer clic al segundo
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Función para dibujar un cuadrado:
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    #Rellena la forma trazada
    begin_fill()
    #Se define el número de lados y el ángulo de cada uno de ellos:
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Función para dibujar un círculo:
def circle(start, end):
    #Se importa la librería a utilizar:
    import math
    up()
    goto(start.x,start.y)
    down()
    #Se rellena la figura:
    begin_fill()
    #Se utilizan 360 lados para marcar la circunferencia:
    for count in range(360):
        fd(math.sin(math.radians(1))*(math.sqrt((end.x - start.x)**2+(end.y - start.y)**2)))
        lt(1) 
    end_fill()
    pass  # TODO

#Función para trazar el rectángulo:
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    1
    #Se trazan 4 lados:
    for count in range(4):
        #Se hacen los ajustes de tamaño a los lados para hacerlos el doble de largos que los lados laterales:
        if count % 2 == 0:
            forward((end.x - start.x) * 2)
            left(90)
        else:
            forward(end.x - start.x)
            left(90)
    end_fill()

#Función para trazar un triángulo:
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Se traza el triangulo con un ángulo recto
    for count in range(2):
        forward(end.x - start.x)
        left(90)
    end_fill()

#Función que guarda la posición de los clics:
def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        #Se asignan las posiciones establecidas con cada clic:
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
#Detección de letras para cada color o función:
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()