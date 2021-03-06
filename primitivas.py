from OpenGL.GL import *
from glew_wish import *
import glfw



def draw():
    glBegin(GL_TRIANGLES)

    glColor3f(0,0,0)

    glVertex3f(-1,0,0)
    glVertex3f(0,1,0)
    glVertex3f(1,0,0)

    glEnd()

def draw_point():
    glBegin(GL_POINT)
    glColor3f(1,0,0)

    glVertex3f(-0.5,0,0)
    glVertex3f(0.2,0,0)

    glEnd()
    
def draw_lines():
    glBegin(GL_LINES)
    glColor3f(1,0,0)

    glVertex3f(-0.5,0,0)
    glVertex3f(0.2,0,0)

    glEnd()

def draw_striplines():
    glBegin(GL_LINE_STRIP)
    glColor3f(1,0,0)

    glVertex3f(-0.5,0,0)
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,0.6,0)
    glVertex3f(0.5,-0.7,0)

    glEnd()

def draw_striptrangles():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1,0,0)

    glVertex3f(-0.5,0,0)
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,0.6,0)
    glVertex3f(0.5,-0.7,0)

    glEnd()

def draw_polygon():
    glBegin(GL_POLYGON)
    glColor3f(1,0,0)

    glVertex3f(-0.5,0,0)
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,0.6,0)
    glVertex3f(0.5,-0.7,0)
    glVertex3f(0.5,1,0)

    glEnd()
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
 
 
    #Draw Loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0, 800, 600)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        # draw_lines()
        # draw_draw_striplines()
        draw_point()
        

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ =="__main__":
    main()