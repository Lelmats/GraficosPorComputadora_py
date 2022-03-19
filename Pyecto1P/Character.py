from OpenGL.GL import *
from glew_wish import *
import glfw
import math

class Player():

    tiempo_anterior = 0.0 
    velocidad = 0.5
    velocidad_x = 0.5
    velocidad_y = 0.5
    IS_JUMPING = False
    IS_FALLING = False
    JUMP = False
    posicion_triangulo_x = -0.6
    posicion_triangulo_y = -0.65
    posicion_triangulo_z = 0
    posicion_y_triangulo_anterior = 0.0

    def draw(self):

        glPushMatrix()
        glTranslatef(self.posicion_triangulo_x, self.posicion_triangulo_y,0.0)

        glBegin(GL_TRIANGLES)

        # if self.colisionando():
        #     glColor3f(0,0,1)
        #     glfw.destroy_window(window)
        # else:
        #     glColor3f(1,0,0.7)

        # cantidad_movimiento = self.velocidad * tiempo_delta

        # if self.colisionando_escaleras() and estado_tecla_arriba == glfw.PRESS :
        #     posicion_triangulo_y = posicion_triangulo_y + cantidad_movimiento

        # if self.colisionando_escaleras() and estado_tecla_abajo == glfw.PRESS:
        #     posicion_triangulo_y = posicion_triangulo_y - cantidad_movimiento
    
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

    def actualizar(self, window, tiempo_delta): 
        global tiempo_anterior
        global estado_tecla_arriba, estado_tecla_abajo
        # global posicion_triangulo_x, posicion_triangulo_y, posicion_triangulo_z, posicion_y_triangulo_anterior

        # tiempo_actual = glfw.get_time()
        # #Cuanto tiempo paso entre la ejecucion actual
        # #y la inmediata anterior de esta funcion
        # tiempo_delta = tiempo_actual - tiempo_anterior

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
        cantidad_movimiento = self.velocidad * tiempo_delta

        # if estado_tecla_arriba == glfw.PRESS:
        #     posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
        if estado_tecla_derecha == glfw.PRESS:
            self.posicion_triangulo_x = self.posicion_triangulo_x + cantidad_movimiento
        # if estado_tecla_abajo == glfw.PRESS:
        #     posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
        if estado_tecla_izquierda == glfw.PRESS:
            self.posicion_triangulo_x = self.posicion_triangulo_x - cantidad_movimiento



        poder_salto = 1.5
        vel_y = self.velocidad_y * tiempo_delta * poder_salto
        gravedad = -0.3
        cantidad_de_salto = 0.1
        estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
        
        if self.JUMP is False and self.IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
            self.JUMP = True
            self.posicion_y_triangulo_anterior = self.posicion_triangulo_y

        if self.JUMP is True:
            # Añade a la y la velocidad_y a la velocidad anteiror
            # Añade la velocidad del salto
            self.posicion_triangulo_y += vel_y
            self.IS_JUMPING = True

        # Ver si ya se paso de burger
        if self.IS_JUMPING:
            if self.posicion_triangulo_y - self.posicion_y_triangulo_anterior >= cantidad_de_salto:
                # print("Bruhc")
                self.JUMP = False
                vel_y = gravedad * tiempo_delta
                self.posicion_triangulo_y += vel_y
                self.IS_FALLING = True

        if self.IS_FALLING: 
            vel_y = gravedad * tiempo_delta
            self.posicion_triangulo_y += vel_y

            if self.posicion_triangulo_y <= self.posicion_y_triangulo_anterior:
                self.IS_JUMPING = False
                self.JUMP = False
                self.IS_FALLING = False
                self.posicion_triangulo_y = self.posicion_y_triangulo_anterior   

        # tiempo_anterior = self.tiempo_actual