#NOTA: Lo entre parentesis es para ti-->Lo borras para que quede bonito

#(Esto del metodo estatico es un poco absurdo, pero cumplo especificaciones)
#Metodo para crear mi objeto de la clase rejilla segun el archivo dado
def load_from_file(filename):
    #Cargamos el archivo. (Como no dice nada lo ponemos como nos de la gana. En mi caso lo mas facilito
    #Solo dice un ejemplo de como pasarle cosas al constructor. Tu flop no usara este metodo prob...)
    #archivo es el descriptor de fichero del archivo
    archivo = open(filename,"r");
    #En la primera linea esta tamanio
    tamanio = archivo.readline();
    #En la segunda los huecos con esta forma:
    poshuecos =  archivo.readline();
    #Todo lo que se abre se cierra
    archivo.close();
    #Creamos el objeto (tiene ambito local)
    rejilla = Rejilla(tamanio, poshuecos);
    #Lo devolvemos
    return rejilla

#My class Rejilla (no es necesario poner un object. Si no sepone te crea una clase de la version
#vieja de python, si se pone de la nueva)
class Rejilla(object):
    #Constructor de la clase ( se llama asi. Esto se ejecuta cada vez que creas un objeto de esta clase)
    def __init__(self, tamanio, huecos):
        #print "CONSTRUCTOR"
        self.tamanio = int(tamanio);
        #Convertimos el string en una secuencia de numeros
        self.huecos = str(huecos)
        self.huecos = self.huecos.replace("[",'');
        self.huecos = self.huecos.replace("]",'');
        self.huecos = self.huecos.replace("(",'');
        self.huecos = self.huecos.replace(")",'');
        self.huecos = self.huecos.replace(",",'');
        #Tb quitamos espacios por si los hubiera
        self.huecos = self.huecos.replace(" ",'');
        matrizhuecos = []
        i = 0;
        #Creamos un array de duplas, que seran nuestras celdillas (duplas puede ser de mas de dos o de uno incluso. Yo lo usamos
        #para coordenadas y parejas de datos y cosas asi)
        cont = 0
        #print "self.huecos: ", self.huecos
        while i<self.tamanio*self.tamanio/4:
            #print int(self.huecos[cont]), int(self.huecos[cont + 1])
            t = int(self.huecos[cont]), int(self.huecos[cont + 1])
            cont = cont + 2;
            i= i+1
            matrizhuecos.append(t)
        #Nuestro nuevo huecos manejable
        #print "len: ", len(matrizhuecos)
        self.huecos = matrizhuecos;
        #O(jo. Aunque parece igual que huecos al principio, ahora es un array de duplas y se puede manipular)
        #print "Mis coordenadas son: ", self.huecos
    #Lo dificil...
    def code(self, message):
        #print "CODIFICACION"
        offset = 0
        mensajecodificado = ""
        #El algoritmo es el siguiente:
        #0.-Creamos un array de nxn celdas para guardar las letras
        matriz = []
        for i in range(self.tamanio*2-1):
            matriz.append([])
            for j in range(self.tamanio):
                matriz[i].append(None)
        #0.1-La longitud del mensaje tiene que ser multiplo de la matriz de celdas. Lo llenamos de blancos desde ya
        whitesneeded = self.tamanio*self.tamanio - len(message)%(self.tamanio*self.tamanio)
        #print "La logitud del mensaje es: ", len(message)
        if (len(message)%(self.tamanio*self.tamanio) != 0):
            #(Seguro que hay una forma mejor de hacer esto..o quiza no!)
            for h in range(whitesneeded):
                message = message + ' '
            #print "La longitud del mensaje ahora es: ", len(message)
        while offset < len(message):
            #0.5.-Ordenamos las coodenadas. Para meter la primera letra en la casilla mas arriba a la izq y etc
            self.huecos.sort(); #Esta funcion manda!
            #1.-Metemos letras en los huecos
            for i in range(self.tamanio*self.tamanio/4):
                #(Ahora nuestras duplas molan)
                xy = self.huecos[i]
                x = xy[0]
                y = xy[1]
                #print "coord: ",xy
                ##print "message[offset]", message[offset]
                matriz[x][y] = message[offset]
                offset = offset + 1
            #print "Matriz: ", matriz
            #2.-Lo guardamos en una variable. y Repetimos
            if (offset%(self.tamanio*self.tamanio))==0:
                #print "offet: ", offset
                #print "Tamanio: ", self.tamanio*self.tamanio
                #print matriz
                for i in range(self.tamanio):
                    for j in range(self.tamanio):
                        mensajecodificado = mensajecodificado + matriz[i][j]
                #print "TABLA COMPLETA: Mensaje ya codificiado: ", mensajecodificado
            #3.-la giramos (En realidad no giramos una 4x4 o lo que sea. Cogemos solo los huecos y hacemos como que los giramos
            #Somos listos)
            #(El ultimo loop es necesario para dejar los huecos a "0", para el decode. Eso pasa por tocar el self y no
            #haber creado una variable auxiliar, pero vamos, que si tenemos cuidado esta perfecto)
            for i in range(self.tamanio*self.tamanio/4):
                #print "Antigua coordenada: ", self.huecos[i], " numero: ", i
                #Las coordenadas de las nuevas filas se calculan asi:
                    #Filanueva = tamanio-1(el cero cuenta ojo) - Colvieja
                #0 = filas, 1 = columnas
                x = (self.tamanio-1)-self.huecos[i][1]
                #Las coordenadas de las columnas nuevas, son las filas viejas
                    #Columnanueva = Filavieja
                y = self.huecos[i][0]
                #Las tuplas no se pueden modificar asi que creamos otra
                self.huecos[i] = x, y
                #print "Nueva coordenada: ", self.huecos[i], " numero: ", i
            #4.-Repetimos hasta completar nuestra tabla nxn
            #(Como el mensaje va "justo", no hay porque vaciarla para que no pasen cosas raras. Tampoco hace falta
            #hacer dos bucles, uno para los 4 giros y otro para completar el mensaje, pues al girar 4 veces las celdillas son
            #las mismas. INTMe explicoINT)

        return mensajecodificado
    #Igual que antes pero al reves
    def decode(self, message, size):
        #print "DECODIFICACION"
        mensajedecodificado = ""
        offset = 0
        #El algoritmo es el siguiente:
        #0.-Creamos un array de nxn celdas para guardar las letras
        matriz = []
        for i in range(self.tamanio*2-1):
            matriz.append([])
            for j in range(self.tamanio):
                matriz[i].append(None)
        #0.1-Por si acaso al mensaje que decodificamos, le hemos quitado los es paciosen blanco, se los volvemos a meter
        #(Esto no lo pruebo, si falla te lo arreglo maniana en tu flop jeje)
        whitesneeded = self.tamanio*self.tamanio - len(message)%(self.tamanio*self.tamanio)
        #print "La logitud del mensaje es: ", len(message)
        if (len(message)%(self.tamanio*self.tamanio) != 0):
            #(Seguro que hay una forma mejor de hacer esto..o quiza no!)
            for h in range(whitesneeded):
                message = message + ' '
            #print "La longitud del mensaje ahora es: ", len(message)
        #-Ojo si el offset este se pone antes si aniades cosas como espacios despues, cambia...
        offsetmsg = len(message) - 1
        while offset < len(message):
            #1.-Guardamos el mensaje en la tabla nxn. Da igual empezar por las primeras nxn o por las ultimas
            if (offset%(self.tamanio*self.tamanio))==0:
                for i in reversed(range(self.tamanio)):
                    for j in reversed(range(self.tamanio)):
                        matriz[i][j] = message[offsetmsg]
                        offsetmsg = offsetmsg - 1
                #print "TABLA COMPLETA: en proceso de decodificacion", matriz
            #2.-la giramos al reves (En realidad no giramos una 4x4 o lo que sea. Cogemos solo los huecos y hacemos como que los giramos
            #Somos listos)
            for i in reversed(range(self.tamanio*self.tamanio/4)):
                #print "Antigua coordenada: ", self.huecos[i], " numero: ", i
                #Las coordenadas de las filas nuevas, son las columnas viejas
                    #Filaueva = Columnavieja
                x = self.huecos[i][1]
                #Las coordenadas de las columnas nuevas se calculan asi:
                    #Columnanueva = tamanio-1(el cero cuenta ojo) - Filavieja
                #0 = filas, 1 = columnas
                y = (self.tamanio-1)-self.huecos[i][0]

                #Las tuplas no se pueden modificar asi que creamos otra
                self.huecos[i] = x, y
                #print "Nueva coordenada: ", self.huecos[i], " numero: ", i

            #2.5.-Ordenamos las coodenadas. Para meter la primera letra en la casilla mas arriba a la izq y etc
            #print "NO reversed huecos: ", self.huecos
            self.huecos.sort(reverse=True); #Esta funcion manda!
            #print "Reversed huecos: ", self.huecos
            #3.-Cogemos las letras de los huecos
            #Cogemos de la mas abajo a la derecha
            for i in range(self.tamanio*self.tamanio/4):
                #(Ahora nuestras duplas molan)
                xy = self.huecos[i]
                x = xy[0]
                y = xy[1]
                mensajedecodificado = matriz[x][y] + mensajedecodificado
                offset = offset + 1
            #print "Mensaje decodificado parcial: ", mensajedecodificado
            #4.-Repetimos hasta completar nuestra tabla nxn
            #(Como el mensaje va "justo", no hay porque vaciarla para que no pasen cosas raras. Tampoco hace falta
            #hacer dos bucles, uno para los 4 giros y otro para completar el mensaje, pues al girar 4 veces las celdillas son
            #las mismas. INTMe explicoINT)

        return mensajedecodificado

    #(como el load. Cojo mi tamanio de la rejilla de mi "cajon", y los huecos de la rejilla y los guardo)
    def save(self, filename):
        #Si no existe lo crea, si existe lo reemplaza
        archivo = open(filename, 'w');
        lineas = self.tamanio,"\n",self.huecos,"\n";
        archivo.write(str(self.tamanio));
        archivo.write('\n');
        #Tb quitamos espacios al escribir
        archivo.write(str(self.huecos).replace(" ",''));
        archivo.close();

#My main (realmente se ejecuta todo el archivo no solo el main cuando haces python main.py..pero bueno,
#esto es lo correcto por si usamos import o mas archivos que este main.py)
#if __name__ == '__main__':
#    rejilla = load_from_file("loadablefile.txt");
#    #codedmsg = rejilla.code("Matemagicas rugby club. For Alma")
#    codedmsg = rejilla.code('En un lugar de l')
#    print "Mensaje codificado COMPLETO: ", codedmsg
#    #(A mi no me hace falta que me pasen el tamanio del mensaje..porque aunque haya espacios al final, hago
#    #que sigan estando, no los quito..esto a tu eleccion. Es una linea mas)
#    decodedmsg = rejilla.decode(codedmsg, 16);
#    print "Mensaje decodificado COMPLETO: ", decodedmsg
#    rejilla.save("saveablefile.txt")

#if __name__ == '__main__':
#    gaps=[(7, 7), (6, 0), (5, 0), (4, 0), (7, 1), (1, 1), (1, 2), (4, 1), (7, 2), (2, 1), (2, 5), (2, 3), (7, 3), (3, 1), (3, 2), (3, 4)]
#    r=Rejilla(8,gaps)
#    texto='En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor.'
#    n=len(texto)
#    out=r.code(texto)
#    print out
#    print texto
#    print r.decode(out,n)
#    print r.decode(out,n)==texto
