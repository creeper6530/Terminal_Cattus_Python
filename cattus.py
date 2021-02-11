#Tento program je něco jako "programovací jazyk", nebo spíše terminál.
#Jmenuje se Cattus.

#_____________________________________


#Import nezbytných knihoven
import datetime

#Import funkce zadání příkazu
from zadání_příkazu import zadání

#Info po startu
print("Vítej v terminálu Cattus!")
print("Verze: 1.0")
datum = str(datetime.datetime.now())
print("Datum: " + datum)
print("Formát data: Rok-měsíc-den hodina:minuta:sekunda.mikrosekunda")

#Smyčka zadávání příkazů:
while True:
    zadání()