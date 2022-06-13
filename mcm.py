def mcd( numero ):
    if numero < 2:
        print(numero)
        return numero

    elif (numero >= 2): 
        if (numero % 2 == 0):
            print(2)
            return mcd( numero//2 )

        elif (numero % 3 == 0):
            print(3)
            return mcd( numero//3 )

        else:
            for x in range(5, numero + 1, 2):
                if (numero % x == 0):
                    print(x)
                    return mcd(numero // x)


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
             
