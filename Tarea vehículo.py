# Importamos la libreria time
import time
# Creamos la clase vehiculo
class Vehiculo:

    garaje = []
    __estado_vehiculo = False
    __tanque = 0
# creamos una funcion para inicializar
    def __init__(self, tipo, modelo, capacidad_tanque, distancia_x_tanque, tanque, distancia_recorrida):
        self.garaje.append(self.__estado_vehiculo)
        self.__tipo = tipo
        self.garaje.append(self.__tipo)
        self.__modelo = modelo
        self.garaje.append(self.__modelo)
        self.__capacidad_tanque = capacidad_tanque
        self.garaje.append(self.__capacidad_tanque)
        self.__distancia_x_tanque = distancia_x_tanque
        self.garaje.append(self.__distancia_x_tanque)
        self.__tanque = tanque
        self.garaje.append(self.__tanque)
        self.__distancia_recorrida = distancia_recorrida
        self.garaje.append(self.__distancia_recorrida)
# Función para ver el garaje
    def ver_garaje(self):
        for i in self.garaje:
            print(i)
# Función para encender el vehiculo
    def encender(self):
        if self.__estado_vehiculo:
            print("\nVehículo encendido.")
        else:
            print("\nEncendiendo vehículo.")
            proceso = "..."
            for i in proceso:
                print(i)
                time.sleep(1)
            self.__estado_vehiculo = True
            print("Vehículo encendido. \n")
# funcion para apagar el vehiculo
    def apagar(self):
        if self.__estado_vehiculo:
            print("\nApagando vehículo.")
            proceso = "..."
            for i in proceso:
                print(i)
                time.sleep(1)
            self.__estado_vehiculo = False
            print("Vehículo apagado.\n")
        else:
            print("\nVehículo apagado.")
# funcion para avanzar
    def avanzar(self, distancia_avanzada):
        if self.__estado_vehiculo == False:
            self.encender()
            if self.__tanque <= 0:
                print("El tranque vacío, necesita ser llenado. Puede hacerlo desde el menú anterior.")
            else:
                proceso = "..."
                for i in proceso:
                    print(i)
                    time.sleep(1)
                print(f"El vehículo avanzó {distancia_avanzada}.\n")
        else:
            proceso = "..."
            for i in proceso:
                print(i)
                time.sleep(1)
            print(f"El vehículo avanzó {distancia_avanzada}.\n")
# funcion para retroceder
    def retroceder(self, distancia_retrocedida):
        if self.__estado_vehiculo == False:
            self.encender()
            if self.__tanque <= 0:
                print("El tranque vacío, necesita ser llenado. Puede hacerlo desde el menú anterior.")
            else:
                proceso = "..."
                for i in proceso:
                    print(i)
                    time.sleep(1)
                print(f"El vehículo retrocedió {distancia_retrocedida}.\n")
        else:
            proceso = "..."
            for i in proceso:
                print(i)
                time.sleep(1)
            print(f"El vehículo retrocedió {distancia_retrocedida}.\n")
# Creamos una clase para vehiculos terrestres
class Terrestre(Vehiculo):

    estado_baul = False

    def cargar_baul(self):
        if self.estado_baul:
            print("\nEl baúl ha sido cargado.\n")
        else:
            self.estado_baul = True
            print("\nEl baúl se cargó con éxito.\n")
    
    def descargar_baul(self):
        if self.estado_baul:
            self.estado_baul = False
            print("\nSe descargo el baúl con éxito.\n")
        else:
            print("\nEl baúl está vacío.\n")
# Creamos una clase para vehiculos maritimo
class Maritimo(Vehiculo):

    estado_red = False

    def lanzar_red(self):
        if self.estado_red:
            print("\nLa red ha sido lanzada.\n")
        else:
            self.estado_red = True
            print("\nLa red se lanzó con éxito.\n")
    
    def pescar_red(self):
        if self.estado_red:
            self.estado_red = False
            print("\nSe pescó con éxito.\n")
        else:
            print("\nLa red ya se pescó.\n")
# Creamos una clase para vehiculos aereo
class Aereo(Vehiculo):
    
    estado_frenado = False

    def frenar(self):
        if self.estado_frenado:
            print("\nSe ha frenado con éxito. A como 9G.\n")
        else:
            self.estado_red = True
            print("\nSe frenó con éxito. A como 9G.\n")
    
    def espintar(self):
        if self.estado_frenado:
            self.estado_frenado = False
            print("\nSobrepasó a los aviones alemanes con éxito.\n")
        else:
            print("\nYa se derrotaron los aviones de la luftwaffe.\n")

class Cabina:

    terrestre = Terrestre("Terrestre", "Carro", 50, 800, 50, 0)
    maritimo = Maritimo("Marítimo", "Barco", 25, 675, 25, 0)
    aereo = Aereo("Aéreo", "Avión", 300, 5000, 300, 0)

    print("        Menú")
    print("1 - Crear vehículo. \n2 - Ver garaje, manejar vehículo. \nPara salir ingrese un número mayor a 2.")
    opcion = int(input("Ingrese una opción (numérica): "))
    while opcion <= 4:
        if opcion == 1:
            print("\n1 - Terrestre. \n2 - Marítimo. \n3 - Aéreo. \n4 - salir (presione cualquier tecla).")
            opcion = input("¿Qué tipo de vehículo necesitará?: ")
            if opcion == "1":
                modelo = input("Modelo del vehículo: ")
                capacidad_tanque = int(input("Capacidad del tanque (litros): "))
                distancia_x_tanque = int(input("Distancia por tanque (kilómetros): "))
                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                if opcion == "1":
                    tanque = int(input("Cantidad de litros que ingresará: "))
                    if tanque <= capacidad_tanque:
                        terrestre = Terrestre("Terrestre", modelo.strip(), capacidad_tanque, distancia_x_tanque, tanque, 0)
                    else:
                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                        terrestre = Terrestre("Terrestre", modelo.strip(), capacidad_tanque, distancia_x_tanque, capacidad_tanque, 0)
                else:
                    terrestre = Terrestre("Terrestre", modelo.strip(), capacidad_tanque, distancia_x_tanque, 0, 0)
            elif opcion == "2":
                modelo = input("Modelo del vehículo: ")
                capacidad_tanque = int(input("Capacidad del tanque (litros): "))
                distancia_x_tanque = int(input("Distancia por tanque (millas náuticas): "))
                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                if opcion == "1":
                    tanque = int(input("Cantidad de litros que ingresará: "))
                    if tanque <= capacidad_tanque:
                        maritimo = Maritimo("Maritímo", modelo.strip(), capacidad_tanque, distancia_x_tanque, tanque, 0)
                    else:
                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                        maritimo = Maritimo("Maritímo", modelo.strip(), capacidad_tanque, distancia_x_tanque, capacidad_tanque, 0)
                else:
                    maritimo = Maritimo("Maritímo", modelo.strip(), capacidad_tanque, distancia_x_tanque, 0, 0)
            elif opcion == "3":
                modelo = input("Modelo del vehículo: ")
                capacidad_tanque = int(input("Capacidad del tanque (litros): "))
                distancia_x_tanque = int(input("Distancia por tanque (nudos): "))
                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                if opcion == "1":
                    tanque = int(input("Cantidad de litros que ingresará: "))
                    if tanque <= capacidad_tanque:
                        aereo = Aereo("Aéreo", modelo.strip(), capacidad_tanque, distancia_x_tanque, tanque, 0)
                    else:
                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                        aereo = Aereo("Aéreo", modelo.strip(), capacidad_tanque, distancia_x_tanque, capacidad_tanque, 0)
                else:
                    aereo = Aereo("Aéreo", modelo.strip(), capacidad_tanque, distancia_x_tanque, 0, 0)
        elif opcion == 2:
            terrestre.ver_garaje()
            opcion = input("¿Desea manejar un vehículo? (1/ presione cualquier tecla): ")
            if opcion == "1":
                vehiculo = input("Ingrese el nombre del vehículo que desea manejar (Ya están tres ejemplos que puede utilizar nombres: Carro, Barco y Avión): ")
                if vehiculo not  in maritimo.garaje:
                    print("El vehículo no existe. Puede agregarlo desde el menú.")
                else:
                    index = aereo.garaje.index(vehiculo)
                    if terrestre.garaje[index - 1] == "Terrestre":
                        print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Cargar baúl. \n7 - Descargar baúl. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                        opcion = int(input("Ingrese una opción: "))
                        while opcion <= 8:
                            if opcion == 1:
                                terrestre.encender()
                            elif opcion == 2:
                                distancia_avanzada = int(input("¿Cuántos kilómetros avanzará?: "))
                                terrestre.avanzar(distancia_avanzada)
                                terrestre.garaje[index + 4] += distancia_avanzada
                                terrestre.garaje[index + 3] -= ((terrestre.garaje[index + 1] / terrestre.garaje[index + 2]) * distancia_avanzada)
                                print("Datos del vehiculo después de avanzar:")
                                print(f"Tipo: {terrestre.garaje[index - 1]}")
                                print(f"Modelo: {terrestre.garaje[index]}")
                                print(f"Capacidad del tanque: {terrestre.garaje[index + 1]}")
                                print(f"Distancia por tanque: {terrestre.garaje[index + 2]}")
                                print(f"Tanque: {terrestre.garaje[index + 3]}")
                                print(f"Distancia recorrida: {terrestre.garaje[index + 4]} kilómetros.")
                            elif opcion == 3:
                                distancia_retrocedida = int(input("¿Cuántos kilómetros retrocederá?: "))
                                terrestre.retroceder(distancia_retrocedida)
                                terrestre.garaje[index + 4] += distancia_retrocedida
                                terrestre.garaje[index + 3] -= ((terrestre.garaje[index + 1] / terrestre.garaje[index + 2]) * distancia_retrocedida)
                                print("Datos del vehiculo después de retroceder:")
                                print(f"Tipo: {terrestre.garaje[index - 1]}")
                                print(f"Modelo: {terrestre.garaje[index]}")
                                print(f"Capacidad del tanque: {terrestre.garaje[index + 1]}")
                                print(f"Distancia por tanque: {terrestre.garaje[index + 2]}")
                                print(f"Tanque: {terrestre.garaje[index + 3]}")
                                print(f"Distancia recorrida: {terrestre.garaje[index + 4]} kilómetros.")
                            elif opcion == 4:
                                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                                if opcion == "1":
                                    tanque = int(input("Cantidad de litros que ingresará: "))
                                    terrestre.garaje[index + 3] += tanque
                                    if terrestre.garaje[index + 3] >= terrestre.garaje[index + 1]:
                                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                                    else:
                                        print("El tranque se llenó con éxito.")                                 
                            elif opcion == 5:
                                print(f"La distancia recorrida por el vehículo {vehiculo} es de: {terrestre.garaje[index + 4]} kilómetros \n")
                            elif opcion == 6:
                                terrestre.cargar_baul()
                            elif opcion == 7:
                                terrestre.descargar_baul()
                            elif opcion == 8:
                                terrestre.apagar()
                            print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Cargar baúl. \n7 - Descargar baúl. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                            opcion = int(input("Ingrese una opción: "))
                    elif maritimo.garaje[index - 1] == "Marítimo":
                        print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Lanzar red. \n7 - Pescar. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                        opcion = int(input("Ingrese una opción: "))
                        while opcion <= 8:
                            if opcion == 1:
                                maritimo.encender()
                            elif opcion == 2:
                                distancia_avanzada = int(input("¿Cuántas millas náuticas avanzará?: "))
                                maritimo.avanzar(distancia_avanzada)
                                maritimo.garaje[index + 4] += distancia_avanzada
                                maritimo.garaje[index + 3] -= ((maritimo.garaje[index + 1] / maritimo.garaje[index + 2]) * distancia_avanzada)
                                print("Datos del vehiculo después de avanzar:")
                                print(f"Tipo: {maritimo.garaje[index - 1]}")
                                print(f"Modelo: {maritimo.garaje[index]}")
                                print(f"Capacidad del tanque: {maritimo.garaje[index + 1]}")
                                print(f"Distancia por tanque: {maritimo.garaje[index + 2]}")
                                print(f"Tanque: {maritimo.garaje[index + 3]}")
                                print(f"Distancia recorrida: {maritimo.garaje[index + 4]} millas náuticas.")
                            elif opcion == 3:
                                distancia_retrocedida = int(input("¿Cuántas millas náuticas retrocederá?: "))
                                maritimo.retroceder(distancia_retrocedida)
                                maritimo.garaje[index + 4] += distancia_retrocedida
                                maritimo.garaje[index + 3] -= ((maritimo.garaje[index + 1] / maritimo.garaje[index + 2]) * distancia_retrocedida)
                                print("Datos del vehiculo después de retroceder:")
                                print(f"Tipo: {maritimo.garaje[index - 1]}")
                                print(f"Modelo: {maritimo.garaje[index]}")
                                print(f"Capacidad del tanque: {maritimo.garaje[index + 1]}")
                                print(f"Distancia por tanque: {maritimo.garaje[index + 2]}")
                                print(f"Tanque: {maritimo.garaje[index + 3]}")
                                print(f"Distancia recorrida: {maritimo.garaje[index + 4]} millas náuticas.")
                            elif opcion == 4:
                                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                                if opcion == "1":
                                    tanque = int(input("Cantidad de litros que ingresará: "))
                                    maritimo.garaje[index + 3] += tanque
                                    if maritimo.garaje[index + 3] >= maritimo.garaje[index + 1]:
                                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                                    else:
                                        print("El tranque se llenó con éxito.")                                 
                            elif opcion == 5:
                                print(f"La distancia recorrida por el vehículo {vehiculo} es de: {maritimo.garaje[index + 4]} millas náuticas \n")
                            elif opcion == 6:
                                maritimo.lanzar_red()
                            elif opcion == 7:
                                maritimo.pescar_red()
                            elif opcion == 8:
                                maritimo.apagar()
                            print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Lanzar red. \n7 - Pescar. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                            opcion = int(input("Ingrese una opción: "))
                    elif aereo.garaje[index - 1] == "Aéreo":
                        print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Frenar. \n7 - Espintar. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                        opcion = int(input("Ingrese una opción: "))
                        while opcion <= 8:
                            if opcion == 1:
                                aereo.encender()
                            elif opcion == 2:
                                distancia_avanzada = int(input("¿Cuántos nudos avanzará?: "))
                                aereo.avanzar(distancia_avanzada)
                                aereo.garaje[index + 4] += distancia_avanzada
                                aereo.garaje[index + 3] -= ((aereo.garaje[index + 1] / aereo.garaje[index + 2]) * distancia_avanzada)
                                print("Datos del vehiculo después de avanzar:")
                                print(f"Tipo: {aereo.garaje[index - 1]}")
                                print(f"Modelo: {aereo.garaje[index]}")
                                print(f"Capacidad del tanque: {aereo.garaje[index + 1]}")
                                print(f"Distancia por tanque: {aereo.garaje[index + 2]}")
                                print(f"Tanque: {aereo.garaje[index + 3]}")
                                print(f"Distancia recorrida: {aereo.garaje[index + 4]} nudos.")
                            elif opcion == 3:
                                distancia_retrocedida = int(input("¿Cuántos nudos retrocederá?: "))
                                aereo.retroceder(distancia_retrocedida)
                                aereo.garaje[index + 4] += distancia_retrocedida
                                aereo.garaje[index + 3] -= ((aereo.garaje[index + 1] / aereo.garaje[index + 2]) * distancia_retrocedida)
                                print("Datos del vehiculo después de retroceder:")
                                print(f"Tipo: {aereo.garaje[index - 1]}")
                                print(f"Modelo: {aereo.garaje[index]}")
                                print(f"Capacidad del tanque: {aereo.garaje[index + 1]}")
                                print(f"Distancia por tanque: {aereo.garaje[index + 2]}")
                                print(f"Tanque: {aereo.garaje[index + 3]}")
                                print(f"Distancia recorrida: {aereo.garaje[index + 4]} nudos.")
                            elif opcion == 4:
                                opcion = input("¿Desea llenar su tanque? (1/ presione cualquier tecla): ")
                                if opcion == "1":
                                    tanque = int(input("Cantidad de litros que ingresará: "))
                                    aereo.garaje[index + 3] += tanque
                                    if aereo.garaje[index + 3] >= aereo.garaje[index + 1]:
                                        print("La capacidad del tanque impide esa cantidad de gasolina (el tanque se llenó hasta su máxima capacidad)")
                                    else:
                                        print("El tanque se llenó con éxito.")                                 
                            elif opcion == 5:
                                print(f"La distancia recorrida por el vehículo {vehiculo} es de: {aereo.garaje[index + 4]} nudos \n")
                            elif opcion == 6:
                                aereo.frenar()
                            elif opcion == 7:
                                aereo.espintar()
                            elif opcion == 8:
                                aereo.apagar()
                            print("1 - Encender. \n2 - avanzar. \n3 - Retroceder. \n4 - Llenar el tanque. \n5 - Distancia recorrida. \n6 - Frenar. \n7 - Espintar. \n8 - Apagar \nPara salir ingrese un número mayor a 8.")
                            opcion = int(input("Ingrese una opción: "))
        print("        Menú")
        print("1 - Crear vehículo. \n2 - Ver garaje, manejar vehículo. \nPara salir ingrese un número mayor a 2.")
        opcion = int(input("Ingrese una opción (numérica): "))