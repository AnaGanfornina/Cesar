from simple_screen import Print, locate, Input, init, finish, cls
from func_cifrados import Cifrador



def main(): 
    init()
    
    while True:
        locate(50, 2)
        Print("CIFRADO CESAR")

        locate(50, 3)
        Print("=============")

        locate(50, 4)
        distancia = int(Input("Distancia cifrado: "))

        locate(50, 5)
        mensaje = Input("Mensaje a descifrar: ")

        cifrado = Cifrador(distancia)
        mensaje_cifrado = cifrado.cifrar(mensaje)

        locate(50, 6)
        Print(f"Mensaje cifrado: {mensaje_cifrado}")

        locate(50, 7)
        seguir = Input("¿Otro mensaje (S/n)?")
        if seguir.lower() != "s":
            break
        cls()
finish()    

if __name__ == "__main__":
    main()