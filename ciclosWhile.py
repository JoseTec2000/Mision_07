#José Isidro Sánchez Vázquez
#mision 7 ciclos while

def dividir(dividendo,divisor):
    cociente = 0
    while (dividendo-divisor)>=0:
        dividendo = dividendo - divisor
        cociente +=1
    print("El cociente es =",cociente)
    print("El residuo es =",dividendo)


def encontrarMayor():
    Terminar= -1
    valor= 0
    contador= 0

    print("Teclea una serie de números para encontrar el mayor.")
    while valor!= -1:
        valor=int(float(input("Teclea un número [-1 para salir]:")))

    if valor<-1:
        print("No hay valor mayor")
    elif valor>Terminar:
        Terminar=valor
        contador+=1
    elif valor< -1:
        print("Ese no es un valor válido: Debes teclear un número entero positivo.")

    elif valor == -1:
        if contador != 0:
            print("El mayor es: ",Terminar)
        else:
            print("No hay valor mayor")


def main():
    tecla = 0
    while tecla!=3:
        print("Mision 07. Ciclo while")
        print("Autor: José Isidro Sánchez Vázquez")
        print("Matricula: A01748144")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        tecla = int(input("Teclea tu opción: "))
        if tecla ==1: #cuando presiona uno realiza la funcion dividir
            print("Calculando divisiones")
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el valor del divisor: "))
            dividir(dividendo, divisor)

            tecla = 0
            print("")
        elif tecla ==2: ###cuando presiona dos realiza la funcion para encontrar al mayor
            encontrarMayor()
            tecla = 0
            print("")
        elif tecla ==3: #cuando presiona tres el programa se cierra
            print("Gracias por usar este programa, regresa pronto.")
            break
        elif tecla<1 or tecla>3: #Cuando presiona un numero diferente a 1,2 o 3 marca error
            print("¡¡¡ERROR¡¡¡,teclea1,2 o 3")
            tecla=0
            print(" ")

main()