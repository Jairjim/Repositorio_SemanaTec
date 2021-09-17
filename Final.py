# Semana Tec: Herramientras computacionales, el arte de la programación
#A01379810 -- Jimena Trachtman RIvera
#A01745310 -- Yael Ariel Márquez
#A01632853 -- Jair Josué Jiménez
#
import HCRfinal #importamos animación de "how to cross a river"

import pygame #importamos librería PyGame para hacer un ambiente didáctico e interfaz para la animación

def redrawGameWindow(Dir, p1, p2): #creamos una clase para dos jugadores, P1 y P2
    global x, y, Side_A, Side_B #definimos el lado de salida de los personajes y el lado de llegada, cruzando el rio
            
    win.blit(bg,(0,0)) #creamos el canvas para el fondo de nuestro juego
    ypos = 300
    for item in Side_A: #para el personaje que se encuentra en el lado de salida del juego
        win.blit(item,(5,ypos))
        ypos = ypos - 60 #determinamos el lugar en posición de y de nuestro elemento

    ypos = 300
    for item in Side_B: #aqui declaramos el lado de llegada de nuestro personaje
        win.blit(item,(450,ypos)) #sumamos 400 px para llegar al otro lado
        ypos = ypos - 60 #volvemos a colocar en posición a nuestro personaje pero del otro lado del río

    if p1 != 'Unknown': #en este if determinamos un posible primer movimiento de alguno de nuestros personajes
        if right: #declaramos la posición de nuestro barco en coordenadas x, y
            win.blit(BoatRight,(x,y))
            win.blit(farmer,(x,y-50)) #posicionamos el barco
            if p2 != farmer: #si nuestro segundo jugador, en este caso el granjero está cerca o va realizar un viaje, se sube
                win.blit(p2,(x+50,y-50))           
        elif left: #si está del lado izquiero nuestro barco e igualmente el granjero entonces
            win.blit(BoatLeft,(x,y)) #se posiciona el barco
            win.blit(farmer,(x,y-50))
            if p2 != farmer: # y se sube nuestro granjero
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(char,(x, y))
    pygame.display.update() #actualizamos nuestro juego con las nuevas coordenadas y posiciones de nuestros elementos

def get_characters(d, p1, p2): #qui incluimos y declaramos la presencia de nuestros personajes
    if p2 == 'Zorro':
        character = fox #incluimos en personaje a un zorro
    elif p2 == 'Maiz':
        character = corn #incluimos en personaje a un saco de maíz
    elif p2 == 'Ganzo':
        character = duck #incluimos en personaje a un pato
    else:
        character = farmer #incluimos en personaje a nuestro principal que es el granjero
    return (d, farmer, character)

def Embark_characters(B, p1, p2): #aqui ya emoezamos a declarar los miviemtnos de los personajes en nuestro barco
    if p1 in B:
        B.remove(p1) #si nuestro primer personaje llega a la otro lado del río, se baja
    if p2 in B:
        B.remove(p2) #si nuestro segundo personaje llega a la otro lado del río, se baja
 
def Disembark_characters(A, p1, p2):
    if p1 not in A:
        A.append(p1) #si nuestro primer personaje no está del lado A entonces se sube al barco
    if p2 not in A:
        A.append(p2) #si nuestro segundo personaje no está del lado A entonces se sube al barco
    
def HCR_animacion(P):
    global x, y, left, right, vel #declaramos variables globales del juego
    global Side_A, Side_B #declaramos como variable global nuestro lado de salida y llegada

    clock = pygame.time.Clock() #incluimos un reloj en el juego para realizar el desplazamiento de los personajes de un lado a otro de forma animada
    run = True #si están en el barco y se van a mover de un lado a otro, se activa el reloj
    move = 0
    while run:
        clock.tick(27) #este elemento se manda a llamar por movimiento de personajes en el barco de un lado a otro
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #"quit" es el contrario de "init", en vez de iniciar un movimiento, desactiva una librería
                run = False
        keys = pygame.key.get_pressed() #activas un elemento cuando una tecla es presionada
        if keys[pygame.K_LEFT]: #si se activa la tecla izquierda, no recibe elementos de la derecha
            left = True
            right = False
            if move < len(P): #declaramos la primera provabilidad del juego
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2]) #declaramos la dirección de movimiento si tenemos dos elementos por subir al barco
                Embark_characters(Side_B, p1, p2) #embarcamos a los dos primeros personajes
                for step in range(65):
                    x -= vel
                    redrawGameWindow(direction, p1, p2) #una vez que se suben los personajes al barco y empieza el juego, tenemos que volver a dibujar la animación
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2) #cuando llegan a su destino (lado contrario de donde embarcaron) bajan a tierra.

        elif keys[pygame.K_RIGHT]: #si se activa la tecla derecha, no recibe elementos de la izquierda
            right = True
            left = False
            if move < len(P):  #declaramos la segunda provabilidad del juego
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2]) #volvemos a declarar la dirección de movimiento si tenemos dos elementos por subir al barco
                Embark_characters(Side_A, p1, p2) #volvemos a subir a dos personajes al barco
                for step in range(65):
                    x += vel
                    redrawGameWindow(direction, p1, p2) #dibujamos nuestro nuevo tablero con las nuevas ubicaciones
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2) #desenbarcamos a los dos personajes
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown')# si no se cumplen nuestras variables entonces volvemos a dibujar nuestro tablero
        

    pygame.quit()  #cuando termina nuestra solución el juego termina

def Busca_solucion():
    P = HCRfinal.HCR() #implementamos este código de diferentes jugadas en nuestro código de animación 
    while len(P) > 22:
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()  #una vez terminado el programa se reinicia el sistema
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))        #imprime texto para el usuario
        P = HCRfinal.HCR()
    print (P)  #imprime nuestro HCR final
    print (len(P))
    print ('\n =====> Solución encontrada:')   #imprime el texto a nuestro usuario
    return (P)

 
            
P = Busca_solucion()   #abrimos seccion para buscar solución
print ('Aquí su animación')  #devuelve solución con texto

pygame.init()

win = pygame.display.set_mode((500,500))  #despliega en display la animación
pygame.display.set_caption("How to Cross the River") #Despliega título para How to Cross the River

BoatRight   = pygame.image.load('BoteRight.png')  #carga imagen de un barco hacia la derecha
BoatLeft    = pygame.image.load('BoteLeft.png')  #carga imagen de un barco hacia la izquierda
bg          = pygame.image.load('seaL.png') #carga imagen de una foca
char        = pygame.image.load('BoteRight.png')  #carga imagen de un barco hacia la derecha
fox         = pygame.image.load('fox.png') #carga imagen de un zorro
corn        = pygame.image.load('corn.png') #carga imagen de el saco de maíz
duck        = pygame.image.load('duck.png')  #carga imagen de un pato
farmer      = pygame.image.load('farmer.png') #carga imagen de un granjero
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

Side_A = [farmer, fox, duck, corn]  #personajes en fila de salida
Side_B = []  #no hay personajes del otro lado del río al inicio de la simulación

HCR_animacion(P) #inicia animación




