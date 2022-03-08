#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math

rotacion = 0.0
escala = 0.5
posicion_triangulo = 1.0

def actualizar():
    global rotacion
    global escala
    global posicion_triangulo
    rotacion = rotacion + 0.05
    if(rotacion >= 360.0):
        rotacion = 0.0
    escala = escala + 0.0005
    if (escala >= 3.0):
        escala = 0.5
    posicion_triangulo = posicion_triangulo + 0.005
    if (posicion_triangulo >= 0.5):
        posicion_triangulo = -1.0

def draw_ejes():
    glBegin(GL_LINES)
    glColor(0,0,0)
    glVertex3f(-1,0,0)
    glVertex3f(1,0,0)
    glVertex3f(0,1.0,0)
    glVertex3f(0,-1.0,0)
    glEnd()

def draw_triangulo():
    global rotacion
    global escala
    global posicion_triangulo
    glPushMatrix()

    #respetar orden: translate -> rotate -> scale
    glTranslatef(posicion_triangulo,posicion_triangulo,0.0)
    glRotatef(rotacion,0.0,0.5,1.0)
    glScalef(escala,escala, 1.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(0,0.5,1)
    
    #Manda vertices a dibujar
    glVertex3f(-0.1,-0.1,0)
    glVertex3f(0,0.1,0)
    glVertex3f(0.1,-0.1,0)
    glEnd()
    glPopMatrix()

def draw_cuadrado():
    glPushMatrix()
    glTranslatef(-0.4,-0.25,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.0,1.0)

    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(-0.1,-0.1,0.0)
    glVertex3f(-0.1,0.1,0.0)

    glVertex3f(-0.05,-0.1,0.0)
    glVertex3f(0.05,-0.1,0.0)
    glVertex3f(0.05,-0.2,0.0)
    glVertex3f(-0.05,-0.2,0.0)

    glEnd()
    glPopMatrix()

def draw():
    draw_triangulo()
    draw_cuadrado()
    draw_ejes()

def main():
    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #actualizar
        actualizar()
        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()