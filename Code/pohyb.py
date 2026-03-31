while True: #Místo true i>=0. Návaznost na odečet času v countdown.py, pro názornost jsem nechal true, pro ukončení - q.
    pohyb = input(str("Zadej směr pohybu (w/a/s/d): "))
    if pohyb == "q" or pohyb == "Q":
        print("Ukončeno")
        break
    elif pohyb == "w" or pohyb == "W":
        #Postava jde nahoru
        print("Pohyb nahoru")
    elif pohyb == "a" or pohyb == "A":
        #Postava jde doleva
        print("Pohyb doleva")
    elif pohyb == "s" or pohyb == "S":
        #Postava jde dolů
        print("Pohyb dolů")
    elif pohyb == "d" or pohyb == "D":
        #Postava jde doprava
        print("Pohyb doprava") 
    
    else:
        #Pokud hráč stiskne jinou klávesu než již zmíněné nic se nestane
        print("Neplatný směr pohybu!")