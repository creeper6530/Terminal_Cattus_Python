#Toto je deklarace příkazu "pomoc".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Deklarace funkce
def pomoc():
    #Deklarace obsahu pomoci
    pomoc = """Vítej v nápovědě pro terminál Cattus!
    
    Seznam příkazů:
    tisk                Vytiskne daný argument.
                        (Poznámka pro trouby: 'vytiskne' znamená vypíše do terminálu na další řádek.)
    smazat              Trvale smaže daný soubor. Soubor ke smazání deklaruješ argumentem.
                        Nezapomeň přidat příponu.
    sm-slozku           Smaže složku. Z bespečnostních důvodů maže jen prázdné složky.
    obsah-sl            Vypíše obsah složky, kde program právě pracuje.
                        Příkaz ti dá na výběr, jestli chceš do výpisu zahrnout i složky.
    akt-adr             Vypíše umístění, kde program právě pracuje.
    zm-adr              Změní umístění, kde program právě pracuje.
                        Pokud chceš o úroveň výše, nastav první argument jako ".." bez uvozovek.
    pomoc               Vypíše tuto pomoc.
    exit                Okamžitě ukončí program. Lze také použít příkaz "konec".

    Terminál Cattus lze vždy okamžitě ukončit klávesovou zkratkou Ctrl+C."""
    
    #Výpis obsahu pomoci
    print(pomoc)
