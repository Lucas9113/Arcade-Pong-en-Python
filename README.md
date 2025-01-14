# Mi Primer Proyecto en Python: Arcade Pong 🕹️  

¡Hola a todos!  
Mi nombre es **Lucas**, y este es mi primer proyecto subido a GitHub. 🎉  

Se trata de una versión del clásico juego arcade **Pong**, implementada en Python. Este proyecto forma parte de mi aprendizaje mientras realizo un máster en programación.  

---

## Descripción del Proyecto 🎮  
Este script recrea el juego **Pong** e incluye las siguientes características:  
- **Importación de módulos:** `turtle`, `random`, `winsound`.  
- **Identificación del ganador:** Determina el jugador que alcanza la puntuación objetivo.  
- **Efectos de sonido:** Reproducción de sonidos en golpes y anotaciones.  
- **Botón de pausa y salida:** Mejora la experiencia de juego.  

---

## Ejemplos del Código 🧩  

### Movimientos de las paletas  
```python
# Paleta izquierda
def paleta_izquierda_up():
    y = left_padel.ycor()
    if y < 290:
        left_padel.sety(y + 20)

def paleta_izquierda_down():
    y = left_padel.ycor()
    if y > -290:
        left_padel.sety(y - 20)

# Paleta derecha
def paleta_derecha_up():
    y = right_padel.ycor()
    if y < 290:
        right_padel.sety(y + 20)

def paleta_derecha_down():
    y = right_padel.ycor()
    if y > -290:
        right_padel.sety(y - 20)


# Rebote en las paletas

# Paleta izquierda
if ball.xcor() < -390 and left_padel.ycor() - 60 < ball.ycor() < left_padel.ycor() + 60:
    ball.setx(-390)
    ball.dx *= -1
    ball.dx *= 1.0
    ball.dy *= 1.0
    sonido_golpe()
``` 

## Cómo Jugar 🕹️ 
1. **Clona este repositorio**:
 ```bash
 git clone https://github.com/Lucas9113/Arcade-Pong-en-Python.git
 ```
2. **Instala las dependencia necesarias**:
```bash
pip install turtle
```
3. **Ejecuta el script**:
```bash
Python arcade_pong.py
```
