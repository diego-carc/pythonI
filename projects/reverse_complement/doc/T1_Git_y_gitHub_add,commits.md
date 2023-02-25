
# Tarea 1: Git y gitHub : add, commits

#### Diego Carmona Campos
#### Última actualización: 25 de febrero de 2023

##### Introducción.
Git es un  controlador de versiones que nos permite llevar un registro de los cambios que hacemos a los archivos de un repositorio. Es muy importante llevar este control ya que cuando trabajamos con muchos archivos e incursionamos en el mundo de la programación, resulta útil tener la capacidad de disringuir entre las versiones de prueba y las versiones definitivas de nuestros *scripts.* Es por ello que, para aprender los pasos fundamentales a la hora de controlar archivos con Git, resolveremos el siguiente problema:

- Necesitamos una secuencia de un gene para probar que nuestro programa `reverse-complement` trabaja correctamente.


##### Metodología
1. **En un archivo de texto, coloca la secuencia de DNA del gene *araC* de *E.coli* en formato fastA (puedes obtenerla aqui http://regulondb.ccg.unam.mx/sequence?type=GN&term=ECK120000050&format=fasta ).**

Desde la terminal de comandos de Bash ejecuté el comando ***wget*** para descargar el archivo en mi escritorio:
'''Bash
wget -O e_coli_araC_secuence.fna http://regulondb.ccg.unam.mx/sequence?type=GN&term=ECK120000050&format=fasta
'''

Ahora desde la terminal de comandos de Git, moví el archivo del escritorio al directorio ***data*** situado en la carpeta del projecto ***reverse_complement***.
'''
mv e_coli_araC_sequence.fna pythonI/projects/reverse_complement/data/
'''

Luego me moví al directorio ***data***.
'''
cd pythonI/projects/reverse_complement/data/
'''

Una vez en el directorio, uso el comando ***add*** para enviar el archivo e_coli_araC_sequence.fna al área de preparación.
'''
git add e_coli_araC_sequence.fna
'''

Posteriormente, uso el comando ***commit*** para confirmar que quiero que Git controle el archivo.
'''
git commit -m 'Working on E. Coli araC sequence' e_coli_araC_sequence.fna
'''

Finalmente, uso el comando ***status*** para verificar que se ha realizado exitosamente.
'''
git status
'''


##### Resultados y Conclusiones
Los retultados pueden encontrarse en [mi repostortio de GitHub](https://github.com/diegocarcam/pythonI).
