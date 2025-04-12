cumle = input("bir cümle daxil et: ")
soz_sayi = len(cumle.split())
saitler = "aeiouAEIOUəiöüƏİÖÜ"
sait_say = sum(1 for c in cumle if c in saitler)
samit_say = sum(1 for c in cumle if c.isalpha() and c not in saitler)

print("Söz sayi:", soz_sayi)
print("sait sayi:", sait_say)
print("samit sayi:", samit_say)

if "Python" in cumle:
    print(f"'Python' sözünün indeksi: {cumle.index('Python')}")
else:
    print("'Python' sözü taplmadi.")
