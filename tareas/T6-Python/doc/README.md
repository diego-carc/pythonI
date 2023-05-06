# T6-Python: Juego de Piedra, papel o tijeras

## Autor: Diego Carmona Campos
## Última actualización: 05/05/2023

### **Introducción**
El uso de ciclos y condicionales es muy importante en programación, pues nos permite construir algoritmos más complejos que sean capaces de responder a distintos casos, así como hacer tareas repetitivas.

**Problema:**

Escribe un script para que un usuario pueda jugar piedra, papel o tijera con la computadora.
El programa debe pedir al usuario su opción y aleatoriamente la computadora seleccionará su opción. Veremos quien gana.


### **Algoritmo**

El algoritmo para resolver el problema es:

1. Pedir el nombre del jugador.
2. Declarar una bandera *play_again* inicializada en *True* para repeir el juego mientras el jugador quiera.
3. Llamar a una función *play_game()* donde se pedirá que el jugador ingrese 'Piedra', 'Papel' o 'Tijeras'.
4. Verificar que el *string* ingresado sea una opción válida.
5. Usar la paquetería *random* para elegir 'Piedra', 'Papel' o 'Tijeras' de forma aleatoria. 
6. Verificar los posibles casos:
    - Empate
    - 'Tijeras' vs 'Papel', 'Papel' vs 'Piedra' o 'Tijeras' vs 'Piedra'.
7. Llamar a la función *define_who_wins()* para imprimir el resultado.

### **Resultados**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T6-Python).