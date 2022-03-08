from msilib.schema import Class
from OpenGL.GL import *
from glew_wish import *
import glfw
import math


class Bala:
    posicion_x  = 0.0
    posicion_y = 0.0
    posicion_z = 0.0

    disparando = False

    angulo = 0.0
    velocidad = 0.8

    def draw(self):
        if self.disparando:
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.0, 0.0)
            glVertex3f(-0.01,0.01,0.0)
            glVertex3f(0.01,0.01,0.0)
            glVertex3f(0.01,-0.01,0.0)
            glVertex3f(-0.01,-0.01,0.0)
            glEnd()
            glPopMatrix()

    def actualizar(self, tiempo_delta):
            if self.disparando:
                cantidad_movimiento = self.velocidad * tiempo_delta
                self.posicion_x = self.posicion_x + (
                    math.cos(self.angulo * math.pi / 180.0) * cantidad_movimiento
                )
                self.posicion_y = self.posicion_y + (
                    math.sin(self.angulo * math.pi / 180.0) * cantidad_movimiento
                )

                #Checar si se salió de los límites:
                if (self.posicion_x > 1 or self.posicion_x < -1 or 
                    self.posicion_y > 1 or self.posicion_y < -1):
                    disparando = False
