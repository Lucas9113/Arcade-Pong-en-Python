### Mi primer proyecto Python: Arcade pong

 Hola buenas a todos! Mi nombre es Lucas!!
 
 **Este es mi primero proyecto subido a Gthub, el cual se trata de script del clasico juego arcade pong.**
 
 Como bien dije antes este es mi primer proyecto subido a GitHub y me encuentro actualmente realizando un master en programacion.
 En este script algo de lo que podemos encontrar es:
 - **Importacion de los modulos: turtle, random, windsound**
 - **Identificacion de ganador**
 - **Efectos de sonido en los golpes como en las anotaciones**
 - **Boton de pausa y salida **





###Algunos fragmentos que encontraremos en el codigo


###Movimientos de las paletas

```python
def paleta_izquierda_up():
    y = left_padel.ycor()
    if y < 290:
        left_padel.sety(y +20)

def paleta_izquierda_down():
    y = left_padel.ycor()
    if y > -290:
        left_padel.sety(y -20)         



##  paleta derecha

def paleta_derecha_up():
    y = right_padel.ycor()
    if y < 290:
        right_padel.sety(y +20)


def paleta_derecha_down():
    y = right_padel.ycor()
    if y > -290:
        right_padel.sety(y -20)
```

### Colicion de bola con las palas

```python
#  # Creamos el rebote en las paletas

      ## Paleta izquierda

if ball.xcor() < -390 and left_padel.ycor() - 60 < ball.ycor() < left_padel.ycor() + 60:
          ball.setx(-390)
          ball.dx *=-1
          ball.dx *= 1.0
          ball.dy *= 1.0
          sonido_golpe()
```

Espero que ayude al que nesecite una ayuda/guia como asi tambien me digan si hay algo que corrgir para que quede mejor.

####Saludos!

###End
