import json
puntajes=[]
def registrar_puntaje():
    id_jugador=input("Ingrese su id de jugador ==> ")
    nombre=input("Ingese su nombre y Apellido ==> ")
    juego=input("Ingrese su juego (VALORANT/FORNITR/FIFA)==> ")
    tipo=input("Ingrese su tipo (Principiante/Avanzado/Experto) ==> ")
    puntaje=input("Ingrese su puntaje ==> ")
    puntajes.append({id_jugador,nombre,juego,puntaje,tipo})
    print("****Datos agregados****")

def lista_de_puntajes():
    print("Id_jugador    Nombre    Valorant    Fornite    FiFa    tipo")
    for puntaje in puntajes:
        print(puntaje)


def menu():


    flag=True
    while flag==True:
        print("1. Registrar Puntajes del Torneo")
        print("2. Listar Los Todos Puntajes ")
        print("3. Imprimir Por Tipo ")
        print("4. Salir Del Programa")
        opcion = input("Ingrese su opcion del 1 al 4 ==> ")
        if opcion == "1":
            registrar_puntaje()
        elif opcion == "2":
            lista_de_puntajes()
        elif opcion == "3":
            print("3")
        elif opcion == "4":
          break
        else:
            print("opcion no existe ")

print(menu())         