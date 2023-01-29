"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Jan Březina
email: brezinajan@proton.me
discord: Ruuda #1658
"""


TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

uzivatele = {
"bob": "123", 
"ann": "pass123", 
"mike": "password123", 
"liz": "pass123"
}

oddelovac = ("-" * 45)

pocet_vel_pismeno_zacatek = 0
pocet_velka_pismena = 0
pocet_mala_pismena = 0
pocet_cisel = 0
suma_cisel = 0
delka_slov_cetnost = dict()
pocet_delka_slov_cetnost = 0

uzivatel = input("Uživatelské jméno: ")
heslo = input("Heslo: ")

if uzivatel in uzivatele and heslo == uzivatele [uzivatel]:
    print(oddelovac)
    print(f"Vítej v naší aplikaci, {uzivatel}.")
    print("Máme 3 texty k analýze")
    print(oddelovac)
    text = input("Zvol text od 1 do 3: ")
    print(oddelovac)
    if text.isnumeric() and 0 < int(text) < 4:
        zvoleny_text = TEXTS[int(text)-1].split()
        vycisteny_text = list()
        
        for slovo in zvoleny_text:
            vycisteny_text.append(slovo.strip(".,:!?"))
        
        for slovo in vycisteny_text:
            if slovo.istitle():
               pocet_vel_pismeno_zacatek += 1
            elif slovo.isupper():
               pocet_velka_pismena += 1
            elif slovo.islower():
               pocet_mala_pismena += 1
            elif slovo.isnumeric():
                pocet_cisel += 1 
                suma_cisel += int(slovo)
            else:
                continue
        
        for slovo in vycisteny_text:
            delka_slova = len(slovo)
            if delka_slova not in delka_slov_cetnost:
                pocet_delka_slov_cetnost = 1
                delka_slov_cetnost [delka_slova] = pocet_delka_slov_cetnost
            else:
                pocet_delka_slov_cetnost = int(delka_slov_cetnost [delka_slova]) + 1
                delka_slov_cetnost [delka_slova] = pocet_delka_slov_cetnost

        pocet_slov = len(vycisteny_text)
        
        if pocet_slov > 4 or pocet_slov == 0:
            print(f"V textu se nachází {pocet_slov} slov.")
        elif 1 < pocet_slov < 5:
            print(f"V textu se nachází {pocet_slov} slova.")
        else:
             print(f"V textu se nachází {pocet_slov} slovo.")
        
        if pocet_vel_pismeno_zacatek > 4 or pocet_vel_pismeno_zacatek == 0:
            print(f"V textu se nachází {pocet_vel_pismeno_zacatek} slov začínajících velkým písmenem.")
        elif 1 < pocet_vel_pismeno_zacatek < 5:
            print(f"V textu se nachází {pocet_vel_pismeno_zacatek} slova začínající velkým písmenem.")
        else:
            print(f"V textu se nachází {pocet_vel_pismeno_zacatek} slovo začínající velkým písmenem.")
        
        if pocet_velka_pismena > 4 or pocet_velka_pismena == 0:
            print(f"V textu se nachází {pocet_velka_pismena} slov psaných velkými písmeny.")
        elif 1 < pocet_velka_pismena < 5:
            print(f"V textu se nachází {pocet_velka_pismena} slova psaná velkými písmeny.")
        else:
            print(f"V textu se nachází {pocet_velka_pismena} slovo psané velkými písmeny.")
        
        if pocet_mala_pismena > 4 or pocet_mala_pismena == 0:
            print(f"V textu se nachází {pocet_mala_pismena} slov psaných malými písmeny.")
        elif 1 < pocet_mala_pismena < 5:
            print(f"V textu se nachází {pocet_mala_pismena} slova psaná malými písmeny.")
        else:
            print(f"V textu se nachází {pocet_mala_pismena} slovo psané malými písmeny.")
        
        if pocet_cisel > 4 or pocet_cisel == 0:
            print(f"V textu se nachází {pocet_cisel} čísel.")
        elif 1 < pocet_cisel < 5:
            print(f"V textu se nachází {pocet_cisel} čísla.")
        else:
            print(f"V textu se nachází {pocet_cisel} číslo.")
       
        print(f"Součet všech čísel v textu je {suma_cisel}.")
       
        print(oddelovac)
        print(f"DÉLKA|{'VÝSKYT'.center(max(delka_slov_cetnost.values()) + 2)}|POČET")
        print(oddelovac)
        
        for delka in sorted(delka_slov_cetnost):
            print(
            f"{str(delka).rjust(5)}|"
            f"{int(delka_slov_cetnost[delka]) * '*'}"
            f"{' ' * (max(delka_slov_cetnost.values()) - delka_slov_cetnost[delka] + 2)}|"
            f"{delka_slov_cetnost[delka]}"
            ) 
    else:
        print("Špatně zvolený text. Ukončuji program.")
        quit()
else:
    print("Neregistovaný uživatel. Ukončuji program.")
    quit()