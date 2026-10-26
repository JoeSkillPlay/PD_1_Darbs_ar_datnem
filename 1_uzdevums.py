with open("countrie_info.txt", "r") as file:
    text = file.read()
    lines = text.splitlines()
    valstis_count = len(lines)

    print("Valstu skaits:", valstis_count)

    valstis = []
    for line in lines:
        valsts = line.split("-", 1)[0]
        valstis.append(valsts)

    valstis.sort()
    print("Valstu nosaukumi alfabētiskā secībā:")
    for valsts in valstis:
        print(valsts)

    garakais_valsts = max(valstis, key=len)
    print("Garākais valsts nosaukums:", garakais_valsts)
    isakais_valsts = min(valstis, key=len)
    print("Īsākais valsts nosaukums:", isakais_valsts)

    
          
