print("=" * 50)
print("   PACMAN GAME - MENU")
print("=" * 50)

# Nastavení - uložená v proměnných
zvuk = "normální"
grafika = "normální"

# HLAVNÍ MENU LOOP
while True:
    print("--- HLAVNÍ MENU ---")
    print("1. Nová hra")
    print("2. Nastavení")
    print("3. ukončit menu")
    print("4. Náš web")
    
    volba = input("Vyber volbu číslem (1(Nová hra)/2(Nastavení)/3(Ukončit menu)/4(Náš web)): ")
    
    # ===== NOVÁ HRA =====
    if volba == "1":
        print("--- Výběr obtížnosti ---")
        obtiznost = input("Vyber obtížnost číslem (1(Easy)/2(Medium)/3(Hard)): ")
        
        if obtiznost == "1":
            print(" EASY MODE")
            print(f"  - Zvuk: {zvuk}")
            print(f"  - Grafika: {grafika}")
            print("     Spouští se PACMAN Easy Mode...")
        elif obtiznost == "2":
            print(" MEDIUM MODE")
            print(f"  - Zvuk: {zvuk}")
            print(f"  - Grafika: {grafika}")
            print("     Spouští se PACMAN Medium Mode...")
        elif obtiznost == "3":
            print(" HARD MODE")
            print(f"  - Zvuk: {zvuk}")
            print(f"  - Grafika: {grafika}")
            print("     Spouští se PACMAN Hard Mode...")
        else:
            print(" Neznámá obtížnost!")
    
    # ===== NASTAVENÍ =====
    elif volba == "2":
        nastaveni_menu = True
        while nastaveni_menu:
            print("--- NASTAVENÍ ---")
            print("1. Zvuk")
            print("2. Grafika")
            print("3. Zpět na hlavní menu")
            
            nas_volba = input("Vyber nastavení číslem (1(Zvuk)/2(Grafika)/3(Zpět)): ")
            
            # ZVUK
            if nas_volba == "1":
                print("--- ZVUK ---")
                print(f"Aktuální: {zvuk}")
                
                print("1. Easy (tichý zvuk)")
                print("2. Medium (normální zvuk)")
                print("3. Hard (hlasitý zvuk)")
                
                zvuk_volba = input("Vyber úroveň zvuku číslem (1(Tichý)/2(normální)/3(hlasitý)): ")
                
                if zvuk_volba == "1":
                    zvuk = "Tichý"
                    print(" Zvuk nastaven na Tichý")
                elif zvuk_volba == "2":
                    zvuk = "Normální"
                    print(" Zvuk nastaven na Normalní")
                elif zvuk_volba == "3":
                    zvuk = "Hlasitý"
                    print(" Zvuk nastaven na Hlasitý")
                else:
                    print(" Neplatná volba!")
            
            # GRAFIKA
            elif nas_volba == "2":
                print("--- Grafika ---")
                print(f"Aktuální: {grafika}")
                print("1. Easy (nízká kvalita)")
                print("2. Medium (střední kvalita)")
                print("3. Hard (vysoká kvalita)")
                
                grafika_volba = input("Vyber kvalitu grafiky číslem (1(Nízká)/2(Střední)/3(Vysoká)): ")
                
                if grafika_volba == "1":
                    grafika = "Nízká"
                    print(" Grafika nastavena na Nízká")
                elif grafika_volba == "2":
                    grafika = "Střední"
                    print(" Grafika nastavena na Střední")
                elif grafika_volba == "3":
                    grafika = "Vysoká"
                    print(" Grafika nastavena na Vysoká")
                else:
                    print(" Neplatná volba!")
                                # ZPĚT
            elif nas_volba == "3":
                print("Vracíte se na hlavní menu...")
                nastaveni_menu = False
# ===== UKONČIT HRU =====
    elif volba == "3":
        jiste = input("Opravdu chceš odejít? (ano/ne): ")
        if jiste == "ano":
            print("Konec hry! Děkuji za hraní!")
            break
            #NÁŠ WEB
    elif volba == "4":
        print("--- Náš web ---")
        web_volba = input("Vyber akci číslem (1(Zkopírovat odkaz)/2(Zpět)) ")
        if web_volba == "1":
              print("Odkaz byl zkopírován")
        elif web_volba == "2":
            print("Vítej zpět na hlavím menu")
        else:
            print(" Neplatná volba!")
    else:
        print(" Neplatná volba! Vyber 1, 2, 3 nebo 4.")
    
    
