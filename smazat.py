#Toto je deklarace příkazu "smazat".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven:
import os

#Deklarace funkce
def smazat(soubor):
    if os.path.exists(soubor):
        os.remove(soubor)
        print("Soubor byl úspešně smazán")
    else:
        print("Daný soubor neexistuje")