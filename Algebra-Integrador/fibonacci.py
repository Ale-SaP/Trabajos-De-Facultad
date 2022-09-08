def fibonacciiterativo(digitoSolicitado):
    numeroDeFibonacci = 1
    numeroPrevio = 0
    vecesHecho = 2

    while (vecesHecho < digitoSolicitado):

        vecesHecho += 1
        numeroPrevio = numeroDeFibonacci - numeroPrevio 
        numeroDeFibonacci = numeroDeFibonacci + numeroPrevio

    print("El número", numeroDeFibonacci, "es el dígito", vecesHecho, "de Fibonacci")


def fibonaccirecursivo(digitoSolicitado):
    if digitoSolicitado <= 2:
        return 1
    else: 
        return( ( fibonaccirecursivo(digitoSolicitado - 1) + fibonaccirecursivo(digitoSolicitado - 2) ) )
