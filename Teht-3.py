# Python Moduuli-3 tehtävä_3, Valintarakenne (if)

# Kysytään käyttäjältä biologinen sukupuoli
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()

# Kysytään käyttäjältä hemoglobiiniarvo
hb_arvo = float(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkistetaan sukupuolen perusteella hemoglobiiniarvon taso
if sukupuoli == "nainen":
    if hb_arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif 117 <= hb_arvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb_arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif 134 <= hb_arvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")
