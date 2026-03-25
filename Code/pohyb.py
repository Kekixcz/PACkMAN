while True: #Místo true i>=0. Návaznost na odečet času v countdown.py, pro názornost jsem nechal true, pro ukončení - q.
    pohyb = input(str("Zadej směr pohybu (w/a/s/d): "))
    if pohyb == "q" or pohyb == "Q":
        print("Ukončeno")
        break
    elif pohyb == "w" or pohyb == "W": #Po stisknutí klávesy W jde postava nahoru
        print("Pohyb nahoru")
    elif pohyb == "a" or pohyb == "A": #Po stisknutí klávesy A jde postava doleva
        print("Pohyb doleva")
    elif pohyb == "s" or pohyb == "S": #Po stisknutí klávesy S jde postava dolů
        print("Pohyb dolů")
    elif pohyb == "d" or pohyb == "D": #Po stisknutí klávesy D jde postava doprava
        print("Pohyb doprava") 
    
    else:
        print("Neplatný směr pohybu!") #Pokud hráč stiskne jinou klávesu než již zmíněné nic se nestane