# # Parte 1
# from distutils.errors import LibError


# file = open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r')
# print(file)
# lineas = file.readlines()
# print(lineas)
# file.close()
# Parte 2
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#     lineas = archivo.readlines()
#     print(lineas)
# print(lineas)
# for l in lineas:
#     print(l.replace('\n',''))

# Parte 3
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#     contenido= archivo.read()
#     lineas = contenido.split('\n')
#     print(lineas)

# Parte 4
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#     # contenido= archivo.read()
#     # lineas = contenido.split('\n')#Quitamos los saltos de linea
#     print(lineas)
#     pos= archivo.tell()
#     print(pos)#Aqui nos da la posicion del puntero
#     print('El archivo tiene{0} caracteres de longitud'.format(pos))

# Parte 5
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#    archivo.seek(6)#Podemos posicionarnos 
#    pos = archivo.tell()
#    print(lineas)
#    contenido = archivo.read()
#    lineas = contenido.split('\n')
#    print(lineas)

#Parte 6
# Lee los datos antes del caracter numero 7
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#    siguientes7= archivo.read(7)
#    print(siguientes7)


# Parte 7
# Con este leemos el tipo de archivo
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'r') as archivo:
#    print(type(archivo.read())) #Str

# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data2.txt",'rb') as archivo:
#    print(type(archivo.read()))    #Bytes

#Parte 8
# Escribe algo en el archivo que nosotros queremos
# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data1.txt",'w') as archivo:
#  archivo.write('Henrito\nGeovani\nVasquez')

# with open(r"C:\Users\CDS2\Desktop\ManejoDeArchivos\data1.txt",'a') as archivo:
#  archivo.write('\nHenry\nOrellana')