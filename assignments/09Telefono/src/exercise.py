def main():
    # escribe tu código abajo de esta línea
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))

    costomen = mensajes*0.80
    costomeg = megas * 0.80
    costomin = minutos * 0.80

    costototal = costomeg + costomen + costomin

    print("El costo mensual es:",costototal)
    
if __name__ == '__main__':
    main()
