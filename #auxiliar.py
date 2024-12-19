#auxiliar
#--------------Ahorcado, funciones sin clases----------
from ahorcado_diagramas import Diagramas
diagrama = Diagramas()
def adivinada(letra, palabra, palabra_oculta, letras_adivinadas):
    if letra in letras_adivinadas:
        print('ya has adivinado esa letra')
    else:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
    return palabra_oculta 


def no_adivinada(func):
    print('No has adivinado. ¡Lo siento!')
    print(func())

def ahorcado(palabra, palabra_oculta):
    letras_adivinadas = []
    j = 0
    while j < 6:
        x = input('Ingresa una letra: ')
        if x in palabra:
            palabra_escondida = adivinada(x, palabra, palabra_oculta, letras_adivinadas)
            palabra_oculta = palabra_escondida
            print(palabra_oculta)
            print(diagrama.vacio())
            letras_adivinadas.append(x)
        else:
            j += 1
            no_adivinada(diagrama.setIntento(j))

        if palabra_oculta == palabra:
            print('¡Felicitaciones!, te has ganado una cheve')
            break

        if j == 6:
            print('Lo siento, perdiste :c')
            