'''
NAME
    pie_pap_tij.py
  
VERSION
    1.0  05/05/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    Este programa está hecho para jugar "Piedra, Papel o Tijera".

CATEGORY
   Game   

USAGE

    % python pie_pap_tij.py

ARGUMENTS
    None    

SEE ALSO
'''

# Imports
import random

# Functions
def play_game():
    # Definir opciones
    options = ['Piedra', 'Papel', 'Tijeras']
    computer_choice = random.choice(options)
    player_choice = input('\n!Ingresa piedra, papel o tijeras!\n').capitalize()

    print(f'\nYo elegí: {computer_choice}\n'
          f'Tú elegiste: {player_choice}')
    
    # El jugador no ingresa una opción válida
    error = 0
    if player_choice not in options:
        print(f'Lo siento, {player_choice} no está permitido :(\n'
              'Intenta de nuevo ;)')
        play_game()
        error = 1

    # Empate
    if computer_choice == player_choice:
        print('¡Empatamos!')
        play_game()
        error = 1

    # Definir lo que sucede si el jugador ingresa 'Piedra'
    if player_choice == options[0]:
        winning_option = options[2]
        losing_option = options[1]
    
    # Definir lo que sucede si el jugador ingresa 'Papel'
    if player_choice == options[1]:
        winning_option = options[0]
        losing_option = options[2]
    
    # Definir lo que sucede si el jugador ingresa 'Tijeras'
    if player_choice == options[2]:
        winning_option = options[1]
        losing_option = options[0]
    
    # Imprimir resultado
    if not error:
        define_who_wins(winning_option, losing_option, computer_choice)
    return()
  
def define_who_wins(win_option, lose_option, computer_choice):
    '''
    Evalúa las entradas del juego 'Piedra papel o tijeras' implementado en la función 'play_game'.
    El resultado del juego se imprime en pantalla.
    '''
    # Mensaje de victoria
    if computer_choice == win_option:
        print(f'\n¡Felicidades, {name}, tú ganas!\n')
        return()
    
    # Mensaje de derrota
    if computer_choice == lose_option:
        print(f'\nBuen intento, {name}, pero esta vez yo gané ;D\n')
        return()

# Main
# Iniciar juego
print('¡Bienvenido al juego de piedra, papel o tijeras! :D\n')
name = input('Ingresa tu nombre: ')

# Jugar hasta que el jugador quiera salir
play_again = True
while play_again:
    play_game()
    play_again = int(input('Ingresa 1 para jugar de nuevo :D \n'
                       'Ingresa 0 para salir :3\n '))

# Terminar juego
print(f'¡Gracias por jugar, {name}!')