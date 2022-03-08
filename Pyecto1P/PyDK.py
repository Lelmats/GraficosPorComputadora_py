from fnmatch import translate
from OpenGL.GL import *
from glew_wish import *
from math import *
from pygame import mixer
import pygame
import math
import glfw

from Character import *
from draws import *
from collision_escaleras import *
from draw_stairs import *
from draw_plataforms import *

pygame.mixer.init()

# mixer.music.load("LVL_Music.wav")
# mixer.music.play(-1)

#proyecto parcial 1    

#unidades por segundo

window = None
tiempo_anterior = 0.0
posicion_cuadrado = [-0.4,0.9, 0.0]
velocidad_angular = 135.0


player = Character()
platano = Platano()


def actualizar_platano(tiempo_delta):
    global direccion_platano
    global velocidad_platano
    global posicion_platano
    global rotacion_platano

    cantidad_rotacion = velocidad_angular * tiempo_delta
    rotacion_platano = rotacion_platano + cantidad_rotacion
    if rotacion_platano > 360.0:
        rotacion_platano = rotacion_platano - 360.0

    cantidad_movimiento = velocidad_platano * tiempo_delta

    if direccion_platano == 1:
        posicion_platano[0] = posicion_platano[0] + cantidad_movimiento
        posicion_platano[1] = posicion_platano[1] + (
            math.sin((angulo_platano + -90) * pi / 180.0) * cantidad_movimiento
        )
        if posicion_platano[0] >= 1:
            direccion_platano = 0

    if direccion_platano == 0:
        posicion_platano[0] = posicion_platano[0] - cantidad_movimiento
        posicion_platano[1] = posicion_platano[1] - (
            math.sin((angulo_platano - 90) * pi / 180.0) * cantidad_movimiento
        )
        if posicion_platano[0] <= -1:
            direccion_platano = 1

def actualizar_barrel(tiempo_delta):
    global tiempo_anterior
    global posicion_barrel

    cantidad_movimiento = platano.velocidad_barrel * tiempo_delta

    if platano.direccion_barrelx == 0:
        platano.posicion_barrel_x = platano.posicion_barrel_x - cantidad_movimiento
    elif platano.direccion_barrelx == 1:    
        platano.posicion_barrel_x = platano.posicion_barrel_x + cantidad_movimiento

    # elif direccion_barrely == 1: 
    #     posicion_barrel[1] = posicion_barrel[1] + cantidad_movimiento

    if platano.posicion_barrel_x <= -0.45 and platano.direccion_barrelx == 0:
        platano.direccion_barrelx = 1
        if platano.direccion_barrely == 0:
            platano.posicion_barrel_y = platano.posicion_barrel_y - (cantidad_movimiento + 0.3)
        
    if platano.posicion_barrel_x >= 0.75 and platano.direccion_barrelx == 1:
        platano.direccion_barrelx = 0
        if platano.direccion_barrely == 0:
            platano.posicion_barrel_y = platano.posicion_barrel_y - (cantidad_movimiento + 0.3)
    
    if platano.posicion_barrel_y <= -0.9:
        # platano.posicion_barrel = [-0.4,0.85, 0.0]
        platano.velocidad_barrel = platano.velocidad_barrel + 0.2
    
def actualizar():    
    global window
    global tiempo_anterior    
    global estado_tecla_arriba
    global cantidad_movimiento
    global estado_tecla_abajo
    global posicion_barrel, posicion_cuadrado
    global angulo_platano


    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    # estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    # estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    # estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    # estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = player.velocidad * tiempo_delta
    # if estado_tecla_arriba == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
    if estado_tecla_derecha == glfw.PRESS:
        player.posicion_triangulo_x = player.posicion_triangulo_x + cantidad_movimiento
    # if estado_tecla_abajo == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
    if estado_tecla_izquierda == glfw.PRESS:
        player.posicion_triangulo_x = player.posicion_triangulo_x - cantidad_movimiento

    actualizar_barrel(tiempo_delta)
    actualizar_platano(tiempo_delta)

    poder_salto = 1.5
    vel_y = player.velocidad_y * tiempo_delta * poder_salto
    gravedad = -0.3
    cantidad_de_salto = 0.1
    estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
    
    if player.JUMP is False and player.IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
        player.JUMP = True
        player.posicion_y_triangulo_anterior = player.posicion_triangulo_y

    if player.JUMP is True:
        # Añade a la y la velocidad_y a la velocidad anteiror
        # Añade la velocidad del salto
        player.posicion_triangulo_y += vel_y
        player.IS_JUMPING = True

    # Ver si ya se paso de burger
    if player.IS_JUMPING:
        if player.posicion_triangulo_y - player.posicion_y_triangulo_anterior >= cantidad_de_salto:
            # print("Bruhc")
            player.JUMP = False
            vel_y = gravedad * tiempo_delta
            player.posicion_triangulo_y += vel_y
            player.IS_FALLING = True

    if player.IS_FALLING: 
        vel_y = gravedad * tiempo_delta
        player.posicion_triangulo_y += vel_y

        if player.posicion_triangulo_y <= player.posicion_y_triangulo_anterior:
            player.IS_JUMPING = False
            player.JUMP = False
            player.IS_FALLING = False
            player.posicion_triangulo_y = player.posicion_y_triangulo_anterior   

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (player.posicion_triangulo_x + 0.05 >= posicion_barrel[0] - 0.01
    and player.posicion_triangulo_x - 0.05 <= posicion_barrel[0] + 0.01 
    and player.posicion_triangulo_y + 0.05 >= posicion_barrel[1] - 0.01
    and player.posicion_triangulo_y - 0.05 <= posicion_barrel[1] + 0.01):
        colisionando = True
    if (player.posicion_triangulo_x + 0.05 >= posicion_cuadrado[0] - 0.01
    and player.posicion_triangulo_x - 0.05 <= posicion_cuadrado[0] + 0.01 
    and player.posicion_triangulo_y + 0.05 >= posicion_cuadrado[1] - 0.01
    and player.posicion_triangulo_y - 0.05 <= posicion_cuadrado[1] + 0.01):
        colisionando = True
    if (player.posicion_triangulo_x + 0.05 >= posicion_platano[0] - 0.02
    and player.posicion_triangulo_x - 0.05 <= posicion_platano[0] + 0.02 
    and player.posicion_triangulo_y + 0.05 >= posicion_platano[1] - 0.05
    and player.posicion_triangulo_y - 0.05 <= posicion_platano[1] + 0.05):
        colisionando = True
    return colisionando

def draw_triangulo():
    glPushMatrix()
    glTranslatef(player.posicion_triangulo_x, player.posicion_triangulo_y,0.0)

    glBegin(GL_TRIANGLES)
    if colisionando():
        glColor3f(0,0,1)
        glfw.destroy_window(window)
    else:
        glColor3f(1,0,0.7)

    if colisionando_escaleras() and estado_tecla_arriba == glfw.PRESS :
        player.posicion_triangulo_y = player.posicion_triangulo_y + cantidad_movimiento

    if colisionando_escaleras() and estado_tecla_abajo == glfw.PRESS:
        player.posicion_triangulo_y = player.posicion_triangulo_y - cantidad_movimiento
 
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()

    # glBegin(GL_LINE_LOOP)

    # glColor(1,1,1)
    # glVertex3f(-0.05, -0.05, 0)
    # glVertex3f(-0.05, 0.05, 0)
    # glVertex3f(0.05, 0.05, 0)
    # glVertex3f(0.05, -0.05, 0)

    # glEdnwad()
    glPopMatrix()
    
def draw_cuadrado():
    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.2, 0.21)

    glVertex3f(-0.1,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(-0.1,-0.1,0.0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(1,1,1)

    glVertex3f(-0.1,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(-0.1,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw():  
    draw_plataform_0_1()
    draw_escaleras()
    draw_escaleras_2()
    draw_escaleras_3()
    draw_escaleras_4()
    draw_escaleras_5()
    draw_plataform()
    draw_plataform_2()   
    draw_plataform_3()   
    draw_plataform_4()   
    draw_plataform_5()   
    draw_plataform_6()   
    draw_plataform_7()   
    draw_cuadrado()
    draw_barrel()
    draw_cajas()
    draw_explosiva()
    draw_bote()
    draw_letrero()
    draw_barril()
    draw_triangulo()
    draw_barriltwo()
    draw_platano()

def main():
    global window
    global tiempo_anterior
    width = 900
    height = 900
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
        glViewport(0,0,800,800)
        #Establecer color de borrado
        glClearColor(0,0,0,1)
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