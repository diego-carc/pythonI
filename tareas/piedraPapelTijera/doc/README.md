# T6-Python: Juego de Piedra, papel o tijeras

## Autor: Diego Carmona Campos
## Última actualización: 02/09/2023

### **Introducción**

El juego de Piedra, Papel o Tijera es un juego de manos en el que existen tres elementos: la piedra, que vence a la tijera rompiéndola, la tijera, que vence al papel cortándolo, y el papel, que vence a la piedra envolviéndola. Se utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se hace a veces usando una moneda, o para dirimir algún asunto (ver https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera). 

Este programa simula el juego para que un usuario pueda jugar piedra, papel o tijera con la computadora.
El programa debe pedir al usuario su opción y aleatoriamente la computadora seleccionará su opción. Veremos quien gana.


### **Algoritmo**

El algoritmo para resolver el problema es:

1. Recibir argumentos con nombre y número de juegos
2. Por cada juego, se llama a la función play()
3. Dentro de la función play, se recibe la elección del jugador y la computadora
4. Si ambas jugadas son iguales, se vuelve a elejir
5. Si ocurre alguno de los casos en los que el jugador gana se devuelve True. De lo contrario
se devuelve False
6. Se le informa al jugador si gana o pierde 


### Ejemplo
```bash
python .\pie_pap_tij.py -n 3 -p Diego
```
output:
```
¡Hola, Diego!
Bienvenid@ al juego de piedra papel o tijera:
!Piedra, Papel o Tijeras!: Piedra

La computadora eligió: Piedra

¡Empate!
!Piedra, Papel o Tijeras!: Papel

La computadora eligió: Tijeras

Lo sentimos, perdite el juego 1 de 3
!Piedra, Papel o Tijeras!: Tijeras

La computadora eligió: Tijeras

¡Empate!
!Piedra, Papel o Tijeras!: Piedra

La computadora eligió: Tijeras

¡¡¡Felicidades!!!
Ganaste el juego 2 de 3
!Piedra, Papel o Tijeras!: Papel

La computadora eligió: Piedra

¡¡¡Felicidades!!!
Ganaste el juego 3 de 3
Gracias por jugar 
```

### Resultados
Los resultados pueden ser encontrados en [mi repositorio de GitHub](https://github.com/diego-carc/pythonI/tree/master/tareas/piedraPapelTijera)