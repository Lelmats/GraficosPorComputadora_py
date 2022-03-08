from OpenGL.GL import *
from glew_wish import *

from Character import *

from draw_stairs import posicion_escaleras
from draw_stairs import posicion_escaleras_2
from draw_stairs import posicion_escaleras_3
from draw_stairs import posicion_escaleras_4
from draw_stairs import posicion_escaleras_5

playerr = Character()

def colisionando_escaleras():
    colisionando_escaleras = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (playerr.posicion_triangulo_x + 0.05 >= posicion_escaleras[0] + 0.05
    and playerr.posicion_triangulo_x - 0.05 <= posicion_escaleras[0] + 0.1 
    and playerr.posicion_triangulo_y + 0.05 >= posicion_escaleras[1] - 0.1
    and playerr.posicion_triangulo_y - 0.05 <= posicion_escaleras[1] + 0.3):
        colisionando_escaleras = True
    if (playerr.posicion_triangulo_x + 0.05 >= posicion_escaleras_2[0] - 0.0
    and playerr.posicion_triangulo_x - 0.05 <= posicion_escaleras_2[0] + 0.1 
    and playerr.posicion_triangulo_y + 0.05 >= posicion_escaleras_2[1] - 0.1
    and playerr.posicion_triangulo_y - 0.05 <= posicion_escaleras_2[1] + 0.3):
        colisionando_escaleras = True
    if (playerr.posicion_triangulo_x + 0.05 >= posicion_escaleras_3[0] - 0.0
    and playerr.posicion_triangulo_x - 0.05 <= posicion_escaleras_3[0] + 0.1 
    and playerr.posicion_triangulo_y + 0.05 >= posicion_escaleras_3[1] - 0.1
    and playerr.posicion_triangulo_y - 0.05 <= posicion_escaleras_3[1] + 0.3):
        colisionando_escaleras = True
    if (playerr.posicion_triangulo_x + 0.05 >= posicion_escaleras_4[0] - 0.0
    and playerr.posicion_triangulo_x - 0.05 <= posicion_escaleras_4[0] + 0.1 
    and playerr.posicion_triangulo_y + 0.05 >= posicion_escaleras_4[1] - 0.1
    and playerr.posicion_triangulo_y - 0.05 <= posicion_escaleras_4[1] + 0.3):
        colisionando_escaleras = True
    if (playerr.posicion_triangulo_x + 0.05 >= posicion_escaleras_5[0] - 0.0
    and playerr.posicion_triangulo_x - 0.05 <= posicion_escaleras_5[0] + 0.1 
    and playerr.posicion_triangulo_y + 0.05 >= posicion_escaleras_5[1] - 0.1
    and playerr.posicion_triangulo_y - 0.05 <= posicion_escaleras_5[1] + 0.2):
        colisionando_escaleras = True

    return colisionando_escaleras