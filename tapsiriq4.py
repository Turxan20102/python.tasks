parol = input("parolu daxil ele: ")

uzun = len(parol) >= 8
boyuk = any(c.isupper() for c in parol)
kicik = any(c.islower() for c in parol)
reqem = any(c.isdigit() for c in parol)
bosluq = " " in parol

if uzun and boyuk and kicik and reqem and not bosluq:
    print("Tehlukesiz parol")
else:
    print("Parol sene cavab vermir")
