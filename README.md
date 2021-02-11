Tento repozitář je repozitář pro projekt terminálu Cattus.

Hlavní program je v souboru cattus.py

Žádné ostatní programy nemá cenu spouštět, ty jen deklarují funkci, která se v hlavním programu naimportuje a spustí.

Hierarchie závislostí vypadá takto:

cattus.py ┐
          ├ knihovna datetime (zabudovaná do Pytonu)
          └ zadání_příkazu.py ┐
                              ├ tisk.py
                              ├ smazat.py ┐
                              │           └ knihovna os (zabudovaná do Pythonu)
                              ├ akt_adr.py ┐
                              │            └ knihovna os (zabudovaná do Pythonu)
                              ├ zm_adr.py ┐
                              │           └ knihovna os (zabudovaná do Pythonu)
                              └ pomoc.py

Vysvětlivka k hierarchii:
Program ve vyšší úrovni je závislý na všech programech v nižší úrovni.
Program ve vyšší úrovni importuje všechny programy v nižší úrovni.
Dva programy ve stejné úrovni na sobě nejsou závislé.
