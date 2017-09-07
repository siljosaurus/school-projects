# Dette programmet lar brukeren legge inn en fahrenheit temperatur som den ønsker å få omregnet til Celcius temperatur.

fahrenheit = input("Skriv inn et tall: ")
# Først laget jeg en variabel der bruker legger inn det tallet den ønsker å konvertere.
omregning = float(fahrenheit) -32 * (5/9)
# Siden "fahrenheit" input fra bruker er en string (tekst), må jeg gjøre inputen om til tallverdier.
# Derfor gjør jeg hele tekstuttrykket om til en float, som fungerer både for heltall input og flyttall input.
# Etterfulgt kommer formelen som regner ut Celsius verdien.
print(fahrenheit ,"Fahrenheit = " ,omregning, "grader Celcius")
# Til slutt printer maskinen ut input verdien som bruker la inn, med den nye Celcius verdien.
