def change():
    gasto = 23.75
    recibido = 100

    print("Ingresar gasto:")
    print(gasto)
    print("dinero recibido")
    print(recibido)
   # vuelto = pagado - gasto
   # pesos = int(vuelto)
   # centavos = 
    vuelto = recibido - gasto
    print("\nVuelto\n")
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(int((vuelto - int(vuelto)) * 100))


change()
