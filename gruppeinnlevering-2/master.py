
# Formattering og Variables
# samling av alle vår kode i gruppe 7.
ITALIC = "\033[3m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

Konflikt_1 = False
Konflikt_2 = False
Konflikt_3 = False
Poeng = 0

#Valg meny og Avsluttning av spillet. 

def Valg_Meny():
    print(f"{UNDERLINE}Hvilken konflikt skal Erling løse?{RESET}")
    print()
    print(f"{BOLD}{UNDERLINE}Konflikt 1:{RESET} Silje og Elias")
    print(f"{BOLD}{UNDERLINE}Konflikt 2:{RESET} Hamdi og Hallgeir")
    print(f"{BOLD}{UNDERLINE}Konflikt 3:{RESET} Motivasjon i teamet")
    print()
    print(f"Totalt poengsum: {BOLD}{UNDERLINE}{Poeng}{RESET}")

def Slutt():
    # You beat the game! Or did you? Poengtelling og resultat fra spillet. 
     if Konflikt_1 == True and Konflikt_2 == True and Konflikt_3 == True:
        print()
     if 0 <= Poeng <= 5:
        farge = RED
     elif 6 <= Poeng <= 8:
        farge = YELLOW
     elif 9 <= Poeng <= 10:
        farge = GREEN

     if 0 <= Poeng <= 5:
        print("Du har løst alle 3 konflikter.")
        print (f"Din totalt poengsum er {BOLD}{UNDERLINE}{farge}{Poeng}/10{RESET}. Prosjektet blir ikke ferdig innen fristen. Dette skaper en større konflikt blant Erling og hans gruppe som gjør at den går i oppløsning. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
    
     elif 6 <= Poeng <= 8:
        print("Du har løst alle 3 konflikter.")
        print (f"Din totalt poengsum er {BOLD}{UNDERLINE}{farge}{Poeng}/10{RESET}. Prosjektet går, men grunnet konflikter må fristen utsettes. {BOLD}{ITALIC}{YELLOW}BRA JOBBA!{RESET}")
    
     elif 9 <= Poeng <= 10:
        print("Du har løst alle 3 konflikter.")
        print(f"Din totalt poengsum er {BOLD}{UNDERLINE}{farge}{Poeng}/10{RESET}. prosjektet gjennomføres godt og gruppen går videre til norming-fasen. {BOLD}{ITALIC}{GREEN}GRATULERER!{RESET}")
    
    
    

#Titel
print()
print(f"""
██████╗ ██████╗  ██████╗ ███████╗     ██╗███████╗██╗  ██╗████████╗ █████╗ ██████╗ ██████╗ ███████╗██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝     ██║██╔════╝██║ ██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██╔══██╗
██████╔╝██████╔╝██║   ██║███████╗     ██║█████╗  █████╔╝    ██║   ███████║██████╔╝██████╔╝█████╗  ██║██║  ██║
██╔═══╝ ██╔══██╗██║   ██║╚════██║██   ██║██╔══╝  ██╔═██╗    ██║   ██╔══██║██╔══██╗██╔══██╗██╔══╝  ██║██║  ██║
██║     ██║  ██║╚██████╔╝███████║╚█████╔╝███████╗██║  ██╗   ██║   ██║  ██║██║  ██║██████╔╝███████╗██║██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚═════╝
{MAGENTA}--------{RESET}""")

# Velkommen til spillet! Intro, bakgrunn
print("Erling har blitt prosjektleder for utviklingen av en ny digitalmedborgerportal til kommunen. \n " \
"Han har et team bestående av 10 personer som alle har ulike roller i prosjektet, fra representanter av kommunens IT-avdeling, \n " \
"til sikkerhetseksperter, og brukerprepresentanter. Som prosjektleder, må Erling ta ansvar og håndtere potensielle konflikter som opppstår mellom medlemmene i teamet. \n "
f"{ITALIC}{UNDERLINE}Hvilke løsninger vil være best i de forskjellige konfliktene for å oppnå best resultat i prosjektet?{RESET}")
print(f"{MAGENTA}------{RESET}")


        
while True: # Repetere Valgmeny fram til alle 3 konflikter er True og gjennomfort.
    if Konflikt_1 == True and Konflikt_2 == True and Konflikt_3 == True:
        Slutt()
        break


    Valg_Meny()
    konflikt_valg = input("Velg Konflikt 1, 2, eller 3? ").lower()
    print(f"{MAGENTA}------{RESET}")
    print()

    if konflikt_valg == "1" and Konflikt_1 == True:
        print(f"{GREEN}Denne konflikten er løst, gjerne velge igjen.{RESET}")
        print()
        continue

    if konflikt_valg == "2" and Konflikt_2 == True:
        print(f"{GREEN}Denne konflikten er løst, gjerne velge igjen.{RESET}")
        print()
        continue

    if konflikt_valg == "3" and Konflikt_3 == True:
        print(f"{GREEN}Denne konflikten er løst, gjerne velge igjen.{RESET}")
        print()
        continue

    if konflikt_valg == "hamburger" or konflikt_valg == "fisk" or konflikt_valg == "fish":
        print(f"Gratulerer! Du har funnet en {BOLD}{ITALIC}{MAGENTA}SECRET ENDING!{RESET} \n"
              "Alle fikk mat og snakket om sine problemer. Prosjektet var gjennomført i rekordtid!")
        print()
        exit()

    if konflikt_valg > "3":
        print(f"{YELLOW}Du har valgt '{konflikt_valg}'. Gjerne velg konflikt 1, 2, eller 3.{RESET}")
        print()
        continue

    
    
    if konflikt_valg == "1":
        #Konflikt number 1
        print("Første konflikten er mellom Silje, som er UX-designer, og Elias, som er IT-rådgiver fra kommunen. \n " \
        "Silje og Elias er uenig om prioritering i teknologivalg og design i prosjektet. Elias ønsker å fokusere på det tekniske og tenker på kostnader. Silje har mer fokus på brukervennlighet")
        print()

        print(f"{BOLD}{ITALIC} Hva bør Erling gjøre for å løse konflikten på best mulig måte, og for å redde relasjonen mellom Silje og Elias? {RESET}")
        print()

        print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Bestemme seg for at han går til individuell samtale med Silje, og med Elias. Han stiller argumentene deres opp til diskusjon i et ønske om å skape aksept for hverandres ønsker.")
        print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Inkluderer hele teamet, han håper at gruppens felleskap kan hjelpe med å finne en løsning og komme med innspill til prosjektet og relasjonen deres.")
        print(f"{BOLD}{UNDERLINE}Løsning 3:{RESET} Sette de sammen i et rom med Noa (sikkerhetsekspert) og Hallgeir (brukerrepresentant), for å forsøke å løse situasjonen ved å få relevante fagpersoner i forholded til prosjektet, \n"
            "           deretter roser han Silje og Elias for deres gode arbeid, og oppfordrer dem til å snakke sammen om hendelsen.")
        print()



        #hvilken løsning velger de? KONFLIKT LØSNING 1, If og elif statements som reagerer fra input data.
        Konflikt_Løsning_1 = input("Hva velger du som beste løsning av 1, 2, eller 3? " )

        if Konflikt_Løsning_1 == "1":
            print(f"{MAGENTA}------{RESET}")
            print("De blir mer sinte på hverandre, forsterker egne meninger og blir mer rigide, og de føler seg truffet fordi de føler de er problemet.")
            print(f"{GREEN}+1 Poeng.{RESET}")
            Poeng = Poeng+1
            Konflikt_1 = True
            print()
            continue

        elif Konflikt_Løsning_1 == "2":
            print(f"{MAGENTA}------{RESET}")
            print("Gruppen får en forståelse av hva som må gjøres for å utføre oppgaven, og kommer frem til en hybridløsning som er et godt bidrag til hovedprosjektet. Silje og Elias sin konflikt får ikke nok prioritering, så etter å ha fått prosjektet på avstand blir relasjonen deres nøytral.")
            print(f"{GREEN}+2 Poeng.{RESET}")
            Poeng = Poeng+2
            Konflikt_1 = True
            print()
            continue

        elif Konflikt_Løsning_1 == "3":
            print(f"{MAGENTA}------{RESET}")
            print("De får begge innspill på forslagene de kommer med, blir opplyst faktorer de ikke har tenkt på før, \n " \
            "da konflikten kommer til en slutt, og en løsning på problemet er funnet, samles Silje og Elias for å prate, og ved å få problemstillingen på avstand, blir det lettere for de å løse opp i krangelen \n "
            "Erling sin ros hjalp dem med å føle seg forstått og validert.")
            print(f"{GREEN}+3 Poeng.{RESET}")
            Poeng = Poeng+3
            Konflikt_1 = True
            print()
            continue

        elif Konflikt_Løsning_1 > "3":
            print(f"{MAGENTA}------{RESET}")
            print(f"Oi! Du har valgt {RED}'{Konflikt_Løsning_1}'{RESET}, en løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
            print (f"Din totale poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
                "Prosjektet kunne desverre ikke gjennomføres.")
            
            print()
            exit()



    elif konflikt_valg == "2":
        # So far so good! Intro til konflikt 2.
        print("Erling lærte mye av konflikten mellom Silje og Elias, og ble deretter oppmerksom på at Hamdi og Hallgeir kom til uenighet om hvordan deltagelsen av innbyggerne i folkemøtene skal bli utført. \n " \
        "Som prosjektlederen, tok Erling ansvar i å prøve å hjelpe de med å komme frem til en løsning.")
        print()

        print(f"{BOLD}{ITALIC} Hva burde Erling gjøre? {RESET}")
        print()

        print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Gi dem tydelig påminnelse av tidsfristen, og oppfordre til at Hamdi og Hallgeir skal møtes for å drøfte en kompromissløsning")
        print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Innkalle til møte der Erling også deltar, for å komme frem til løsning med innspill fra alle parter")
        print()



        #hvilken løsning velger de? KONFLIKT LØSNING 2, If og elif statements som reagerer fra input data.
        Konflikt_Løsning_2 = input("Hva velger du som beste løsning av 1 eller 2? " )

        if Konflikt_Løsning_2 == "1":
            print(f"{MAGENTA}------{RESET}")
            print("Hamdi og Hallgeir møtes på veiene av Erling sin beskjed, og etter en diskusjon som eskalerte til en krangel, kom de frem til at de måtte gi slipp på sine preferanser. \n" \
            "Til slutt, har de brukt for lang tid, så de har kommet opp med en løsning som tar hensyn til begge parter, men som fungerer dårlig.")
            print(f"{GREEN}+2 Poeng.{RESET}")
            Poeng = Poeng+2
            Konflikt_2 = True
            print()
            continue

        elif Konflikt_Løsning_2 == "2":
            print(f"{MAGENTA}------{RESET}")
            print("De prater om løsninger, og kommer frem til et felles produkt som er godt nok, og leverer akkurat innenfor tidsfristen Alle er fornøyde med resultatet. ")
            print(f"{GREEN}+4 Poeng.{RESET}")
            Poeng = Poeng+4
            Konflikt_2 = True
            print()
            continue

        elif Konflikt_Løsning_2 > "2":
            print(f"{MAGENTA}------{RESET}")
            print(f"Oi! du har valgt {RED}'{Konflikt_Løsning_2}'{RESET}, en  et løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
            print (f"Din totalt poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
                "Prosjektet kunne desverre ikke gjennomføres.")
            print()
            exit()
            


    elif konflikt_valg == "3":
        # A challenge approaches! Intro til konflikt 3.
        print("Erling må nå prioritere motivasjon i selvet teamet. Han drøftet mulige løsniner")

        print(f"{BOLD}{ITALIC} Hvilken syns du er best? {RESET}")
        print()

        print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Gi rom for prat under prosjektsamarbeidet, tillate kaffepauser når som helst og skaper et avslappet miljø.")
        print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Motivere med belønning, at om de får levert et bra produkt innen fristen får de dra ut å spise, og minner dem på at det er en belønning i slutten av prosjektet.")
        print(f"{BOLD}{UNDERLINE}Løsning 3:{RESET} Ta initiativ til regelmessige felles aktiviteter, der det er frivillig å bli med, men der alle blir inkludert. Dette kan være å gå tur, bowle, eller å gå ut å spise.")
        print()



        #hvilken løsning velger de? KONFLIKT LØSNING 3, If og elif statements som reagerer fra input data.
        Konflikt_Løsning_3 = input("Hva velger du som beste løsning av 1, 2, eller 3? " )

        if Konflikt_Løsning_3 == "1":
            print(f"{MAGENTA}------{RESET}")
            print("Fristene underveis i prosjektet blir holdt, men tempoet er ikke raskt nok og rammene innad i teamet er avslappet.")
            print(f"{GREEN}+1 Poeng.{RESET}")
            Poeng = Poeng+1
            Konflikt_3 = True
            print() 
            continue

        elif Konflikt_Løsning_3 == "2":
            print(f"{MAGENTA}------{RESET}")
            print("Teamet motiveres av belønning i starten av prosjektfasen, men blir fort vandt til tanken og ser ikke på belønningen som motivasjon etter en stund. På slutten av prosjektet, er det likevel en glede å samles for å spise ute.")
            print(f"{GREEN}+2 Poeng.{RESET}")
            Poeng = Poeng+2
            Konflikt_3 = True
            print()
            continue

        elif Konflikt_Løsning_3 == "3":
            print(f"{MAGENTA}------{RESET}")
            print("Faste sammenkomster skaper gode relasjoner blant kollegaene, og gir glede og motivasjon til å jobbe sammen med de andre i gruppen grunnet styrkede relasjoner.")
            print(f"{GREEN}+3 Poeng.{RESET}")
            Poeng = Poeng+3
            Konflikt_3 = True
            print()
            continue

        elif Konflikt_Løsning_3 > "3":
            print(f"{MAGENTA}------{RESET}")
            print(f"Oi! du har valgt {RED}'{Konflikt_Løsning_3}'{RESET}, en løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
            print (f"Din totalt poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
                "Prosjektet kunne desverre ikke gjennomføres.")
            print()
            exit()
            

