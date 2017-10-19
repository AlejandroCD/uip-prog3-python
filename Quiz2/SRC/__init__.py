#CREE UN PROGRAMA, SIGUIENDO EL PARADIGMA DE PROGRAMACION ORIENTADA A OBJETOS, QUEPERMITA CALCULAR EL VOLUMEN DE LAS SIGUIENTES FIGURAS GEOMETRICAS: CONO, ESFERA, CILINDRO

from abc import abstractclassmethod

class Figura(object):
    pi = 3.14159265359

    def __init__(self, radio = 0, altura = 0):
        self.radio = radio
        self.altura = altura

    @abstractclassmethod
    def formula(self):
        pass

class Cono(Figura):
    def formula(self):
       return self.pi * (self.radio**2) * (self.altura/3)

class Cilindro(Figura):
    def formula(self):
        return self.pi * (self.radio**2) * self.altura

class Esfera(Figura):
    def formula(self):
        return (4/3)*self.pi*(self.radio**3)

while(True):
    cual = input("1 = Cono \n2 = Cilindro \n3 = Esfera \nCual es la figura: ")

    if cual == "1":
        while(True):
            try:
                radio = int(input("cual es el radio:"))
                if radio > 0:
                    break
                else:
                    print("La respuesta debe ser positiva.")
            except ValueError:
                print("Respuesta inadecuada, trata devuelta.")
        while (True):
            try:
                altura = int(input("Cual es la altura:"))
                if altura > 0:
                    break
                else:
                    print("La respuesta debe ser positiva.")
            except ValueError:
                print("Respuesta inadecuada, trata devuelta.")
        cn = Cono(radio, altura)
        print("El volumen de el Cono es %.2f" % (cn.formula()))
        cont = input("Usar programa devuelta? y = si ")
        if cont.lower() == "y":
            continue
        else:
            break

    elif cual == "2":
        while (True):
            try:
                radio = int(input("cual es el radio:"))
                if radio > 0:
                    break
                else:
                    print("La respuesta debe ser positiva.")
            except ValueError:
                print("Respuesta inadecuada, trata devuelta.")
        while (True):
            try:
                altura = int(input("Cual es la altura:"))
                if altura > 0:
                    break
                else:
                    print("La respuesta debe ser positiva.")
            except ValueError:
                print("Respuesta inadecuada, trata devuelta.")
        cl = Cilindro(radio, altura)
        print("El volumen de el Cono es %.2f" % (cl.formula()))
        cont = input("Usar programa devuelta? y = si ")
        if cont.lower() == "y":
            continue
        else:
            break

    elif cual == "3":
        while (True):
            try:
                radio = int(input("cual es el radio:"))
                if radio > 0:
                    break
                else:
                    print("La respuesta debe ser positiva.")
            except ValueError:
                print("Respuesta inadecuada, trata devuelta.")
        es = Esfera(radio)
        print("El volumen de el Cono es %.2f" % (es.formula()))
        cont = input("Usar programa devuelta? y = si ")
        if cont.lower() == "y":
            continue
        else:
            break

    else:
        print("Respuesta invalida, por favor trate devuelta.")
