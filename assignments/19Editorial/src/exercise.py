def main():
    # escribe tu código abajo de esta línea
    import math
    numpal = int(input("Dame el número de palabras: "))
    
    totalpag = math.ceil(numpal/ 475)
    total = totalpag * 60
    descuento = total -(total * 0.1)
    
    print("El costo de la publicación es:", descuento)


if __name__ == '__main__':
    main()
