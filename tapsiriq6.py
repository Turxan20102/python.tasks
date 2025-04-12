import random

gizli = random.randint(1, 10)
cehd = 0
tapildi = False

while cehd < 3:
    texmin = int(input("ededi  tap (1-10): "))
    cehd += 1

    if texmin == gizli:
        print("Tebrikler gizli ededi tapdun")
        tapildi = True
        break
    elif texmin < gizli:
        print("daha boyuk bir eded cehd et.")
    else:
        print("daha kicik bir eded cehd et.")

if not tapildi:
    print(f"uduzdun gizli ədəd {gizli} di.")
