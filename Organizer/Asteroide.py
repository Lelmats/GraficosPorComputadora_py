from msilib.schema import Directory
from re import M
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Asteroide(Modelo):

    def __init__(self, x, y, direccion, velocidad):
        super().__init__(x,y,0.0, velocidad, direccion)
        
    def actualizar (self, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        self.posicion_x = self.posicion_x + (math.cos(self.direccion * math.pi / 180.0) * cantidad_movimiento)
        self.posicion_y = self.posicion_y + (math.sin(self.direccion * math.pi / 180.0) * cantidad_movimiento)
    
        if self.posicion_x > 1.05: 
            self.posicion_x = -1.0
        if self.posicion_x < -1.05: 
            self.posicion_x = 1.0
            
        if self.posicion_y > 1.05: 
            self.posicion_y = -1.0   
        if self.posicion_y < -1.05: 
            self.posicion_y = 1.0  

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.4, 0.9, 0.21)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()
