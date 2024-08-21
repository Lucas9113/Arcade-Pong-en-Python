"Script basico para crear el juego Arcade pong con la libreria turtle"

# Importamos la libreria necesaria en caso de no tenrla instalada usamos pip install 

import turtle
import random
import winsound



# Creamos la pantalla(screen) donde vamos a jugar

screen = turtle.Screen()
screen.title('Arcade Pong') # titulo de de la pantalla
screen.bgcolor('black') # color de la pantalla del juego
screen.setup(1000,700) # dimensiones de la pantalla
screen.tracer(0)



# inicializamos variables: bulce principal, puntajes, velocidad de la bola, pausa
bucle_principal = True
en_pausa = False
score_left = 0
score_rigth = 0
ball_speed = 0.10


# Incluimos sistema de puntajes
puntaje = turtle.Turtle()
puntaje.color('white')
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0,280)


# mostramos el puntaje por pantalla
def puntaje_display():
    puntaje.clear()
    puntaje.write(f'Juador 1:  {score_left}    |   Jugador 2:  {score_rigth}', align='center', font=('Courier',15, 'bold italic' ))


puntaje_display()


# mostramos opcion de salida del juego

def mensaje_quit():
    quit = turtle.Turtle()
    quit.color('white')
    quit.penup()
    quit.hideturtle()
    quit.goto(0,-299)
    quit.write(f'Exit : Q', align='center', font=('Courier',15, 'bold italic'))

mensaje_quit()



# creamos la opcion de pausa

pause = turtle.Turtle()
pause.color('white')
pause.penup()
pause.hideturtle()
pause.goto(0,-326)
pause.write(f'Pause : P', align='center', font=('Courier',15, 'bold italic'))

# creamos funcion para la opcionde pausa
def pausar():
    global en_pausa
    en_pausa = not en_pausa

    
# creamos la funcion de opcion de salida con Q

def opcion_quit():
    global bucle_principal
    bucle_principal = False
    turtle.bye()


# mostrar ganador
def es_ganador():
    if score_left > score_rigth:
        ganador1 = turtle.Turtle()
        ganador1.color('Green')
        ganador1.penup()
        ganador1.hideturtle()
        ganador1.goto(0,200)
        ganador1.write(f'  Ganador: Jugador 1 :)', align='center', font=('Courier', 30, 'normal'))
    else:
        ganador2 = turtle.Turtle()
        ganador2.color('Green')
        ganador2.penup()
        ganador2.hideturtle()
        ganador2.goto(0,200)
        ganador2.write(f'  Ganador: Jugador 2 :)', align='center', font=('Courier', 30, 'normal'))
            




# mensaje de fin de juego

def mensaje_fin():
    msj_fin = turtle.Turtle()
    msj_fin.color('red')
    msj_fin.penup()
    msj_fin.hideturtle()
    msj_fin.goto(0,0)
    msj_fin.write(f'    JUEGO TERMINADO\n  Pulsa "Q" para salir', align='center', font=('Courier', 25, 'bold'))

      
    


#////////////////////////////////////////////////// efectos de sonido /////////////////////////////////////////////////////////

def sonido_punto():
    winsound.PlaySound("Speech On.wav", winsound.SND_ASYNC)

def sonido_golpe():
    winsound.PlaySound("Speech Misrecognition.wav", winsound.SND_ASYNC)        
    

# //////////////////////// Creacion de paletas y bola /////////////////////////////////

# Creacion de la paleta izquierda
left_padel = turtle.Turtle()
left_padel.speed(1)
left_padel.shape('square')
left_padel.color('white')
left_padel.shapesize(stretch_wid=5, stretch_len=1)
left_padel.penup()
left_padel.goto(-400,0)


# Creacion linea media
lin_med = turtle.Turtle()
lin_med.shape('square')
lin_med.color('white')
lin_med.shapesize(stretch_wid=20, stretch_len=0.05)
lin_med.penup()
lin_med.goto(0,0)


# creacion paleta derecha
right_padel = turtle.Turtle()
right_padel.speed(1)
right_padel.shape('square')
right_padel.color('white')
right_padel.shapesize(stretch_wid=5, stretch_len=1)
right_padel.penup()
right_padel.goto(400,0)



# creacion pelota
ball = turtle.Turtle()
ball.speed('fastest')
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dy = random.choice([-ball_speed, ball_speed])
ball.dx = random.choice([-ball_speed, ball_speed])

# movimientos paletas
## paleta izquierda

def paleta_izquierda_up():
    y = left_padel.ycor()
    if y < 290:
        left_padel.sety(y +20)

def paleta_izquierda_down():
    y = left_padel.ycor()
    if y > -290:
        left_padel.sety(y -20)         



## paleta derecha

def paleta_derecha_up():
    y = right_padel.ycor()
    if y < 290:
        right_padel.sety(y +20)


def paleta_derecha_down():
    y = right_padel.ycor()
    if y > -290:
        right_padel.sety(y -20)



# aasignacion de teclas
screen.listen()
screen.onkeypress(paleta_izquierda_up, 'w')
screen.onkeypress(paleta_izquierda_down, 's')
screen.onkeypress(paleta_derecha_up, "Up")
screen.onkeypress(paleta_derecha_down, "Down")
screen.onkeypress(opcion_quit, 'q')
screen.onkeypress(pausar, "p")


#/////////////////////////  Bucle prrincipal para dar inicio al juego /////////////////////////////
while bucle_principal:
   

    screen.update()
    if not en_pausa: 
     # iniciamos la posicion de la pelota

      ball.setx(ball.xcor() + ball.dx)
      ball.sety(ball.ycor() + ball.dy)

     # creamos el rebote tanto en la parte superior como inferior de la pantalla

      if ball.ycor() > 340:
         ball.sety(340)
         ball.dy *=-1


      if ball.ycor() < -340:
         ball.sety(-340)
         ball.dy *=-1


      # Creamos el rebote en las paletas

      ## Paleta izquierda

      # if ball.xcor() < -390 and left_padel.ycor() - 60 < ball.ycor() < left_padel.ycor() + 60:
      # (ball.dx < 0 and ball.xcor() < -390 and ball.xcor() > -400) and (left_padel.ycor() -60 < ball.ycor() < left_padel.ycor() +60 ):
      if ball.xcor() < -390 and left_padel.ycor() - 60 < ball.ycor() < left_padel.ycor() + 60:
          ball.setx(-390)
          ball.dx *=-1
          ball.dx *= 1.0
          ball.dy *= 1.0
          sonido_golpe()
       

      ## paleta derecha

    
      # if (ball.dx > 0 and ball.xcor() > 390 and ball.xcor() < 400) and (rigth_padel.ycor() - 60 < ball.ycor() < rigth_padel.ycor() + 60 ):

      if ball.xcor() > 390 and right_padel.ycor() - 60 < ball.ycor() < right_padel.ycor() + 60:
         ball.setx(390)
         ball.dx *=-1
         ball.dx *= 1.0
         ball.dy *= 1.0
         sonido_golpe()
        



      ## Si la pelota pasa algunos de los extremos izuierdo o derecho actualizamos puntaje del jugador correspondiente

      if ball.xcor() > 490:
         score_left += 1
         ball.goto(0,0)
         ball.dx = random.choice([-ball_speed, ball_speed])
         ball.dy = random.choice([-ball_speed, ball_speed])
         sonido_punto()
         puntaje_display()

      if ball.xcor() < -490:
         score_rigth += 1
         ball.goto(0,0)
         ball.dx = random.choice([-ball_speed, ball_speed])
         ball.dy = random.choice([-ball_speed, ball_speed])
         sonido_punto()
         puntaje_display()
 

      if (score_left == 5) or (score_rigth == 5) or (score_left + score_rigth == 5):
         es_ganador()
         mensaje_fin()
         bucle_principal = False
    
      



screen.mainloop()