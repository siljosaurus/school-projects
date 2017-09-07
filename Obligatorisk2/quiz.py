# Dette er en quiz som tester brukerens kunnskaper om Apple. Ved å bruke brukerens input Y/N på påstandene får brukeren tilbakemelding på om de har fått riktig svar eller ikke.

"""
OPPGAVETEKST: I dag er Apple verdens største tech-selskap. Men, de har alltid vært frempå.
Test dine kunnskaper om Apple sin fortid!
"""

# Dette er variabelen med poengsummen til brukeren.
sum = 0

# Denne prosedyren sjekker input fra bruker Y/N. Hvis Y, forklarer den spilleregler, for så å sette i gang prosedyren med spørsmålene. Hvis N, starter den prosedyren på nytt.
def intro():
    introduksjon = input("Hei, og velkommen til den store Apple testen! Er du klar for å begynne? Y/N: ")
    if introduksjon == ("Y"):
        print("Du vil nå få 5 påstander. Svar enten Y eller N. Det er 1 poeng for hvert riktig svar.")
        spoorsmaal()
    else:
        intro()
# Denne prosedyren har laget hvert spørsmål som en input, der bruker svarer Y/N. Dersom det blir riktig svar setter den i gang prosedyren riktigSvar, og hvis det blir feil svar setter den i gang prosedyren feilSvar.
def spoorsmaal():
    spm1 = input("1. Steve Wozniak laget de første Apple computerene. Y/N: ")
    if spm1 == ("Y"):
        riktigSvar()
    else:
        feilSvar()

    spm2 = input("2. Den første iPhone ble lansert i 2004. Y/N: ")
    if spm2 == ("N"):
        riktigSvar()
    else:
        feilSvar()

    spm3 = input("3. Apple laget en tablet på starten av 90 tallet. Y/N: ")
    if spm3 == ("Y"):
        riktigSvar()
    else:
        feilSvar()

    spm4 = input("4. Johnny Ive designet skeumorphism for Apple. Y/N: ")
    if spm4 == ("N"):
        riktigSvar()
    else:
        feilSvar()

    spm5 = input("5. Den første macen floppet fordi den hadde for primitivt operativsystem i forhold til konkurrentene. Y/N: ")
    if spm5 == ("N"):
        riktigSvar()
    else:
        feilSvar()

# Denne prosedyren legger til et poeng i sum variabelen for hver gang den blir trigget. "Global" er fordi jeg ikke ønsker å lage ny sum pr gang, men legge til 1 poeng for hver gang den blir trigget.
def riktigSvar():
    global sum
    sum += 1
    print("Riktig!", sum ,"poeng")

# Denne prosedyren blir trigget hver gang det er et feil svar, og da får bruker tilbakemelding om at svaret er feil, og summen er lik som forrige spm.
def feilSvar():
    print("Feil!", sum ,"poeng")

# Denne prosedyren kommer etter at intro prosedyren, og spørsmål prosedyren har kjørt. Spillet er over. Hvis sum er lik 5 eller mer er alt rett. Hvis sum er lik 4 eller mindre er det en eller flere feil.
def totalSum():
    print("Takk for spillet! Du fikk totalt: ", sum ,"poeng")
    if sum >=5:
        print("Gratulerer, alt rett!")
    elif sum <=4:
        print("Bedre lykke neste gang!")

# Denne prosedyren "runder av" hele spillet og lar bruker velge om den vil spille på nytt, og hvis ikke får den et ønske om en fin dag.
def enGangTil():
    egt = input("Vil du spille igjen? Y/N: ")
    if egt == ("Y"):
        intro()
    else:
        print("Ha en fin dag :-)")

# Her trigges først intro prosedyren, som igjen starter spørsmålene avhengig av brukers input.
# Totalsum kommer etter at spillet er ferdig, og runder av der bruker får tilbakemelding om poengsummen.
# EnGangTil prosedyren runder av og gir bruker mulighet til å velge om den vil spille på nytt eller ikke.
intro()
totalSum()
enGangTil()
