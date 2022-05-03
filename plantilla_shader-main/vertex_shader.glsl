#version 330 core
layout (location = 0) in vec4 position;
in vec4 color;

//Los out van hacia el fragment shader
out vec4 fragmentColor;
//hay que establecer posicion en la propiedad
//gl_Position que es del tipo vec4
void main() {
    gl_Position = position;
    fragmentColor = color;
}
