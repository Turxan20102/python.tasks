a = float(input("Birinci ededi daxil et: "))
b = float(input("İkinci ededi daxil et: "))
emeliyyat = input("Əməliyyat sec (+, -, *, /): ")

if emeliyyat == "+":
    print("Nəticə:", a + b)
elif emeliyyat == "-":
    print("Nəticə:", a - b)
elif emeliyyat == "*":
    print("Nəticə:", a * b)
elif emeliyyat == "/":
    if b == 0:
        print("Sifira bölmek olmaz!")
    else:
        print("Nəticə:", a / b)
else:
    print("Əməliyyat tanimadi!")
