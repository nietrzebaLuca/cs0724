def crypt(text, key):
    ret = ""
    for c in text:
        if c.isalpha():
            b = ord('A') if c.isupper() else ord('a')
            new_c = chr((ord(c) - b + key) % 26 + b)
            ret += new_c
        else:
            ret += c
    return ret

def decrypt(text, key):
    return crypt(text, -key)

def main():
    print("cifrare con cesare")
    chosen = int(input("scegli:\n1 - cifrare\n2 - decifrare\n"))

    inn = input("test: \n")
    key = -1
    out = ""

    try:
        key = int(input("di quanto saltare?\t"))
    except ValueError:
        print("un numero intero devi inserire!!")
        return

    if (chosen == 1):
        out = crypt(inn, key)
        print(f"testo cifrato: {out}")
    elif (chosen == 2):
        out = decrypt(inn, key)
        print(f"testo cifrato: {out}")
    else:
        print("input non valido ciccio !!")

if __name__ == "__main__":
    main()
        