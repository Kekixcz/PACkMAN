import time
powerup = input("Zadejte číslo:")
#                   1 - +5 sekund
#                   2 - +1 život 
#                   3 - 5s nesmrtelnost
a = True
cas = 150       #čas a životzy jsou proměné v game.py
zivoty = 1
z = 0
while cas>=0: 
    #Sebrán powerup pro přidání 5 sekund
    if powerup == "1":
        #Maximální časový limit (5 sekund nelze přidat)
        if cas>175:
            print("Je mi líto, maximlní časový limit by dosažen!")
            break
        #Přidání 5 sekund k aktuálnímu času a čas vypsán
        else:
            cas += 5
            print(f"Časový power up byl sebrán! Nyní más {cas} sekund. ")
            break
    #Sebrán powerup pro přidání 1 života
    if powerup == "2":
        #Maximální počet životů (1 život nelze přidat)
        if zivoty == 3:
            print("Již máš maximlní počet životů!")
            break
        #Přidání 1 života a ohlášení maxima životů
        elif zivoty == 2:
            zivoty += 1
            print("Nyní máš planý počet životů")
            break
        #Přidání 1 života a vypsání aktuálního počtu
        elif zivoty == 1:
            zivoty += 1
            print(f"Život navíc se vždycky hodí!! Nyní más {zivoty} životy. ")
            break
    #Sebrán powerup pro přidání 5s nesmrtelnosti
    if powerup == "3":
        #Jsi nesmrtelný na 5s
        print("Nyní máš nesmrtelnost na 5 sekund")
        z = zivoty
        zivoty = 100
        time.sleep(5)
        zivoty = z
        z = 0
        #Čas vypršel jsi znovu smrtelníkem
        print(f"Jsi smrtelník, nyní máš {zivoty} životů")
        break
