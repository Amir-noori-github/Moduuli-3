# Python Moduuli-3 tehtävä_2, Valintarakenne (if)

# Kysytään käyttäjältä hyttiluokkaa
hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C): ").upper()

# Tarkistetaan hyttiluokka ja tulostetaan vastaava kuvaus
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
