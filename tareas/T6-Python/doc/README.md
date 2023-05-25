# T6-Python: Juego de Piedra, papel o tijeras

## Autor: Diego Carmona Campos
## Última actualización: 05/05/2023

### **Introducción**

El juego de Piedra, Papel o Tijera es un juego de manos en el que existen tres elementos: la piedra, que vence a la tijera rompiéndola, la tijera, que vence al papel cortándolo, y el papel, que vence a la piedra envolviéndola. Se utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se hace a veces usando una moneda, o para dirimir algún asunto (ver https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera). 

Este programa simula el juego para que un usuario pueda jugar piedra, papel o tijera con la computadora.
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


### Instalación

Solo se requiere tener python instalado, recomendamos la version más reciente.

### Ejemplos

**1. El usuario da su nombre y la opción "papel"**

En línea de comando se corre el programa
```
python3 juego.py

```

El programa pedirá nombre y la opción al usuario:

```
¡Bienvenido al juego de piedra, papel o tijeras! :D

Ingresa tu nombre: Diego

!Ingresa piedra, papel o tijeras!
papel

Yo elegí: Papel
Tú elegiste: Papel
¡Empatamos!

!Ingresa piedra, papel o tijeras!
```

Si es un empate, el programa le pedirá una nueva opción.

```
!Ingresa piedra, papel o tijeras!
piedra

Yo elegí: Tijeras
Tú elegiste: Piedra

¡Felicidades, Diego, tú ganas!

Ingresa 1 para jugar de nuevo :D 
Ingresa 0 para salir :3
```

**2. El usuario continua con el juego y teclea la opción Tijeras**

Para continuar con le juego, se debe teclar la opción 1
```
Ingresa 1 para jugar de nuevo :D 
Ingresa 0 para salir :3
 1
```

Después se pedirá la nueva opción

```
!Ingresa piedra, papel o tijeras!
tijeras

Yo elegí: Piedra
Tú elegiste: Tijeras

Buen intento, Diego, pero esta vez yo gané ;D

Ingresa 1 para jugar de nuevo :D 
Ingresa 0 para salir :3

```
