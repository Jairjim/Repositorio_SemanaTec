#Se importa la librería random, permite el adquirir números aleatorios
import random
#se declaran las variables de posición en forma de arreglos
#que van de ladp izquiero a derecho
Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

#elige, quien será la primera elección para realiar el movimiento
def seleccion(L):
    op = random.randint(0,len(L)-1)
    return (L[op])

#Realiza el viaje de la imagen
def Viaje(F, D):
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    return ('Granjero',p1)

#En caso de que coexista la posibilidad que se quede en la longitud
#únicamente los elementos que se puedan comer entre sí, retorna un valor
#falso, en caso de que no sea así, se vuelve positivo
def valida_estado(L):
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
    return True

#
def reiniciar_sistema(): #reinicia nuestra animación 
    global Lado_A, Lado_B, Path #declaramos nuestras variables globales para nuestra animación de How to Cross a River 
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz'] #iniciamos todos nuestros personajes del lado A 
    Lado_B = [] #no tenemos personajes en el lado B, que es del otro lado del río 
    Path = [] #iniciamos nuestro path, pero aun no comienzan los viajes en el batco 
    

def HCR():#definimos nuestra clase de posición
    F = Lado_A #declaramos nuesto lugar de  salida 
    D = Lado_B #declaramos nuestro lugar de llegada al otro lado del río 
    while len(Lado_B) != 4: #iniciamos nuestro ciclo while pra la animación de los procesos del lado B
        p1, p2 = Viaje(F, D) #iniciamos viaje de los dos primeros pasajeros 
        if valida_estado (F) and valida_estado (D): #valida el estado de los pasajeros, si hay 2 por subir se activa, de lo contrario  no cruzan en el barco 
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :') #iniciamos camino para cruzar el río 
            else: # de lo contrario 
                Path.append('B->A :') #regresamos del lado B al lado A 
            Path.append(p1) #agregamos ambos procesos a la animación 
            Path.append(p2)
            
            Temp = F #variables temprales
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema() #reinicia el sistema si no corre de manera correcta 
            F = Lado_A #incluimos nuestro lado A del río a nuestra variable temporal 
            D = Lado_B #incluimos nuestro lado B del río a nuestra variable temporal 
    return (Path) #devolvemos al usuario el path 


def main(): #iniciamos programa completo 
    P = HCR() #corremos sección How to Cross a RIver 
    while len(P) > 22: 
        reiniciar_sistema() #iniciamos el sistema para hacer nuestro path 
        print ('\nBuscando una mejor solución, Longitud del Path', len(P)) #devolvemos el texto a nuestro usuario sobre la búsqueda de uan mejor solución 
        P = HCR() #declaramos variable y estado 
    print (P) #imprimimos el path 
    print (len(P))# imprimimos nuestra duración 
            
main() #corremos programa en totalidad 

  
