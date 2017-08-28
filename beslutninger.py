# Dette programmet lar bruker korrespondere med maskinen. Ved hjelpe av else/if statements kan programmet gi forskjellige svar ut fra brukerens input.

inp = input ("Har du lyst på en brus?: ")
if (inp == "Ja" or inp == "ja"):
    print("Her har du en brus")
# Jeg starter med å lage en input variabel sammen med en tekststring som spør bruker om den har lyst på en brus.
# Etterfulgt kommer en if statement, der programmet skal utføre en print funksjon dersom brukeren har svart ja (her valgte jeg også å legge inn mulighet for bruker å skrive med både stor og liten J for å gjøre programmet hakket mer brukervennlig).

elif (inp == "Nei" or inp == "nei"):
    print("Den er grei.")
# Her bruker jeg en elif (else if) statement siden programmet skal gi forskjellig output svar avhengig om bruker svarer ja eller nei.

else:
    print("Det forstod jeg ikke helt.")
# Til sist har jeg lagt til en else statement, slik at maskinen responderer med tekststringen "Det forstod jeg ikke helt" når bruker skriver inn noe som ikke samsvarer med if + elif over.
