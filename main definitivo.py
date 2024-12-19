from palabras import palabras_ahorcado
from ahorcado_diagramas import Diagramas
diagrama = Diagramas()
#Guardamos todo el juego como una clase. Cada juego de ahorcado es una instancia de ésta, cuyo atributo principal es la palabra que da sentido al juego, y su secundaria/derivada que está oculta con guiones bajos
class Ahorcado:
    letras_adivinadas = []
    letras_no_adivinadas = []
    j = 0
    def __init__(self, palabra, categoria):
        self.palabra = palabra
        #Ésta pudo ser una variable global, ya que depende del argumento palabra que se tome al instanciar. Preferí dejarla así para enfatizar que este es un atributo que toma cada instancia
        self.palabra_oculta = len(self.palabra) * '_' 
        self.categoria = categoria

    def presentacion(self):
        print(f'-------Juego del ahorcado: {self.categoria}---------')
        print(self.palabra_oculta)
        print(diagrama.setIntento(0)())

    def adivinar(self, letra):    
        if letra in self.palabra:
            if letra not in self.letras_adivinadas:
                for i in range(len(self.palabra)):
                    if self.palabra[i] == letra:
                        self.palabra_oculta = self.palabra_oculta[:i] + letra + self.palabra_oculta[i+1:] #Revelar las posiciones en donde la letra fue adivinada en la palabra
                self.letras_adivinadas.append(letra)
                print(self.palabra_oculta)
                print(diagrama.setIntento(self.j)())
                print('Letras no adivinadas: ', ', '.join(self.letras_no_adivinadas))       
            else:
                print('ya has adivinado esa letra')
                print(self.palabra_oculta)
                print(diagrama.setIntento(self.j)())
                print('Letras no adivinadas: ', ', '.join(self.letras_no_adivinadas))                 
                
    def no_adivinar(self, letra):
        self.j += 1
        print('No has adivinado. ¡Lo siento!')
        print(self.palabra_oculta)
        print(diagrama.setIntento(self.j)())
        if letra not in self.letras_no_adivinadas:
            self.letras_no_adivinadas.append(letra)
            print('Letras no adivinadas: ', ', '.join(self.letras_no_adivinadas))
        else:
            print('Ya te habías equivocado en esa >:|')
            print('Letras no adivinadas: ', ', '.join(self.letras_no_adivinadas))
           
    def ahorcado(self):
        self.presentacion()
        #reiniciamos estas listas al recorrer una nueva palabra del diccionario, si fuera para juegos aislados se puede omitir esto. Esto no pasa con j ya que en todos empieza desde 0
        self.letras_adivinadas = []
        self.letras_no_adivinadas = []
        while self.j < 6:
            x = input('Ingresa una letra: ')
            if x == '': #¿ejemplo de guard clause? si hubiera puesto if x != '', tendría ifs anidados
                print("No ingresar letra es considerado un error")
                self.no_adivinar(x)
            else:
                if x in self.palabra:
                    self.adivinar(x)
                else:
                    self.no_adivinar(x)

            if self.palabra_oculta == self.palabra:
                print('¡Felicitaciones!, te has ganado una cheve \n')
                break

        if self.j == 6:
            print(f'La palabra era: {self.palabra}')
            print('Lo siento, perdiste :c  \n')

    #Preguntamos si se quiere continuar al siguiente ahorcado
    def continuar(self):
        while True:
            opcion = input('¿Deseas continuar con el siguiente?: Si//No ')
            if opcion in ["Si", "si", "SI", "Sí", "sí", "SÍ"]:
                return opcion
            elif opcion in ["No", "no", "NO"]:
                return opcion
            else:
                print('Ingresa una opción válida: Si//No ')
                continue

def jugar():      
    #Ejecucion del juego con base en las palabras del diccionario
    for i in palabras_ahorcado.keys():
        #Ejecución de la instancia, es decir, de un juego de ahorcado
        ahorcado = Ahorcado(palabras_ahorcado[i], i)
        ahorcado.ahorcado()

        #Condiciones de cierre o continuación
        if list(palabras_ahorcado.keys()).index(i) == len(list(palabras_ahorcado.keys()))-1: #Para verificar si todavia tenemos palabras en el diccionario para continuar
            print('Se han acabado los juegos')
            break
        else:
            opcion = ahorcado.continuar()
            if opcion in ["Si", "si", "SI", "Sí", "sí", "SÍ"]:
                continue
            else:                                       #gracias al método continuar(), solo se nos devuelven dos tipos de valores válidos: todas las formas de si o las de no, y por eso solo es un if - else
                print('Fin del juego')
                break

jugar()          