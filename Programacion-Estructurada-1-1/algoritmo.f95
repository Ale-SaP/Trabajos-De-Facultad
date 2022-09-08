Program ejercicio
    real :: acumulador
    integer :: contador
    real :: edad
    real :: promedio
    acumulador = 0
    contador = 0
    print *, 'Ingresar Edad: '
    read *, edad

    do while (edad /= 0)
        acumulador = acumulador + edad
        contador = contador + 1
        print *, 'Ingresar Edad: '
        read *, edad
    end do

    promedio = acumulador / contador
    print *, 'El promedio es:'
    print *, promedio

End Program ejercicio