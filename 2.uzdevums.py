with open("countrie_dataset.csv", "r", encoding="utf-8") as file:
    text = file.read()
    lines = text.splitlines()
    countries_info = []
    for line in lines:
        iso_code = line.split(",")[1]
        country_name = line.split(",")[0]
        phone_code = line.split(",")[2]
        region= line.split(",")[3]
        capital = line.split(",")[4]
        population = line.split(",")[5]
        countries_info.append((country_name, iso_code, phone_code, region, capital, population))

    african_countries = []
    for country in countries_info:
        if country[3] == "Africa":
            african_countries.append(country)
    african_countries.sort(key = lambda country: country[5], reverse=True)
    print("5 apdzīvotākās valstis Āfrikā: ")
    for country in african_countries[:5]:
        print(f"{country[0]} - Iedzīvotāju skaits: {country[5]}")

    print("\nValstis kuru nosaukumos un arī galvaspilsētām ir viens vārds: ")
    for country in countries_info:
        if len(country[0].split()) ==1 and len(country[4].split()) == 1:
            print(f"Valsts: {country[0]}, galvaspilsēta: {country[4]}")


    print("\nValstis Eiropā: ")
    for country in countries_info:
        if country[3] == "Europe":
            print(f"Valsts: {country[0]}")

    print("\nValstis, kuru telefona kods sākas ar +3: ")
    for country in countries_info:
        if country[2].startswith("+3"):
            print(f"Valsts: {country[0]}, telefona kods: {country[2]}")

user_iso_code = input("Ievadiet valsts ISO kodu: ").upper()
for country in countries_info:
    if country[1] == user_iso_code:
        print(f"Valsts nosaukums: {country[0]}")
        print(f"ISO kods: {country[1]}")
        print(f"Tālruņa kods: {country[2]}")
        print(f"Reģions: {country[3]}")
        print(f"Galvaspilsēta: {country[4]}")
        print(f"Iedzīvotāju skaits: {country[5]}")
        break
        