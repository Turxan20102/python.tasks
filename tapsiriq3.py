ededler = []
for i in range(5):
    eded = int(input(f"{i+1}-ci ededi daxil et: "))
    if eded not in ededler:
        ededler.append(eded)

print("ferrqli ədədlərin cemi:", sum(ededler))
