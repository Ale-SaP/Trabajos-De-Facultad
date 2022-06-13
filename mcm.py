def mcdRecursivo( numero ):
    if numero < 2:
        print(numero)
        return numero

    elif (numero >= 2): 
        if (numero % 2 == 0):
            print(2)
            return mcdRecursivo( numero//2 )

        elif (numero % 3 == 0):
            print(3)
            return mcdRecursivo( numero//3 )

        else:
            for x in range(5, numero + 1, 2):
                if (numero % x == 0):
                    print(x)
                    return mcdRecursivo(numero // x)



def mcdIterativo( numero ):
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

def mcdConMemoizacion( numero ):
    if numero < 2:
        print(numero)
        return numero

    elif (numero >= 2): 
        if (numero % 2 == 0):
            print(2)
            return mcdConMemoizacion( numero//2 )

        elif (numero % 3 == 0):
            print(3)
            return mcdConMemoizacion( numero//3 )

        else:
            for x in ListaDePrimos:
                if (numero % x == 0):
                    print(x)
                    return mcdConMemoizacion(numero // x)


divisores = []
def mcdLista( numero ):
    global divisores
    if numero < 2:
        divisores.append(numero)
        return divisores

    elif (numero >= 2): 
        if (numero % 2 == 0):
            divisores.append(2)
            return mcdLista( numero//2 )

        elif (numero % 3 == 0):
            divisores.append(3)
            return mcdLista( numero//3 )

        else:
            for x in range(5, numero + 1, 2):
                if (numero % x == 0):
                    divisores.append(x)
                    return mcdLista(numero // x)
             
