from fnmatch import translate
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

#unidades por segundo
velocidad = 0.5
posicion_triangulo = [-0.3,-0.75,0.0]
posicion_cuadrado = [-0.4,0.9, 0.0]
posicion_plataforma_0_1 = [0,-0.9, 0.0]
posicion_plataforma_1 = [0.2,-0.9, 0.0]
posicion_plataforma_2 = [0.2,0.3, 0.0]
posicion_plataforma_3 = [0.2,0.6, 0.0]
posicion_plataforma_4 = [0.2,0.9, 0.0]
posicion_plataforma_5 = [0.2,1.2, 0.0]
posicion_plataforma_6 = [0.2,1.5, 0.0]
posicion_plataforma_7 = [0.6,1.5, 0.0]
posicion_escaleras = [0.7,-0.7,0.0]
posicion_escaleras_2 = [-0.5,-0.4,0.0]
posicion_escaleras_3 = [0.7,-0.1,0.0]
posicion_escaleras_4 = [-0.5,0.2,0.0]
posicion_escaleras_5 = [0.7,0.6,0.0]
window = None

tiempo_anterior = 0.0

def actualizar():
    global tiempo_anterior
    global window
    global posicion_triangulo
    global posicion_cuadrado
    global estado_tecla_arriba
    global cantidad_movimiento
    global estado_tecla_abajo
    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta
    # if estado_tecla_arriba == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
    if estado_tecla_derecha == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] + cantidad_movimiento
    # if estado_tecla_abajo == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
    if estado_tecla_izquierda == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] - cantidad_movimiento

    # if estado_tecla_w == glfw.PRESS:
    #     posicion_cuadrado[1] = posicion_cuadrado[1] + cantidad_movimiento
    # if estado_tecla_d == glfw.PRESS:
    #     posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
    # if estado_tecla_s == glfw.PRESS:
    #     posicion_cuadrado[1] = posicion_cuadrado[1] - cantidad_movimiento
    # if estado_tecla_a == glfw.PRESS:
    #     posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento

    tiempo_anterior = tiempo_actual
    
def colisionando():
    colisionando = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (posicion_triangulo[0] + 0.05 >= posicion_plataforma_0_1[0] - 0.7
    and posicion_triangulo[0] - 0.05 <= posicion_plataforma_0_1[0] + 0.2 
    and posicion_triangulo[1] + 0.05 >= posicion_plataforma_0_1[1] - 0
    and posicion_triangulo[1] - 0.05 <= posicion_plataforma_0_1[1] + 0.099):
        colisionando = True
    if (posicion_triangulo[0] + 0.05 >= posicion_plataforma_1[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_plataforma_1[0] + 0.8 
    and posicion_triangulo[1] + 0.05 >= posicion_plataforma_1[1] - 0
    and posicion_triangulo[1] - 0.05 <= posicion_plataforma_1[1] + 0.099):
        colisionando = True
    return colisionando

def colisionando_escaleras():
    colisionando_escaleras = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_2[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_2[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_2[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_2[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_3[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_3[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_3[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_3[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_4[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_4[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_4[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_4[1] + 0.22):
        colisionando_escaleras = True
    if (posicion_triangulo[0] + 0.05 >= posicion_escaleras_5[0] - 0.0
    and posicion_triangulo[0] - 0.05 <= posicion_escaleras_5[0] + 0.1 
    and posicion_triangulo[1] + 0.05 >= posicion_escaleras_5[1] - 0.1
    and posicion_triangulo[1] - 0.05 <= posicion_escaleras_5[1] + 0.22):
        colisionando_escaleras = True
    return colisionando_escaleras

def draw_triangulo():
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1],0.0)

    glBegin(GL_TRIANGLES)
    if colisionando():
        glColor3f(0,0,1)
        
    else:
        glColor3f(1,0,0.7)

    if colisionando_escaleras() and estado_tecla_arriba == glfw.PRESS :
        posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
        
    if colisionando_escaleras() and estado_tecla_abajo == glfw.PRESS:
        posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()

    glBegin(GL_LINE_LOOP)

    glColor(1,1,1)
    glVertex3f(-0.05, -0.05, 0)
    glVertex3f(-0.05, 0.05, 0)
    glVertex3f(0.05, 0.05, 0)
    glVertex3f(0.05, -0.05, 0)

    glEnd()
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

def draw_plataform_0_1():
    glPushMatrix()
    glTranslatef(posicion_plataforma_0_1[0], posicion_plataforma_0_1[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9,0.1, 0.2)

    glVertex3f(-0.7,0,0.0)
    glVertex3f(0.2,0,0.0)
    glVertex3f(0.2,0.1,0.0)
    glVertex3f(-0.7,0.1,0.0)

    glEnd()
    glBegin(GL_LINE_LOOP)

    glColor(1,1,1)
    glVertex3f(-0.7,0,0.0)
    glVertex3f(0.2,0,0.0)
    glVertex3f(0.2,0.1,0.0)
    glVertex3f(-0.7,0.1,0.0)

    glEnd()
    glPopMatrix()
    
def draw_plataform():
    glPushMatrix()
    glTranslatef(posicion_plataforma_1[0], posicion_plataforma_1[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0,0,0.0)
    glVertex3f(0.8,0.1,0.0)
    glVertex3f(0.8,0.2,0.0)
    glVertex3f(0,0.1,0.0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(1,1,1)
    glVertex3f(0,0,0.0)
    glVertex3f(0.8,0.1,0.0)
    glVertex3f(0.8,0.2,0.0)
    glVertex3f(0,0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_2():
    glPushMatrix()
    glTranslatef(posicion_plataforma_2[0], posicion_plataforma_2[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0.7,-0.9,0.0)
    glVertex3f(-0.9,-0.8,0.0)
    glVertex3f(-0.9,-0.7,0.0)
    glVertex3f(0.7,-0.8,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_3():
    glPushMatrix()
    glTranslatef(posicion_plataforma_3[0], posicion_plataforma_3[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(-0.8,-0.9,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glVertex3f(-0.8,-0.8,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_4():
    glPushMatrix()
    glTranslatef(posicion_plataforma_4[0], posicion_plataforma_4[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(0.7,-0.9,0.0)
    glVertex3f(-0.9,-0.8,0.0)
    glVertex3f(-0.9,-0.7,0.0)
    glVertex3f(0.7,-0.8,0.0)

    glEnd()
    glPopMatrix()

def draw_plataform_5():
    glPushMatrix()
    glTranslatef(posicion_plataforma_5[0], posicion_plataforma_5[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.1, 0.2)

    glVertex3f(-0.8,-0.9,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glVertex3f(-0.8,-0.8,0.0)

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
    draw_triangulo()


def main():
    global window

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