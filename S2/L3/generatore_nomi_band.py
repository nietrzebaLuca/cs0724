
def main():
	print("generatore nomi di band")
	print()
	s1 = str(input("inserire nome citta origine: "))
	s2 = str(input("inserire nome animale domestico: "))
	print()
	stringOutput(s1, s2)

def stringOutput(a, b):
        print("nome generato: "+a+" "+b)

if __name__ == "__main__":
        main()
