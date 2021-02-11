#Toto je deklarace příkazu "tisk".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import příkazů
from tisk import tisk
from smazat import smazat
from pomoc import pomoc
from akt_adr import adresář
from zm_adr import zm_adresář

#Deklarace funkce
def zadání():
    #Zadání příkazu
    print()
    comm = input(">>> ")

    #Detekce příkazu
    if comm == "tisk":
        obsah = input("Zadejte první argument: ")
        tisk(obsah) #Zavolá funkci "tisk" naimportovanou výše v programu bloku importující příkazy s argumentem v proměnné "obsah".
    elif comm == "smazat":
        soubor = input("Zadejte první argument: ")
        smazat(soubor) #Zavolá funkci "smazat" naimportovanou výše v bloku programu importující příkazy s argumentem v proměnné "soubor".
    elif comm == "pomoc":
        pomoc() #Zavolá funkci "pomoc" naimportovanou výše v bloku programu importující příkazy.
    elif comm == "exit":
        exit() #Okamžitě ukončí program. na tom není nic těžkého :-)
    elif comm == "akt-adr":
        adresář() #Zavolá funkci "adresář" naimportovanou výše v bloku programu importující příkazy.
    elif comm == "zm-adr":
        adr = input("Zadejte první argument: ")
        zm_adresář(adr) #Zavolá funkci "zm_adresář" naimportovanou výše v bloku programu importující příkazy.
    else:
        print("Neznámý příkaz.")