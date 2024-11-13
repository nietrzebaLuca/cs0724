

def main():
        l1 = []
	l2 = []
        
	print("generatore nomi di band")
	n = int(input("inserire un numero (fidati inseriscilo): "))
        print()
	listaCitta(n, l1)
	print()
	listaAnimali(n, l2)
	print()
	stringOutput(l1, l2)

def stringOutput(l1, l2):
        for i in range(len(l1)):
                print("nome della band: "+l1[i]+" "+l2[i])
                      

def listaCitta(m, l):
        print(f"inserisci {m} nomi di citta")
        for i in range(m):
                s = str(input("inserisci citta di origine: "))
                l.append(s)

def listaAnimali(m, l):
        print(f"inserisci {m} nomi di animali")
        for i in range(m):
                s = str(input("inserisci animale domestico: "))
                l.append(s);

if __name__ == "__main__":
        main()
