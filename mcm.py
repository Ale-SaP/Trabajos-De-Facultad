def factoresRecursivo( numero ):
    if numero < 2:
        print(numero)
        return numero

    elif (numero >= 2): 
        if (numero % 2 == 0):
            print(2)
            return factoresRecursivo( numero//2 )

        elif (numero % 3 == 0):
            print(3)
            return factoresRecursivo( numero//3 )

        else:
            for x in range(5, numero + 1, 2):
                if (numero % x == 0):
                    print(x)
                    return factoresRecursivo(numero // x)



def factoresIterativo( numero ):
    while numero >= 2:
        if (numero % 2 == 0):
            numero = numero//2
        elif (numero % 3 == 0):
            numero = numero//3
        else:
            for x in range(5, numero + 1, 2):
                if (numero % x == 0):
                    print(x)
                    numero = numero//x



ListaDePrimos = []

def factoresConMemoizacion( numero ):
    if numero < 2:
        print(numero)
        return numero

    else:
        for x in ListaDePrimos:
           if (numero % x == 0):
              print(x)
              return mcdConMemoizacion(numero // x)
             
