#Toto je deklarace příkazu "pomoc".
#Je v odděleném souboru pro větší přehlednost kódu

#_______________________________


#Deklarace funkce
def pomoc():
    #Deklarace obsahu pomoci
    pomoc = """Vítejte v nápovědě pro terminál Cattus!
    
    Seznam příkazů:
    tisk                Vytiskne daný argument.
                        (Poznámka pro trouby: 'vytiskne' znamená vypíše do terminálu na další řádek.)
    smazat              Trvale smaže daný soubor. Soubor ke smazání deklaruješ argumentem.
                        Nezapomeň přidat příponu.
                        Takže pokud máš soubor Wordu jménem "dopis", tak napiš do argumentu "dopis.docx" bez uvozovek.
    pomoc               Vypíše tuto pomoc.
    akt-adr             Vypíše umístění, kde program právě pracuje.
    zm-adr              Změní umístění, kde program právě pracuje.
                        Pokud chceš o úroveň výše, nastav první argument jako ".." bez uvozovek.
    exit                Okamžitě ukončí program.

    Terminál Cattus lze vždy okamžitě ukončit klávesovou zkratkou Ctrl+C."""
    
    #Výpis obsahu pomoci
    print(pomoc)