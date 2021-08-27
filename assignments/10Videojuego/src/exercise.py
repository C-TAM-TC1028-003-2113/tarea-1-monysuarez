def main():
    # escribe tu código abajo de esta línea
    nuevos= int(input("Dame la cantidad de juegos nuevos: "))
    usados = int(input("Dame la cantidad de juegos usados: "))

    costonue = 1000*nuevos
    costousados = 350 * usados
    
    costototal = costonue + costousados
    print("El total de la compra es:",costototal)

if __name__ == '__main__':
    main()