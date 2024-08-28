# Python Moduuli-3 tehtävä_1, Valintarakenne (if)
# Kysytään kalastajalta kuhan pituutta
pituus = float(input("Anna kuhan pituus senttimetreinä: "))
# Valintarakenne (if),
# Määritellään kuhan alimmainen sallittu pyyntimitta
alamitta = 37.0

# Tarkistetaan, onko kuha alamittainen
if pituus < alamitta:
    puuttuva_mitta = alamitta - pituus
    print(f"Kuha on alamittainen. Laita se takaisin järveen! "
          f"Kuha on {puuttuva_mitta:.1f} cm liian lyhyt.")
else:
    print("Kuha on sallittua pyyntimittaa.")
