from fnmatch import translate
from OpenGL.GL import *
from glew_wish import *
from Character import *
from math import * 
import math
import glfw

player = Character()


posicion_barrel = [-0.4,0.85, 0.0]

class Platano:
    posicion_barrel_x = 0
    posicion_barrel_y = 0
    posicion_barrel_z = 0
    direccion_barrelx = 1
    direccion_barrely = 0
    velocidad_barrel = 0.9

angulo_platano = 0.0
direccion_platano = 1
velocidad_platano = 0.5
rotacion_platano = 0
posicion_platano = [-0.9,0.85,0.0]

def draw_barrel():
    sides = 32    
    radius = 0.04  
    glPushMatrix()
    glTranslatef(posicion_barrel[0], posicion_barrel[1], 0.0)
    glBegin(GL_POLYGON)
    glColor3f(150/255,62/255,0)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides)     
        sine  = radius * sin(i*2*pi/sides)   
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()      

def draw_cajas():
    glPushMatrix()
    glTranslatef(0,-0.6,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.0,0)
    glVertex3f(0.94,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.0,0)
    glVertex3f(0.88,0.0,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.86,-0.1,0.0)
    glVertex3f(0.94,0.0,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.94,-0.1,0.0)
    glVertex3f(0.86,0.0,0.0)
    glEnd()
    glPopMatrix()  

    #2dacaja
    glPushMatrix()
    glTranslatef(0.04,-0.5,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.0,0)
    glVertex3f(0.94,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.0,0)
    glVertex3f(0.88,0.0,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.86,-0.1,0.0)
    glVertex3f(0.94,0.0,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.94,-0.1,0.0)
    glVertex3f(0.86,0.0,0.0)
    glEnd()
    glPopMatrix()  

    glPushMatrix()
    glTranslatef(-1.5,0.9,0)
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(222/255,222/255,222/255)
    glVertex3f(0.95,-0.03,0)
    glVertex3f(0.85,-0.03,0)
    glVertex3f(0.85,-0.05,0)
    glVertex3f(0.95,-0.05,0)
    glEnd()
    glPopMatrix()  

def draw_barril():
    glPushMatrix()
    glTranslatef(-1.5,0.3,0)

    glBegin(GL_QUADS)
    glColor3f(0,105/255,12/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(2/255,66/255,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(2/255,66/255,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

def draw_barriltwo():
    glPushMatrix()
    glTranslatef(-1.65,-0.7,0)

    glBegin(GL_QUADS)
    glColor3f(230/255,158/255,2/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(54/255,0,161/255)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(54/255,0,161/255)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

#tercer barril
    glPushMatrix()
    glTranslatef(-1.75,-0.7,0)

    glBegin(GL_QUADS)
    glColor3f(32/255,0,97/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(232/255,135/255,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(232/255,135/255,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

    #dalkq 

    glPushMatrix()
    glTranslatef(-1.65,-0.51,0)

    glBegin(GL_QUADS)
    glColor3f(0,140/255,158/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(191/255,0,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(191/255,0,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

def draw_bote():
    glBegin(GL_QUADS)
    glColor3f(19/255,0,191/255)
    glVertex3f(0.98,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.05,0)
    glVertex3f(0.98,0.05,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,0.03,0.0)
    glVertex3f(0.85,0.03,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,0.02,0.0)
    glVertex3f(0.85,0.02,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,-0.08,0)
    glVertex3f(0.85,-0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,-0.07,0)
    glVertex3f(0.85,-0.07,0)
    glEnd()

def draw_letrero():
    
    glPushMatrix()
    glTranslatef(1.75,0.6,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.1,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.1,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(230/255,158/255,2/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  

    glPushMatrix()
    glTranslatef(1.8,0.7,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.2,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.2,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(173/255,0,173/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  

    glPushMatrix()
    glTranslatef(0,-0.42,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.2,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.2,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0,219/255,37/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  
    
    glPushMatrix()
    glTranslatef(0.1,-0.32,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.1,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.1,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(255/255,225/255,28/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix() 

def draw_explosiva():
    glBegin(GL_QUADS)
    glColor3f(156/255,156/255,156/255)
    glVertex3f(-0.65,-0.3,0)
    glVertex3f(-0.55,-0.3,0)
    glVertex3f(-0.55,-0.4,0)
    glVertex3f(-0.65,-0.4,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(156/255,156/255,156/255)
    glVertex3f(-0.59,-0.25,0)
    glVertex3f(-0.61,-0.25,0)
    glVertex3f(-0.61,-0.4,0)
    glVertex3f(-0.59,-0.4,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(138/255,138/255,138/255)
    glVertex3f(-0.65,-0.23,0)
    glVertex3f(-0.55,-0.23,0)
    glVertex3f(-0.55,-0.25,0)
    glVertex3f(-0.65,-0.25,0)
    glEnd()

def draw_platano():
    glPushMatrix()
    glScale(0.8,0.8,0)
    glTranslatef(posicion_platano[0], posicion_platano[1], 0.0)
    glRotatef(rotacion_platano,0.0,0.0,1.0)

    glBegin(GL_POLYGON)
    glColor3f(0.9, 1.0, 0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.08,0.1,0.0)
    glVertex3f(0.06,0.05,0.0)
    glVertex3f(0.06,0.0,0.0)
    glVertex3f(0.07,-0.05,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0.12,-0.1,0.0)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(0.08,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,0.12,0.0)
    glVertex3f(0.08,0.12,0.0)

    glEnd()

    glPopMatrix()
