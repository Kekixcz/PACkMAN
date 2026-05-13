<<<<<<< HEAD
# ======================================
#     class pro Hráče, Duchy, body
# ======================================
class Hrac:
    def __init__(self, jmeno, hp):
        self.jmeno = jmeno
        self.skore = 0
        self.hp    = 100
        self.killskore = 0

    def __str__(self):
        return f"packman {self.jmeno} | HP: {self.hp} | skore: {self.skore} | kill skore: {self.killskore}"
 #hráč = vygenerovány životy,jmeno, skore, kill skore(počet zabití ducha)

class Duch: 
    def __init__(self, jmeno, hp, demage):
        self.jmeno = jmeno
        self.hp    = hp
        self.demage= demage
    def __str__(self):
        return f"duch {self.jmeno} | HP: {self.hp}"
    def utok(self):
        if hrac.hp > 1 : 
            hrac.hp -= 1
            print(f"nyní máš{hrac.hp}")
        else: pass
        #dodělat co když nemá životy

#duch = vygenerovány životy, jmeno
class Bod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"bod {self.jmeno} | HP: {self.hp}"
#bod = skore pro hráče 
class Megabod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"megabod {self.jmeno} | HP: {self.hp}"
#mega bod = skore pro hráče 

# ======================================
#             HRÁČ SNÍ BOD
# ======================================

if Hrac.hp > 0 and Bod.hp > 0:

    # bod je sněden
    Bod.hp = 0

    # přidání score
    Hrac.skore += 1

    print(f"{Hrac.jmeno} snědl bod!")

    print(f"Skóre hráče: {Hrac.skore}")
# ======================================
#          HRÁČ SNÍ MEGA BOD
# ======================================

if Hrac.hp > 0 and Megabod.hp > 0:

    # mega bod je sněden
    Megabod.hp = 0

    # přidání score
    Hrac.skore += 50

    print(f"{Hrac.jmeno} snědl mega bod!")

    print(f"Skóre hráče: {Hrac.skore}")
# ======================================
#        DUCH MŮŽE SNÍST HRÁČE
#    jen když hráč nesnědl megabod
# ======================================

if Megabod.hp > 0:

    # duch sní hráče
    Hrac.hp -= Duch.demage

    print(f"{Duch.jmeno} snědl hráče {Hrac.jmeno}!")

    print(f"HP hráče: {Hrac.hp}")

else:

    print(f"{Hrac.jmeno} má nesmrtelnost!")
# ======================================
#            HRÁČ SNÍ DUCHA
#          když snědl megabod
#           a dostane score
# ======================================

if Megabod.hp <= 0:

    # hráč sní ducha
    Duch.hp -= 100

    # kill score
    Hrac.killskore += 1

    # přidání score
    Hrac.skore += 100

    print(f"{Hrac.jmeno} snědl ducha {Duch.jmeno}!")

    print(f"Score hráče: {Hrac.skore}")

    print(f"Kill score: {Hrac.killskore}")

else:

    print(f"{Hrac.jmeno} nemá megabod!")



hrac = Hrac("packman", 5)
duch1 = Duch("duch1", 1, 1)
duch2 = Duch("duch1", 1, 1)
duch3 = Duch("duch1", 1, 1)
=======
# ======================================
#     class pro Hráče, Duchy, body
# ======================================
class Hrac:
    def __init__(self, jmeno, hp):
        self.jmeno = jmeno
        self.skore = 0
        self.hp    = 100
        self.killskore = 0

    def __str__(self):
        return f"packman {self.jmeno} | HP: {self.hp} | skore: {self.skore} | kill skore: {self.killskore}"
 #hráč = vygenerovány životy,jmeno, skore, kill skore(počet zabití ducha)

 class Duch: 
    def __init__(self, jmeno, hp, demage):
        self.jmeno = jmeno
        self.hp    = hp
        self.demage= demage
    def __str__(self):
        return f"duch {self.jmeno} | HP: {self.hp}"
    def utok(self):
        if hrac.hp > 1 : 
            hrac.hp -= 1
            print(f"nyní máš{hrac.hp}")
    
#duch = vygenerovány životy, jmeno
class Bod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"bod {self.jmeno} | HP: {self.hp}"
#bod = skore pro hráče 
class Megabod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"megabod {self.jmeno} | HP: {self.hp}"
#mega bod = skore pro hráče 

# ======================================
#             HRÁČ SNÍ BOD
# ======================================

if Hrac.hp > 0 and Bod.hp > 0:

    # bod je sněden
    Bod.hp = 0

    # přidání score
    Hrac.skore += 1

    print(f"{Hrac.jmeno} snědl bod!")

    print(f"Skóre hráče: {Hrac.skore}")
# ======================================
#          HRÁČ SNÍ MEGA BOD
# ======================================

if Hrac.hp > 0 and Megabod.hp > 0:

    # mega bod je sněden
    Megabod.hp = 0

    # přidání score
    Hrac.skore += 50

    print(f"{Hrac.jmeno} snědl mega bod!")

    print(f"Skóre hráče: {Hrac.skore}")
# ======================================
#        DUCH MŮŽE SNÍST HRÁČE
#    jen když hráč nesnědl megabod
# ======================================

if Megabod.hp > 0:

    # duch sní hráče
    Hrac.hp -= Duch.demage

    print(f"{Duch.jmeno} snědl hráče {Hrac.jmeno}!")

    print(f"HP hráče: {Hrac.hp}")

else:

    print(f"{Hrac.jmeno} má nesmrtelnost!")
# ======================================
#            HRÁČ SNÍ DUCHA
#          když snědl megabod
#           a dostane score
# ======================================

if Megabod.hp <= 0:

    # hráč sní ducha
    Duch.hp -= 100

    # kill score
    Hrac.killskore += 1

    # přidání score
    Hrac.skore += 100

    print(f"{Hrac.jmeno} snědl ducha {Duch.jmeno}!")

    print(f"Score hráče: {Hrac.skore}")

    print(f"Kill score: {Hrac.killskore}")

else:

    print(f"{Hrac.jmeno} nemá megabod!")



hrac = Hrac("packman", 5)
duch1 = Duch("duch1", 1, 1)
duch2 = Duch("duch1", 1, 1)
duch3 = Duch("duch1", 1, 1)
>>>>>>> 6a3392f (hlava code)
