'''
NAME
    biomolecules.py
  
VERSION
    1.0  08/09/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa simula una célula en la que se sintetizan y degradan ciertas biomoléculas.

CATEGORY
   Biological    

USAGE

    % python biomolecules.py 

ARGUMENTS
    None

SEE ALSO
'''
from time import sleep
from random import randint

class biomolecula():
    organico = True

    def __init__(self, nombre:str, polimero:bool, subunidad:str, hidrofilica:bool):
        self.nombre = nombre
        self.polimero = polimero
        self.subunidad = subunidad
        self.hidrofilica = hidrofilica
        

    def  sintetizar(self):
        print("Llamando enzimas...")
        sleep(randint(1,4))
        print(f"Se sintetizó {self.nombre}")

    def degradar(self):
        print("LLamando enzimas...")
        sleep(randint(1,4))
        print(f"Se degradó {self.nombre}")

class carbohidrato(biomolecula):
    def __init__(self, nombre, polimero: bool, subunidad: str ):
        super().__init__(nombre, polimero, subunidad, True)
    
    def sintetizar(self):
        print("LLamando glicosil transferasas...")
        sleep(randint(1,4))
        print(f"Se sintetizó {self.nombre}")
    
    def degradar(self):
        print("LLamando sacaridasas")
        sleep(randint(1,4))
        print(f"Se degradó {self.nombre}")
    

class proteina(biomolecula):
    def __init__(self, nombre, hidrofilica):
        super().__init__(nombre, True, "Aminoácidos", hidrofilica)
    
    def sintetizar(self):
        print("LLamando ribosomas...")
        sleep(randint(1,4))
        print(f"Se sintetizó {self.nombre}")
    
    def degradar(self):
        print("LLamando proteasas")
        sleep(randint(1,4))
        print(f"Se degradó {self.nombre}")
    

class lipido(biomolecula):
    def __init__(self, nombre):
        super().__init__(nombre, False, "Ácidos grasos", False)
    
    def sintetizar(self):
        return super().sintetizar()
    
    def degradar(self):
        print("LLamando lipasas...")
        sleep(randint(1,4))
        print(f"Se degradó {self.nombre}")
    

class acido_nucleico(biomolecula):
    def __init__(self, nombre):
        super().__init__(nombre, True, "Nucleótidos", True)
    
    def sintetizar(self):
        print("LLamando ADN polimerasas...")
        sleep(randint(1,4))
        print(f"Se sintetizó {self.nombre}")
    
    def degradar(self):
        print("LLamando exonucleasas...")
        sleep(randint(1,4))
        print(f"Se degradó {self.nombre}")
    
# Simulación
print("Inicia la síntesis de biomoléculas...")
glucogeno = carbohidrato('Glucógeno', True, 'Glucosa')
glucogeno.sintetizar()
print(glucogeno.__dict__)
print('\n')

colesterol = lipido('Colesterol')
colesterol.sintetizar()
print(colesterol.__dict__)
print('\n')

ADN = acido_nucleico('ADN')
ADN.sintetizar()
print(ADN.__dict__)
print('\n')

ATP_sintasa = proteina('ATP_sintasa',False)
ATP_sintasa.sintetizar()
print(ATP_sintasa.__dict__)
print('\n')

print("Las biomoléculas se van a degradar...")
glucogeno.degradar()
print('\n')
colesterol.degradar()
print('\n')
ADN.degradar()
print('\n')
ATP_sintasa.degradar()