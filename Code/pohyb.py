while True: #Místo true i>=0. Návaznost na odečet času v countdown.py, pro názornost jsem nechal true, pro ukončení - q.
    pohyb = input(str("Zadej směr pohybu (w/a/s/d): "))
    if pohyb == "q" or pohyb == "Q":
        print("Ukončeno")
        break
    elif pohyb == "w" or pohyb == "W":
        print("Pohyb nahoru")
    elif pohyb == "a" or pohyb == "A":
        print("Pohyb doleva")
    elif pohyb == "s" or pohyb == "S":
        print("Pohyb dolů")
    elif pohyb == "d" or pohyb == "D":
        print("Pohyb doprava") 
    
    else:
        print("Neplatný směr pohybu!")