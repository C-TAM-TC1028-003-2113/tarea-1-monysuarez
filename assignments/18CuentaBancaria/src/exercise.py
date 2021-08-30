def main():
    # escribe tu código abajo de esta línea
    ant = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques= int(input("Dame el número de cheques: "))

    costocheques= cheques * 13
    utilidad = ingresos - egresos
    totalmedio = ant + utilidad - costocheques
    total = totalmedio - (totalmedio * 0.075)

    print("El saldo final de la cuenta es:",total)
if __name__ == '__main__':
    main()
