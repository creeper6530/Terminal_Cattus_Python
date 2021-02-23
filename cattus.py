#Tento program je můj vlastní terminál napsaný v Pythonu.
#Jmenuje se Cattus.

#_____________________________________


#Import nezbytných knihoven
import datetime

#Import funkce zadání příkazu
from zadání_příkazu import zadání

#Info po startu
print("Vítej v terminálu Cattus!")
print("Verze: 1.2")
datum = str(datetime.datetime.now())
print("Aktuální datum a čas: " + datum)
print("Formát data a času: Rok-měsíc-den hodina:minuta:sekunda.mikrosekunda")

#Smyčka zadávání příkazů:
while True:
    zadání()
