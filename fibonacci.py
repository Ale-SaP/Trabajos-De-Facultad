def fibonacciIterativo(cantidadDeVeces):

    numeroDeFibonacci = 1
    numeroPrevio = 0
    vecesHecho = 2

    while (vecesHecho < cantidadDeVeces):

        vecesHecho += 1
        numeroPrevio = numeroDeFibonacci - numeroPrevio 
        numeroDeFibonacci = numeroDeFibonacci + numeroPrevio

        print("El número", numeroDeFibonacci, "es el dígito", vecesHecho, "de Fibonacci")


def fibonacciRecursivo(cantidadDeVeces):
    if cantidadDeVeces <= 2:
        return 1
    else: 
        return( ( fibonacciRecursivo(cantidadDeVeces - 1) + fibonacciRecursivo(cantidadDeVeces - 2) ) )
