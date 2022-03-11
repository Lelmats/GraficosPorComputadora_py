class Modelo:
    @property
    def posicion_x(self):
        return self._posicion_x
    @posicion_x.setter
    def posicion_x(self,posicion_x):
        self._posicion_x = posicion_x

    @property
    def posicion_y(self):
        return self._posicion_y
    @posicion_x.setter
    def posicion_y(self,posicion_y):
        self._posicion_y = posicion_y

    @property
    def posicion_z(self):
        return self._posicion_z
    @posicion_z.setter
    def posicion_z(self,posicion_z):
        self._posicion_z = posicion_z


    def __init__(self, posicion_x = 0.0, posicion_y = 0.0, posicion_z = 0.0):
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._posicion_z = posicion_z