#include <stdio.h>

void ejercicio() {
    float acumulador;
    float contador;
    float edad;
    float promedio;
    contador = 0;
    acumulador = 0;
    printf("Ingresar Edad: ");
    scanf("%f", &edad);

    while ( edad != 0) {
        acumulador = acumulador + edad;
        contador = contador + 1;
        printf("Ingresar Edad: ");
        scanf("%f", &edad);
    }

    promedio = acumulador/contador;
    printf("El promedio es: %f", promedio);
}

int main()
{ 
    ejercicio();
    return 0;
}