a = float(input("Birinci ededi daxil et: "))
b = float(input("İkinci ededi daxil et: "))
emeliyyat = input("Emeliyyat sec (+, -, *, /): ")

if emeliyyat == "+":
    print("Netice:", a + b)
elif emeliyyat == "-":
    print("Netice:", a - b)
elif emeliyyat == "*":
    print("Netice:", a * b)
elif emeliyyat == "/":
    if b == 0:
        print("Sifira bölmek olmaz!")
    else:
        print("Netice:", a / b)
else:
    print("Emeliyyat tanimadi!")
