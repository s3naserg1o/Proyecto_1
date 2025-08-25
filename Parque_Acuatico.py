edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 6:
    print("Zona infantil con chaleco.")
elif edad >= 6 and edad <= 11:
    print("Toboganes medianos con adulto cerca.")
elif edad >= 12 and edad <= 17:
    print("Toboganes grandes; sin zonas profundas sin adulto.")
elif edad >= 18:
    print("Acceso total y responsabilidad de adulto.")