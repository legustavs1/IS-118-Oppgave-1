
# Formattering og Variables
ITALIC = "\033[3m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

Poeng = 0

#Titel
print("")
print(f"""
██████╗ ██████╗  ██████╗ ███████╗     ██╗███████╗██╗  ██╗████████╗ █████╗ ██████╗ ██████╗ ███████╗██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝     ██║██╔════╝██║ ██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██╔══██╗
██████╔╝██████╔╝██║   ██║███████╗     ██║█████╗  █████╔╝    ██║   ███████║██████╔╝██████╔╝█████╗  ██║██║  ██║
██╔═══╝ ██╔══██╗██║   ██║╚════██║██   ██║██╔══╝  ██╔═██╗    ██║   ██╔══██║██╔══██╗██╔══██╗██╔══╝  ██║██║  ██║
██║     ██║  ██║╚██████╔╝███████║╚█████╔╝███████╗██║  ██╗   ██║   ██║  ██║██║  ██║██████╔╝███████╗██║██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚═════╝
{MAGENTA}--------{RESET}""")

# Velkommen til spillet! Intro, bakgrunn og intro til konflikt 1.
print("Erling har blitt prosjektleder for utviklingen av en ny digitalmedborgerportal til kommunen. \n " \
"Han har fått en team som består av 10 folk som har forskjellige roller, fra representanter av kommunens IT-avdeling, til sikkerhetseksperter, og brukerprepresentanter. \n ")
print("Som prosjektleder, opplever Erling at det blir konflikter mellom de forskjellige medlemmer i teamet. \n "
f"{ITALIC}{UNDERLINE}Hva er beste løsning i de forskjellige konflikter til å ha beste resultat i prosjektet?{RESET}")

print(f"{MAGENTA}------{RESET} \n" \
"Første konflikten er mellom Silje, som er UX-designer, og Elias, som er IT-rådgiver fra kommunen. \n " \
"De er uenig om prioritering rundt prioriteringer. Elias fil ha fokus på Tekniske og kostnader, mens Silje har mer fokus på brukervennlighet. ")
print("")

print(f"{BOLD}{ITALIC} Hva burde Erling gjør til å løse konflikten best? {RESET}")
print("")

print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Bestemme seg for at han går til individuell samtale med Silje, og med Elias.")
print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Samle hele gruppen for å sette felles kriterier, og deretter samler et team med de relaterte til løsningen for å utvikle noe som passer kriteriene.")
print(f"{BOLD}{UNDERLINE}Løsning 3:{RESET} Velge å sette de sammen i et rom med Noa og Hallgeir for å forsøke å løse situasjonen ved å få innspill fra de som har mer kunnskap om hva \n"
      "           Elias og Silje kritiserer hverandre for.")
print("")



#hvilken løsning velger de? KONFLIKT LØSNING 1, If og elif statements som reagerer fra input data.
Konflikt_Løsning_1 = input("Hva velger du som beste løsning av 1, 2, eller 3? " )

if Konflikt_Løsning_1 == "1":
    print(f"{MAGENTA}------{RESET}")
    print("De blir mer sinte på hverandre, forsterker egne meninger og blir mer rigide, og de føler seg truffet fordi de er problemet.")
    Poeng = Poeng+1
    print("")

elif Konflikt_Løsning_1 == "2":
    print(f"{MAGENTA}------{RESET}")
    print("Gruppen får en forståelse av hva som må gjøres for å utføre oppgaven, og kommer frem til en god hybridløsning som er et godt bidrag til hovedprosjektet.")
    Poeng = Poeng+2
    print("")

elif Konflikt_Løsning_1 == "3":
    print(f"{MAGENTA}------{RESET}")
    print("De får begge innspill på forslagene de kommer med, blir opplyst faktorer de ikke har tenkt på før, \n " \
    "og begge forlater rommet med å ikke være helt fornøyde grunnet at de føler de ikke har blitt hørt for deres løsning, \n "
    "og må endre noe de var selvsikre og stolte av.")
    Poeng = Poeng+3
    print("")

elif Konflikt_Løsning_1 > "3":
    print(f"{MAGENTA}------{RESET}")
    print(f"Oi! du har valgt et løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
    print (f"Din totalt poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
           "prosjekten desverre gjennomført ikke.")
    
    print("")
    exit()




# So far so good! Intro til konflikt 2.
print("Etterpå, fant Erling ut at Hamdi og Hallgeir er uenige om hvordan deltagelsne av innbyggerne i folkemøtene skal bli utført. \n " \
"Som prosjektlederen, er det Erling sitt ansvar å prøve å finne hjelpe de komme seg fram til en løsning")
print("")

print(f"{BOLD}{ITALIC} Hva burde Erling gjør? {RESET}")
print("")

print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Gi dem tydelig påminnelse, og de to møtes for å drøfte kompromissløsning")
print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Innkalle til møte der Erling deltar,for å komme frem til løsning")
print("")



#hvilken løsning velger de? KONFLIKT LØSNING 2, If og elif statements som reagerer fra input data.
Konflikt_Løsning_1 = input("Hva velger du som beste løsning av 1 eller 2? " )

if Konflikt_Løsning_1 == "1":
    print(f"{MAGENTA}------{RESET}")
    print("Hamdi og Hallgeir møtes på veiene av Erling sin beskjed, og etter en diskusjon som eskalerte til en krangel, kom de frem til at de måtte gi slipp på sine preferanser. \n" \
    "Til slutt, har de brukt for lang tid, så de har kommet opp med en løsning som tar hensyn til begge parter, men som fungerer svært dårlig.")
    Poeng = Poeng+2
    print("")

elif Konflikt_Løsning_1 == "2":
    print(f"{MAGENTA}------{RESET}")
    print("De prater om løsninger, og kommer frem til et felles produkt som er optimalt, i god tid. ")
    Poeng = Poeng+4
    print("")

elif Konflikt_Løsning_1 > "2":
    print(f"{MAGENTA}------{RESET}")
    print(f"Oi! du har valgt et løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
    print (f"Din totalt poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
           "prosjekten desverre gjennomført ikke.")
    print("")
    exit()



# A Challenger approaches! Intro til konflikt 3.
print("Siste problem Erling merket var motivasjon i selvet teamet. Han satt lenge å drøftet om noen mulig løsning")

print(f"{BOLD}{ITALIC} Hvilken syns du er best? {RESET}")
print("")

print(f"{BOLD}{UNDERLINE}Løsning 1:{RESET} Gi rom for prat under prosjektsamarbeidet, tillate kaffepauser når som helst og skaper et avslappet miljø.")
print(f"{BOLD}{UNDERLINE}Løsning 2:{RESET} Motivere med belønning, at om de får levert et bra produkt innen fristen får de dra ut å spise, og minner dem på at det er en belønning i slutten av prosjektet.")
print(f"{BOLD}{UNDERLINE}Løsning 3:{RESET} Ta initiativ til regelmessige felles aktiviteter, der det er frivillig å bli med, men der alle blir inkludert. Dette kan være å gå tur, bowle, eller å gå ut å spise.")
print("")



#hvilken løsning velger de? KONFLIKT LØSNING 3, If og elif statements som reagerer fra input data.
Konflikt_Løsning_1 = input("Hva velger du som beste løsning av 1, 2, eller 3? " )

if Konflikt_Løsning_1 == "1":
    print(f"{MAGENTA}------{RESET}")
    print("Fristene underveis i prosjektet blir holdt, men tempoet er ikke raskt nok og rammene innad i teamet blir ikke holdt.")
    Poeng = Poeng+1
    print("") 

elif Konflikt_Løsning_1 == "2":
    print(f"{MAGENTA}------{RESET}")
    print("Teamet motiveres av belønning på starten av prosjektfasen, men blir fort vandt til tanken og ser ikke på belønningen som motivasjon lenger.")
    Poeng = Poeng+2
    print("")

elif Konflikt_Løsning_1 == "3":
    print(f"{MAGENTA}------{RESET}")
    print("Faste sammenkomster skaper gode relasjoner blant kollegaene, og gir glede og motivasjon til å jobbe sammen med de andre i gruppen grunnet styrkede relasjoner.")
    Poeng = Poeng+3
    print("")

elif Konflikt_Løsning_1 > "3":
    print(f"{MAGENTA}------{RESET}")
    print(f"Oi! du har valgt et løsning som ikke var mulig. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")
    print (f"Din totalt poengsum var: {BOLD}{UNDERLINE}{Poeng}{RESET} \n "
           "prosjekten desverre gjennomført ikke.")
    print("")
    exit()



# You beat the game! Or did you? Poengtelling og resultat fra spillet. 
print("")
if 0 <= Poeng <= 5:
    print (f"Din totalt poengsum er {BOLD}{UNDERLINE}{Poeng}{RESET}. Prosjektet blir ikke ferdig innen fristen. Dette skaper en større konflikt blant Erling og hans gruppe som gjør at den går i oppløsning. {BOLD}{ITALIC}{RED}GAME OVER!{RESET}")

elif 6 <= Poeng <= 8:
    print (f"Din totalt poengsum er {BOLD}{UNDERLINE}{Poeng}{RESET}. Prosjektet går, men grunnet konflikter må fristen utsettes. {BOLD}{ITALIC}{YELLOW}BRA JOBBA!{RESET}")

elif 9 <= Poeng <= 10:
    print(f"Din totalt poengsum er {BOLD}{UNDERLINE}{Poeng}{RESET}. prosjektet gjennomføres godt og gruppen går videre til norming-fasen. {BOLD}{ITALIC}{GREEN}GRATULERER!{RESET}")