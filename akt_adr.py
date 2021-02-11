#Toto je deklarace příkazu "akt-adr".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven:
import os

#Deklarace funkce
def adresář():
    adr = os.getcwd()
    print(adr)