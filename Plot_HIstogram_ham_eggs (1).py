import matplotlib.pyplot as plt

text = "" #texto pero meterlo en txt
remove =  ".:,'!-()?"  #para quitar carácteres especiales
file1 = open("Green_eggs_and_ham.txt", "r")
Lines = file1.readlines()
count = 0
#loop que revisa linea por linea el texto y lo guarda como un string para ser procesado
for i in Lines:
    count += 1
    i = i.replace('\n', " ")
    text = text + i
print(text)

for character in remove:
    text = text.replace(character, "") #remplaza los carácteres especiales por nada
text = text.lower() #cambia las palabras mayúsculas por minúsculas
words = text.split(" ") #separa las palabras para pasarlas en un arreglo
diccionario_frecuencias = {}
for word in words:
    if word in diccionario_frecuencias:
        diccionario_frecuencias[word] += 1 #a cada palabra le da un número en el orden, entonces va sumando uno
    else:
        diccionario_frecuencias[word] = 1 #cuando termina el diccionario ya no suma los valores

for word in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[word] #cuenta la frecuencia de palabras
    print (f"la palabra {word} tiene una frecuencia de {frecuencia}") #así se evita concatenar
words.sort(reverse=True)#ordenamos nuestra lista para poder graficarla en orden


count = 0
temp_list = []

#loop que tiene la funcionalidad de dividir de 10 en 10 las graficas para nuestro histograma
for i in range(0,len(words)):
    if words[i] != words[i+1]:
        count += 1
    if count % 10 == 0 and count != 0 and len(temp_list) != 0:
        temp_list.append(words[i])
        plt.hist(temp_list,edgecolor = 'black')#graficacion de histograma
        plt.show()
        temp_list = []
    if words[i] == "":
        break
    if count % 5 != 0 or count == 0:
        temp_list.append(words[i])
