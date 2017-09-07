#1 Er dette lovlig kode?
"""
Dette er lovlig kode helt frem til siste linje, if b < 10: print(b + "Hei!").
Fordi vi i printkommandoen skal printe både en int og en str, kan de ikke skilles med +.
Da må man skille med komma. Denne koden vil rett og slett bli ignorert, uten at vi får noen errorbeskjed.
"""

#2 Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
"""
Brukervennlighet:
Et problem kan være at bruker ikke umiddelbart vet hva et heltall er for noe, og skriver inn et flyttall istedet.
Da vil programmet krasje. For å løse dette kunne man lagt inn en errorbeskjed til bruker, der programmet oppfatter
at bruker har lagt inn et flyttall, og deretter forklarer systemet "Desimaler er ikke tillatt, prøv igjen!". Det samme
kunne man gjort om brukeren legger inn bokstaver som input. Det vil være brukervennlig slik at bruker forstår hva den
har gjort siden programmet krasjer.

Bruker låses til tall fra 1-9:
Når brukeren har fått lagt inn riktig type tall, så vil det fortsatt være problematisk når vi kommer til if statementen.
Hvis bruker har skrevet inn et tall som er ==10, vil programmet ikke kjøre gjennom if statement. Det vil det heller ikke
gjøre dersom bruker har skrevet inn et tall som er større enn 10. Så bruker må skrive et tall fra 1-9 for å aktivere if
statementen - alt annet input vil ikke aktivere noe som helst.
"""
