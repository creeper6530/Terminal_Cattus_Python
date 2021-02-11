#Toto je deklarace příkazu "obsah-slozky".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Import nezbytných knihoven:
import os

#Deklarace funkce
def obsh_slozky():
    
    typ = input("Chcete do výpisu zahrnout i složky? Pokud ne, vypíšou se jen soubory. (Y/N): ")
    
    
    if typ == "n":
        print(list(filter(os.path.isfile, os.listdir())))
    elif typ == "y":
        print(os.listdir())
    

    elif typ == "N":
        print(list(filter(os.path.isfile, os.listdir())))
    elif typ == "Y":
        print(os.listdir())

    
    else:
        print("Špatné zadání.")