palabra_secreta = "escuela"
intento = 1

print("ADIVINA LA PALABRA SECRETA")
print("TIENES 3 TURNOS")
print("PISTA 1: ES UN LUGAR A QUE SE VA")

while intento < 4:
    if intento == 2:
        print("PISTA 2: USUALMENTE SOLO VAN PERSONAS JOVENES")
    if intento == 3:
        print("PISTA 3: SE VA A APRENDER")
    print("\nTURNO: " + str(intento) + " DE 3")
    palabra = input("PALABRA = ")
    if palabra.lower() == "escuela":
        print("\n\nHAS GANADO!")
        break
    else:
        print("\nADIVINA DEVUELTA!")
        intento += 1

if intento == 4:
    print("PERDISTE!")