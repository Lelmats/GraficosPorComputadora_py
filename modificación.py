from OpenGL.GL import *
from glew_wish import *
import glfw

color = [0.6, 0.1, 0.7]
posicion = [-0.4,0.2]
velocidad = 0.01

def key_callback(window, key, scancode, action, mods):
    global color
    global posicion
    global velocidad

    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    if key == glfw.KEY_R and action == glfw.PRESS:
        color = [1.0,0.0,0.0]
    if key == glfw.KEY_G and action == glfw.PRESS:
        color = [0.0,1.0,0.0]
    if key == glfw.KEY_B and action == glfw.PRESS:
        color = [0.0,0.0,1.0]

    #Presionar Arriba
    if key == glfw.KEY_UP and (action == glfw.PRESS or glfw.REPEAT):
        posicion[1] = posicion [1] + velocidad
        if posicion[1] >= 1:
            posicion[1] = -0.9999
    #Presionar Abajo
    if key == glfw.KEY_DOWN and (action == glfw.PRESS or glfw.REPEAT):
        posicion[1] = posicion [1] - velocidad
        if posicion[1] <= -1:
            posicion[1] = 0.9999
    #Presionar derecha
    if key == glfw.KEY_RIGHT and (action == glfw.PRESS or glfw.REPEAT):
        posicion[0] = posicion [0] + velocidad
        if posicion[0] >= 1:
            posicion[0] = -0.9999
    #Presionar izquierda
    if key == glfw.KEY_LEFT and (action == glfw.PRESS or glfw.REPEAT):
        posicion[0] = posicion [0] - velocidad
        if posicion[0] <= -1:
            posicion[0] = 0.9999

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
    
def draw_triangle():
    global color

    glPushMatrix()
    glTranslatef(posicion[0], posicion[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(color[1],color[1],color[0])

    #Manda vertices a dibujar
    glVertex3f(-0.08,-0.08,0)
    glVertex3f(0,0.08,0)
    glVertex3f(0.08,-0.08,0)

    glEnd()
    glPopMatrix()
def main():
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
    glfw.set_key_callback(window, key_callback)

    #Draw Loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0, 800, 800)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        draw()
        draw_triangle()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ =="__main__":
    main()