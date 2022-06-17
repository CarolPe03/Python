def saludo():
    name=input("¿Cuál es tu nombre?: ")
    print("Hola "+name.upper())
    age=input("¿Cuál es tu edad?: ")
    age=int(age)
    print("Tienes ",age," años y en 3 años tendras",(age+3))

if __name__=='__main__':
    #Linea para ejecutarse    
    saludo()

    