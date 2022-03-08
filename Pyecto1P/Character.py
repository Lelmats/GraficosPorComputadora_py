from collision_escaleras import colisionando_escaleras
from OpenGL.GL import *
from glew_wish import *
import glfw

class Character:
    posicion_triangulo_x = 0
    posicion_triangulo_y = 0
    posicion_triangulo_z = 0
    posicion_y_triangulo_anterior = 0.0
    velocidad = 0.5
    velocidad_x = 0.5
    velocidad_y = 0.5
    IS_JUMPING = False
    IS_FALLING = False
    JUMP = False

# def draw(self):
#     glPushMatrix()
#     glTranslatef(self.posicion_triangulo_x, self.posicion_triangulo_y,0.0)

#     # glBegin(GL_TRIANGLES)
#     # if colisionando(self):
#     #     glColor3f(0,0,1)
#     #     glfw.destroy_window(window)
#     # else:
#     #     glColor3f(1,0,0.7)

#     if colisionando_escaleras() and estado_tecla_arriba == glfw.PRESS :
#         self.posicion_triangulo_y = self.posicion_triangulo_y + cantidad_movimiento

#     if colisionando_escaleras() and estado_tecla_abajo == glfw.PRESS:
#         self.posicion_triangulo_y = self.posicion_triangulo_y - cantidad_movimiento
 
#     glVertex3f(-0.05,-0.05,0)
#     glVertex3f(0.0,0.05,0)
#     glVertex3f(0.05,-0.05,0)
#     glEnd()

#     # glBegin(GL_LINE_LOOP)

#     # glColor(1,1,1)
#     # glVertex3f(-0.05, -0.05, 0)
#     # glVertex3f(-0.05, 0.05, 0)
#     # glVertex3f(0.05, 0.05, 0)
#     # glVertex3f(0.05, -0.05, 0)

#     # glEdnwad()
#     glPopMatrix()