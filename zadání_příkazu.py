#Toto je deklarace funkce pro zadávání příkazů.
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven
import os

#Import příkazů
from tisk import tisk
from smazat import smazat
from smazat_slozku import sm_slozku
from obsah_slozky import obsh_slozky
from pomoc import pomoc
from akt_adr import adresář
from zm_adr import zm_adresář
from kdo_jsem import kdojsemja

#Deklarace, zda je uživatel admin
os.environ['admin'] = "False"

#Deklarace funkce
def zadání():
    #Získání admin stavu
    admin = os.getenv('admin')

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
    
    
    elif comm == "sm-slozku":
        složka = input("Zadejte první argument: ")
        sm_slozku(složka) #Zavolá funkci "sm_slozku" naimportovanou výše v bloku programu importující příkazy s argumentem v proměnné "složka".
    
    
    elif comm == "obsah-sl":
        obsh_slozky() #Zavolá funkci "obsh_slozky" naimportovanou výše v bloku programu importující příkazy.
    
    
    elif comm == "pomoc":
        pomoc() #Zavolá funkci "pomoc" naimportovanou výše v bloku programu importující příkazy.
    
    
    elif comm == "exit":
        exit() #Okamžitě ukončí program. Na tom není nic těžkého :-)

    
    elif comm == "konec":
        exit() #Okamžitě ukončí program. Na tom není nic těžkého :-)
    
    
    elif comm == "akt-adr":
        adresář() #Zavolá funkci "adresář" naimportovanou výše v bloku programu importující příkazy.
    
    
    elif comm == "zm-adr":
        adr = input("Zadejte první argument: ")
        zm_adresář(adr) #Zavolá funkci "zm_adresář" naimportovanou výše v bloku programu importující příkazy s argumentem v proměnné adr.

    elif comm == "zm-uzv":
        if admin == "True":
            os.environ['admin'] = "False"
        else:
            os.environ['admin'] = "True"

    elif comm == "kdojsem":
        kdojsemja(admin) #Zavolá funkci "kdojsemja" naimportovanou výše v bloku programu importující příkazy s argumentem v proměnné admin.
    
    else:
        print("Neznámý příkaz. Pokžij příkaz 'pomoc' pro nápovědu.")
