#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from cmath import cos, pi, sin
from Asteroide import Asteroide
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
import dis

from Nave import *

#unidades por segundo
posicion_cuadrado = [-0.2, 0.0, 0.0]
window = None

tiempo_anterior = 0.0

nave = Nave()
asteroide = Asteroide()


def actualizar():
    global tiempo_anterior
    global window

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
   
    nave.actualizar(window, tiempo_delta)
    #actualizar_bala(tiempo_delta)
    tiempo_anterior = tiempo_actual
    
def colisionando():
    colisionando = False
    #Método de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado

    return colisionando

def draw():
    asteroide.dibujar()
    #draw_bala()
    nave.dibujar()

def main():
    global window

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
