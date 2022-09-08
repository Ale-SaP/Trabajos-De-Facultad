function ejercicio()
    acumulador = 0
    contador = 0
    io.write('Ingresar Edad: ')
    edad = tonumber( io.read() )

    while (edad ~= 0)
    do
        acumulador = acumulador + edad
        contador = contador + 1
        io.write('Ingresar Edad: ')
        edad = tonumber( io.read() )
    end

    promedio = acumulador/contador
    print("El promedio es:", promedio)
 end

 ejercicio()