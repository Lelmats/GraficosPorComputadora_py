from OpenGL.GL import *
from glew_wish import *

posicion_plataforma_0_1 = [0,-0.9, 0.0]
posicion_plataforma_1 = [0.2,-0.9, 0.0]
posicion_plataforma_2 = [0.2,0.3, 0.0]
posicion_plataforma_3 = [0.2,0.6, 0.0]
posicion_plataforma_4 = [0.2,0.9, 0.0]
posicion_plataforma_5 = [0.2,1.2, 0.0]
posicion_plataforma_6 = [0.2,1.5, 0.0]
posicion_plataforma_7 = [0.6,1.5, 0.0]

def draw_plataform_0_1():
    glPushMatrix()
    glTranslatef(posicion_plataforma_0_1[0], posicion_plataforma_0_1[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9,0.1, 0.2)

    glVertex3f(-0.7,0.1,0.0)
    glVertex3f(0.2,0.1,0.0)
    glVertex3f(0.2,0.2,0.0)
    glVertex3f(-0.7,0.2,0.0)

    glEnd()
  
    

    glPopMatrix()
    
def draw_plataform():
    glPushMatrix()
    glTranslatef(posicion_plataforma_1[0], posicion_plataforma_1[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0.0,0.1,0.0)
    glVertex3f(0.8,0.1,0.0)
    glVertex3f(0.8,0.2,0.0)
    glVertex3f(0.0,0.2,0.0)
    glEnd()

    
    glPopMatrix()

   
def draw_plataform_2():
    glPushMatrix()
    glTranslatef(posicion_plataforma_2[0], posicion_plataforma_2[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0.7,-0.8,0.0)
    glVertex3f(-0.9,-0.8,0.0)
    glVertex3f(-0.9,-0.7,0.0)
    glVertex3f(0.7,-0.7,0.0)

    glEnd()
    glPopMatrix()
    

def draw_plataform_3():
    glPushMatrix()
    glTranslatef(posicion_plataforma_3[0], posicion_plataforma_3[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(-0.8,-0.8,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glVertex3f(-0.8,-0.7,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_4():
    glPushMatrix()
    glTranslatef(posicion_plataforma_4[0], posicion_plataforma_4[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0.7,-0.8,0.0)
    glVertex3f(-0.9,-0.8,0.0)
    glVertex3f(-0.9,-0.7,0.0)
    glVertex3f(0.7,-0.7,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_5():
    glPushMatrix()
    glTranslatef(posicion_plataforma_5[0], posicion_plataforma_5[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(-0.7,-0.8,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glVertex3f(-0.7,-0.7,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_6():
    glPushMatrix()
    glTranslatef(posicion_plataforma_6[0], posicion_plataforma_6[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(-0.9,-0.8,0.0)
    glVertex3f(0.1,-0.8,0.0)
    glVertex3f(0.1,-0.7,0.0)
    glVertex3f(-0.9,-0.7,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_7():
    glPushMatrix()
    glTranslatef(posicion_plataforma_7[0], posicion_plataforma_7[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9,0.1,0.2)

    glVertex3f(-0.3,-0.8,0.0)
    glVertex3f(0.3,-0.85,0.0)
    glVertex3f(0.3,-0.75,0.0)
    glVertex3f(-0.3,-0.7,0.0)

    glEnd()
    glPopMatrix()

