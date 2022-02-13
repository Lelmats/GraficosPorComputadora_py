from OpenGL.GL import *
from glew_wish import *

posicion_triangulo = [-0.3,-0.75,0.0]
from draw_stairs import posicion_escaleras
from draw_stairs import posicion_escaleras_2
from draw_stairs import posicion_escaleras_3
from draw_stairs import posicion_escaleras_4
from draw_stairs import posicion_escaleras_5


def colisionando_escaleras():
    colisionando_escaleras = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_2[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_2[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_2[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_2[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_3[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_3[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_3[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_3[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_4[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_4[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_4[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_4[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_5[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_5[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_5[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_5[1] + 0.22):
        colisionando_escaleras = True
    return colisionando_escaleras