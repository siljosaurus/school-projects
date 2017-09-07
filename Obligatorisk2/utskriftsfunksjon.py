# Dette programmet kommuniserer med brukeren ved å spørre om navn og bosted, for så å printe en personlig hilsen tilbake. Det er lagt opp en prosedyre som kalles 3 ganger.

def navnBosted():
# Her definerer jeg prosedyren, og har kalt den for "navnBosted" ved å bruke bibliotekfunksjonen "def".
    navn = input("Heisann! Hva heter du?: ")
    bosted = input("Hvor bor du?: ")
# Videre har jeg laget to input variabler som spør om navn og bosted, som maskinen innhenter fra bruker.
    print("Hei," ,navn ,"fra", bosted, ":-)")
    print("\n")
# Deretter bruker den informasjon som brukeren har lagt inn til å gi en personlig hilsen tilbake.
# For ordens skyld la jeg inn et tomt linjeskift, da blir det fort mer ryddig og oversiktlig.


def flereGanger():
    navnBosted()
    navnBosted()
    navnBosted()
# Her har jeg laget en prosedyre, som kaller på den ovenstående prosedyren flere ganger.
# Det betyr at den kjører det samme "scriptet" som over, tre ganger.


flereGanger()
# Her kaller jeg på sistnevnte prosedyre, som setter i gang prosedyren "navnBosted" til å kjøre tre ganger etter hverandre.
