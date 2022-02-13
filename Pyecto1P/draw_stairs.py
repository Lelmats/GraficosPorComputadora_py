from OpenGL.GL import *
from glew_wish import *

posicion_escaleras = [0.7,-0.7,0.0]
posicion_escaleras_2 = [-0.5,-0.4,0.0]
posicion_escaleras_3 = [0.7,-0.1,0.0]
posicion_escaleras_4 = [-0.5,0.2,0.0]
posicion_escaleras_5 = [0.7,0.6,0.0]


def draw_escaleras():
    glPushMatrix()
    glTranslatef(posicion_escaleras[0], posicion_escaleras[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0.1,0.9)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_2():
    glPushMatrix()
    glTranslatef(posicion_escaleras_2[0], posicion_escaleras_2[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0.1,0.9)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_3():
    glPushMatrix()
    glTranslatef(posicion_escaleras_3[0], posicion_escaleras_3[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0.1,0.9)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_4():
    glPushMatrix()
    glTranslatef(posicion_escaleras_4[0], posicion_escaleras_4[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0.1,0.9)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_5():
    glPushMatrix()
    glTranslatef(posicion_escaleras_5[0], posicion_escaleras_5[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0.1,0.9)

    glVertex3f(0,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.2,0.0)
    glVertex3f(0,-0.2,0.0)

    glEnd()
    glPopMatrix()