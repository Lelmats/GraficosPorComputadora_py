from OpenGL.GL import *
from glew_wish import *
import glfw

color = [0.6, 0.1, 0.7]
posicion = [0.2,0,0]
velocidad = 0.01
posicion_cuadrado = [-0.2,0.0,0.0]
window = None

def actualizar():
    global window
    global posicion
    global posicion_cuadrado

    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    #revisamos estados y realizamos acción
    if estado_tecla_arriba == glfw.PRESS:
        posicion[1] = posicion[1] + velocidad
    if estado_tecla_derecha == glfw.PRESS:
        posicion[0] = posicion[0] + velocidad
    if estado_tecla_abajo == glfw.PRESS:
        posicion[1] = posicion[1] - velocidad
    if estado_tecla_izquierda == glfw.PRESS:
        posicion[0] = posicion[0] - velocidad

    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)


    #revisamos estados y realizamos acción awsd
    if estado_tecla_w == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] + velocidad
    if estado_tecla_s == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] - velocidad    
    if estado_tecla_d == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] + velocidad
    if estado_tecla_a == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] - velocidad

def draw():

    glPushMatrix()
    glTranslatef(posicion[0], posicion[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(color[0],color[1],color[1])

    glVertex3f(-0.2,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,-0.2,0)
    glVertex3f(-0.2,-0.2,0)

    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(color[0],color[1],color[1])

    glVertex3f(-0.2,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,-0.2,0)
    glVertex3f(-0.2,-0.2,0)

    glEnd()
    glPopMatrix()
    
    
def main():
    global window
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Mi ventana", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    #Establecer Contexto
    glfw.make_context_current(window)

    #inicializar Glew
    glewExperimental = True
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    
    #Imprimir Version
    version = glGetString(GL_VERSION)
    print(version)
 
    #Establecer el key callback
    # glfw.set_key_callback(window, key_callback)

    #Draw Loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0, 800, 800)
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

if __name__ =="__main__":
    main()