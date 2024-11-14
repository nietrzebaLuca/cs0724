import math

def quadrato(n):
    return f"perimetro: {4*n}, area: {n*n}"
def cerchio(n): 
    return f"perimetro: {2*n*math.pi}, area: {n*n*math.pi}"
def rettangolo(n, m):
    return f"perimetro: {2*(n+m)}, area: {n*m}"

def main():
    print("calcolatore base di superfici e perimetri\nscegli tra:\n1-quadrato\n2-cerchio\n3-rettangolo")

    try:
        x = int(input(": "))
        
        if(x == 1):
            print("hai scelto quadrato: ")
            n = int(input("inserire un intero (x>0): "))
            print(quadrato(n))
        elif(x == 2):
            print("hai scelto cerchio: \n")
            n = int(input("inserire un intero (x>0): "))
            print(cerchio(n))
        elif(x == 3):
            print("hai scelto rettangolo: \n")
            n = int(input("inserire un intero (x>0): "))
            m = int(input("inserire un'altro intero (x>0): "))
            print(rettangolo(n,m))
        else:
            print("invalido !!!")
    except ValueError:
        print("ERROR: numero non valido")

if __name__ == "__main__":
    main()
