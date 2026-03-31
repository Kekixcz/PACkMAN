import time
print("Zapíná se hra")
# odpočet do startu
print("3") 
time.sleep(1)
print("2") 
time.sleep(1)
print("1") 
time.sleep(1)
# hra začala
print("Start, časový limit je 180s")

try:
    for i in range(179,0, -1):
        i=i+1
        
        if i==0:
            # vypršel čas
            print("Konec hry")
            break
        else:
            # odpočítávání času
            print(i)
            time.sleep(1)
except KeyboardInterrupt:
    # uživatel stiskl (ctrl + c) a sám ukončil hru
    print("\n\nHra byla ukončena uživatelem")



#Pozměnil jsem, bývalá kod počítal od 1-180, nyní kód jde 180-0, + hru můžeme stisknutím ctrl + c ukončit