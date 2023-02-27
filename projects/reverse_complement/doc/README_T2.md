
# Tarea 2: Comparar versiones y restaurar archivos.

#### Diego Carmona Campos
#### Última actualización: 27 de febrero de 2023

##### Introducción.
Git es una herramienta muy poderosa para llevar un control sobre las versiones de nuestros archivos. Esto es porque además de ayudarnos a llevar un registro de los cambios que hacemos, también nos permite visualizar estos cambios así como restaurar versiones anteriores. Es por eso que pondremos en práctica estas funciones al resolver el siguiente problema:

- Necesitamos probar que nuestro programa reverse-complement trabaja correctamente con 2 secuencias.

##### Metodología
1. 1.  En el archivo de DNA que ya tienes creado, agrega la secuencia del gene araB en formato Fasta. 

Desde la terminal de comandos de Bash ejecuté el comando ***wget*** para descargar el archivo en mi escritorio. El archivo lo conseguí de http://regulondb.ccg.unam.mx/search/jsp/files/eck120000049.fna

'''Bash
wget -O e_coli_araB_sequence.fna http://regulondb.ccg.unam.mx/search/jsp/files/eck120000049.fna
'''

Ahora desde la terminal de comandos de Git, moví el archivo del escritorio al directorio ***data*** situado en la carpeta del projecto ***reverse_complement***.
'''
mv e_coli_araB_sequence.fna pythonI/projects/reverse_complement/data/
'''

Luego me moví al directorio ***data***.
'''
cd pythonI/projects/reverse_complement/data/
'''

Una vez en el directorio, agrego el contenido del archivo e_coli_araB_sequence.fna al archivo e_coli_araC_sequence.fna usando **cat**.
''
cat e_coli_araB_sequence.fna >> e_coli_araC_sequence.fna  
'''

2.  **Sube los cambios a git y confirmalos.**

Uso el comando ***commit*** para guardar el cambio.
'''
git commit -m 'Agregué araB a la secuencia araC' e_coli_araC_sequence.fna
'''

Como ya no utilizaré el archivo e_coli_araB_sequence.fna, lo elimino con **rm**.

'''
rm e_coli_araB_sequence.fna
'''

3. **Simula que el gene araC ha sufrido 3 mutaciones en su secuencia, cambia 3 nucleótidos.**

Usando **vi** abro el archivo e_coli_araC_sequence.fna y modifico 3 nucleotidos.
'''
vi e_coli_araC_sequence.fna
'''

4. **Agrega los cambios a git y confirmalos.**

Confirmo los cambios.
'''
git commit -m 'Modifiqué 3 nucleotidos de araC' e_coli_araC_sequence.fna
'''

5. **Haz las siguientes comparaciones del archivo: última vs penútima y última vs antepenúltima.**

Uso **log** para revisar mi hitorial de **commits**.
'''
git log --oneline
'''

Para comparar el archivo con la última versión, uso el ID del penúltimo **commit**.
'''
git diff 606d81a e_coli_araC_sequence.fna
'''

Para comparar el archivo con la penúltima versión, uso el ID del antepenúltimo **commit**.
'''
git diff 9d89c56 e_coli_araC_sequence.fna
'''

6. Restaura la versión del archivo que no tiene las mutaciones.

Una vez identificado el **commit** al que quiero regresar, uso **checkout** para restaurar la versión.
'''
git checkout 606d81a e_coli_araC_sequence.fna
'''

Finalmente guardo los cambios:
'''
git commit -m 'Restauré la secuencia original de araC' e_coli_araC_sequence.fna
'''


##### Resultados y Conclusiones
Los retultados pueden encontrarse en [mi repostortio de GitHub](https://github.com/diegocarcam/pythonI).
