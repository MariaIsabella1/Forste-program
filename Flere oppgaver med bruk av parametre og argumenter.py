import math

def siHeiTil(navn):
  print(f"Hei, {navn}!")

def arealKvadrat(side):
    areal = side*side
    print(f"Arealet av et kvadrat med side {side:.2e} er {areal:.4e}")

arealKvadrat(5)

#Lag en funksjon som regner ut arealet av en sirkel. Funksjonen skal ta ett tall som parameter og skrive ut setninger som «Arealet av en sirkel med radius 2 er 12.56» i konsollen.

def arealSirkel(radius):
    areals = math.pi*radius**2
    print(f"Arealet av en sirkel med radius {radius} er {areals:.2e} ")

arealSirkel(2)

#Lag en funksjon med to parametre, en by og et land. Funksjonen skal skrive ut en tekst som denne: «Oslo er en by i Norge.»

def byOgLand(by,land):
    print(f"{by} er en by i {land}")

byOgLand("Stockholm", "Sverige")

#Lag funksjonen minst(a, b) som tar to tall, a og b , som parametre og skriver ut det minste av tallene.

def minst(a,b):
    if a > b:
        print(f"{b} er det minste tallet")
    elif a < b:
        print(f"{a} er det minste tallet")
    else:
        print("De er like store")

minst(10,2)

#Lag funksjonen navneskilt(navn) , som lager et skilt ved hjelp av tegn rundt det oppgitte navnet. For eksempel:

def navneskilt(navn):
    print(f"+----------+","\n","|",navn,"|","\n", "+---------+")

navneskilt("Louise")

def maria(alder, høyde):
    a = høyde/alder
    print(a)
    if a < 10:
        print("du er kul")
    elif a > 10:
        print("du er ukul")
    else:
        print("what?!")

print("Hello")
