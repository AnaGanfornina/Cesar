from simple_screen import Screen_manager,Print,locate,cls,Input,init,finish
from func_cifrados import Cifrador

def main():
    init()
    with Screen_manager:

        entrada = ""
        
        while entrada != "N":

            #Imprimir titulo
            locate(50,2)
            Print("CIFRADO CESAR")
            locate(50,4)
            Print("=============")
            
            #Pedir distancia
            locate(50,5)
            d = int(Input("Distancia de cifrado: "))
            instancia = Cifrador(d)

            #Pedir  mensaje a cifrar
            locate(50,6)
            mensaje = Input("Mensaje: ")

            #Procesar cifrado
            cifrado = Cifrador(d)
            mensaje_cifrado = cifrado.cifrar(mensaje)

            #imprimir mensaje cifrado
            locate(50,7)
            Print(f"Mensaje cifrado: {mensaje_cifrado}")

            locate(50,8)
            entrada = Input("¿otro mensaje (S/n)?")
            entrada = entrada.upper
            cls()
            

finish()

#Aportación de diego

if __name__ == "__main__":
    main()