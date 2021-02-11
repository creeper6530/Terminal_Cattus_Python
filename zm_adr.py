#Toto je deklarace příkazu "zm-adr".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven:
import os

#Deklarace funkce
def zm_adresář(adr):
    os.chdir(adr)