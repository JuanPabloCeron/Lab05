
#***************************************************

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("Suma: ",3," + ",8," = ",sumar(3, 8))
 
#***************************************************
   
def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("Resta: ",9," - ",2," = ",restar(9, 2))

#***************************************************    

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print("Multiplicar: ",6," * ",3," = ",multiplicar(6, 3))
    
#****************************************************

def dividir(a, b):

    try: 
        c =   round(a / b, 2)  
        return c
    except ZeroDivisionError as e:
        print ("No se puede dividir entre cero")

if __name__ == "__main__":
    print("Dividir: ",8," / ",2," = ",dividir(8, 3))    

#****************************************************    