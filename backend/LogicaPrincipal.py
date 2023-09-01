
class Telecomunicaciones:

    def __init__(self,tamaño ):
        self.colas = []
        self.tamaño = tamaño
        self.contdor = 0

    def append(self):
        pass

tamaño = int(input("Ingrese el número de personas que quiere ingresar a la cola: "))
def requerimiento(cola=[], contador=0):
    # Nombre de solicitud, Nombre de persona, Descripción del problema, Nivel de urgencia

    if tamaño == contador:
        print("Cola de solicitudes:")
        for solicitud in cola:
            print(solicitud)
        return

    else:
        nombreDeSolicitud = str(input("Por favor ingrese su número de solicitud: "))
        nombre = str(input("Por favor ingrese su nombre: "))
        descripcion = str(input("Por favor ingrese la descripción de su solicitud: "))

        while True:
            urgencia = str(input("Por favor ingrese su nivel de urgencia del 1 al 3: "))
            if urgencia == "1" or urgencia == "2" or urgencia == "3":
                break
            else:
                print("Recuerde que el valor de urgencia debe estar entre 1 y 3.")

        solicitud = [nombreDeSolicitud, nombre, descripcion, urgencia]
        cola.append(solicitud)

        contador += 1
        return requerimiento(cola, contador)

variable = requerimiento()

