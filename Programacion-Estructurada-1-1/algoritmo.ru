def ejercicio
    acumulador = 0
    contador = 0
    puts("Ingresar Edad: ")
    edad = gets.to_f

    while edad != 0
        acumulador += edad
        contador += 1
        puts("Ingresar Edad: ")
        edad = gets.to_f
    end

    promedio = acumulador/contador
    print "El promedio es: ", promedio
end

ejercicio