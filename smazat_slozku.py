#Toto je deklarace příkazu "sm-slozku".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven:
import os

#Deklarace funkce
def sm_slozku(složka):
    
    try:
        os.rmdir(složka)
    except OSError:
        print("Stala se chyba. Nejspíše složka něco obsahuje, nebo daná složka neexistuje.")
    else:
        print("Složka byla úspešně smazána.")