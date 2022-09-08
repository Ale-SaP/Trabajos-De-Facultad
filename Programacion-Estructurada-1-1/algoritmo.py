def ejercicio():
    acumulador = 0
    contador = 0
    edad = float( input("Ingresar Edad: ") )

    while ( edad != 0 ):
        acumulador += edad
        contador += 1
        edad = float( input("Ingresar Edad: ") )

    promedio = acumulador/contador
    print(f"El promedio es: {promedio}")

ejercicio()