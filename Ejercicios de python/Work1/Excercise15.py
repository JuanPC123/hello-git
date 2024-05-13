One = input("escribe algun texto: ")
Two = input("escribe otro texto: ")

One = len(One)
Two = len(Two)

if One > Two:
    print("El primer texto es mas largo", One)
else:
    print("El segundo texto es mas largo" , Two)