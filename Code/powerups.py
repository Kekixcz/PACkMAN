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
    if powerup == "1":
        if cas>175:
            print("Je mi líto, maximlní časový limit by dosažen!")
            break
        else:
            cas += 5
            print(f"Časový power up byl sebrán! Nyní más {cas} sekund. ")
            break
    if powerup == "2":
        if zivoty == 3:
            print("Již máš maximlní počet životů!")
            break
        elif zivoty == 2:
            zivoty += 1
            print("Nyní máš planý počet životů")
            break
        elif zivoty == 1:
            zivoty += 1
            print(f"Život navíc se vždycky hodí!! Nyní más {zivoty} životy. ")
            break
    if powerup == "3":
        print("Nyní máš nesmrtelnost na 5 sekund")
        z = zivoty
        zivoty = 100
        time.sleep(5)
        zivoty = z
        z = 0
        print(f"Jsi smrtelník, nyní máš {zivoty} životů")
        break
