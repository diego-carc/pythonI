'''
NAME
    pie_pap_tij.py
  
VERSION
    2.0  02/09/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    Este programa está hecho para jugar "Piedra, Papel o Tijera".

CATEGORY
   Game   

USAGE

    % python pie_pap_tij.py -n [Número de veces para jugar] -p [Nombre del jugador]

ARGUMENTS
    --Number: Número de veces que se va a jugar
    --Player: Nombre del jugador 

SEE ALSO
'''

# Imports
import random
import argparse

# Functions
def play():
   '''
   Permite jugar piedra papel o tijeras
   '''

   if (player := input("!Piedra, Papel o Tijeras!: ")) not in (moves:=["Piedra", "Papel", "Tijeras"]):
        print("Las únicas opciones váldidas son:\n\t-Piedra\n\t-Papel\n\t-Tijeras")
        return(play())
   
   print(f"\nLa computadora eligió: {(computer := random.choice(moves))}\n")
   
   if player == computer:
        print("¡Empate!")
        return(play())
   
   if player == "Tijeras" and computer == "Papel" \
        or player == "Papel" and computer == "Piedra" \
            or player == "Piedra" and computer == "Tijeras":
        return(True)
   
   else: return(False)

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number',
                    help="Número de veces que se desea jugar",
                    type=int)
parser.add_argument('-p', "--player",
                    help="Nombre del jugador o jugadora")
args = parser.parse_args()

# Jugar
print(f"¡Hola, {args.player}!\nBienvenid@ al juego de piedra papel o tijera:")

for i in  range(1, args.number + 1):
     if play(): print(f"¡¡¡Felicidades!!!\nGanaste el juego {i} de {args.number}")
     else: print(f"Lo sentimos, perdite el juego {i} de {args.number}")

print("Gracias por jugar")

