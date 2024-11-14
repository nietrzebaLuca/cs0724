import math

def quadrato(n):
    return ("perimetro: ",4*n,"area: ", n*n)
def cerchio(n):
    return ("perimetro: ",2*n*math.pi,"area: ", n*n*math.pi)
def rettangolo(n, m):
    return ("perimetro: ",2*(n+m),"area: ", n*m)

def main():
    print("calcolatore base di superfici e perimetri\nscegli tra:\n1-quadrato\n2-cerchio\n3-rettangolo")
    x = int(input(":"))
    if(x == 1):
        print("hai scelto quadrato: \n")
        n = int(input("inserire un intero: "))
        print(quadrato(n))

    elif(x == 2):
        print("hai scelto cerchio: \n")
        n = int(input("inserire un intero: "))
        print(cerchio(n))
    
    elif(x == 3):
        print("hai scelto rettangolo: \n")
        n = int(input("inserire un intero: "))
        m = int(input("inserire un'altro intero: "))
        print(rettangolo(n,m))
    else:
        return 0

if __name__ == "__main__":
    main()