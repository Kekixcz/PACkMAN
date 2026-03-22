body = int(input("Zadej počet bodů: "))
cas = int(input("Zadej počet sekund: "))
zivoty = int(input("Zadej počet životů: "))
umrel = input("Umřel jsi? (ano/ne): ")
# Posbírá jsi všechny body?
if body == 100:
    print("Vyhrál jsi!")
    print("Konec hry")
else:
    #Máš čas a umřel jsi?
    if cas > 0  and umrel == "ano" and zivoty == 1:
        print("Zemřel jsi!")
        print("Konec hry")
    #Máš čas a neumřel jsi?
    elif cas > 0 and umrel == "ne":
        print("Máš dostatek času!")
        print("Pokračuj dál!")
       
    #Máš čas, umřel jsi, ale máš ještě životy?
    elif cas > 0 and umrel == "ano" and zivoty > 1:
        print("Máš dostatek času!")
        print("Pokračuj dál!")
    #Nemáš čas?
    else:
        print("Nemáš dostatek času!")
        print("Konec hry")
