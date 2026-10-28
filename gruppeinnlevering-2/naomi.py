# Gruppeinnlevering 2
print("\nDette er gruppe oppgave 2 i IS-118, i denne oppgaven møter vi Erling(Prosjektleder) og han sitt team.\n" \
"De skal utvikle en ny digital medborgerportal for kommunen. Det har gått seks uker siden de startet.\n" \
"De er i storming fasen av prosjektet men det oppstår noen konflikter, hva bør Erling gjøre?\n")


# Beslutningspunkt 1: Hvordan håndterer Erling konflikten mellom Silje og Elias?
print("\nKonflikt 1: Silje(UX-designer) og Elias(IT-rådgiver) danner en uenighet rundt prioriteringer om brukervennlighet, det tekniske og kostnader\n" \
"\nHva må Erling bestemme seg for å gjøre for å løse denne konflikten?\n" \
"\nLøsning-1: Erling bestemmer seg for at han går til individuell samtale med Silje, og med Elias\n" \
"\nLøsning-2: Elias samler hele gruppen for å sette felles kriterier, og deretter samler et team med de relaterte til løsningen for å utvikle noe som passer kriteriene\n" \
"\nLøsning-3: Erling velger å sette de sammen i et rom med Noa og Hallgeir for å forsøke å løse situasjonen ved å få innspill fra de som har mer kunnskap om hva Elias og Silje kritiserer hverandre for\n")

poengsum = 0
løsning_konflikt_1 = input("Skriv Løsning-1, Løsning-2 eller Løsning-3 her: ")

if løsning_konflikt_1 == "Løsning-1" :
     print("\nDe blir mer sinte på hverandre, forsterker egne meninger og blir mer rigide, og de føler seg truffet fordi de er problemet.\n")
     poengsum = poengsum + 1
     print("Poengsum er: ",poengsum)

elif løsning_konflikt_1 == "Løsning-2":
    print("\nGruppen får en forståelse av hva som må gjøres for å utføre oppgaven, og kommer frem til en god hybridløsning som er et godt bidrag til hovedprosjektet.\n")
    poengsum = poengsum + 2
    print("Poengsum er: ",poengsum)

elif løsning_konflikt_1 == "Løsning-3":
    print("\nDe får begge innspill på forslagene de kommer med, blir opplyst faktorer de ikke har tenkt på før,\n" \
    "og begge forlater rommet med å ikke være helt fornøyde grunnet at de føler de ikke har blitt hørt for deres løsning, og må endre noe de var selvsikre og stolte av.\n")
    poengsum = poengsum + 3
    print("Poengsum er: ",poengsum)
else:
    print("Du la inn en løsning som ikke var mulig, GAME OVER!")
    exit()

# Beslutningspunkt 2: Hvordan håndterer han uenigheten mellom Hamdi og Hallgeir?
print("\nKonflikt 2: Hamdi og Hallgeir er uenige om hvordan deltagelsen av innbyggerne i folekmøtene skal bli utført\n" \
"\nHva må Erling bestemme seg for å gjøre for å løse denne konflikten?\n" \
"\nLøsning-1: Erling gir dem en tydelig påminnelse av tidsfristen, og ønsker at de to skal ta et møte så fort så mulig for å drøfte en kompromissløsning\n" \
"\nLøsning-2: Erling tilkaller til møte med dem, og setter av god til å drøfte løsninger og postivite og negative sider med oppgaven\n")

løsning_konflikt_2 = input("\nSkriv Løsning-1 eller Løsning-2 her: ")

if løsning_konflikt_2 == "Løsning-1" :
    print("\nHamdi og Hallgeir møtes på veiene av Erling sin beskjed, og etter en diskusjon som eskalerte til en krangel, kom de frem til at de måtte gi slipp på sine preferanser. \n" \
    "Til slutt, har de brukt for lang tid, så de har kommet opp med en løsning som tar hensyn til begge parter, men som fungerer svært dårlig.\n")
    poengsum += 2
    print("Poengsum er: ",poengsum)

elif løsning_konflikt_2 == "Løsning-2" :
    print("\nDe prater om løsninger, og kommer frem til et felles produkt som er optimalt, i god tid\n")
    poengsum += 4
    print("Poengsum er: ",poengsum)
else:
    print("Du la inn en løsning som ikke var mulig, GAME OVER!")
    exit()


# Beslutningspunkt 3: Hvordan bevarer han motivasjonen i teamet?
print("\nKonflikt 3: Motivasjonen i teamet forsvinner\n" \
"\nHva må Erling bestemme seg for å gjøre for å løse denne konflikten?\n" \
"\nLøsning-1: Erling gir rom for prat under prosjektsamarbeidet, tillater kaffepauser når som helst og skaper et avslappet miljø.\n" \
"\nLøsning-2: Erling motiverer med belønning, at om de får levert et bra produkt innen fristen får de dra ut å spise, og minner dem på at det er en belønning i slutten av prosjektet.\n" \
"\nLøsning-3: Erling tar initiativ til regelmessige felles aktiviteter, der det er frivillig å bli med, men der alle blir inkludert. Dette kan være å gå tur, bowle, eller å gå ut å spise.\n")

løsning_konflikt_3 = input("\nSkriv Løsning-1, Løsning-2 eller Løsning-3 her: ")

if løsning_konflikt_3 == "Løsning-1" :
    print("\nFristene underveis i prosjektet blir holdt, men tempoet er ikke raskt nok og rammene innad i teamet blir ikke holdt.\n")
    poengsum += 1
    print("Poengsum er: ",poengsum)

elif løsning_konflikt_3 == "Løsning-2" :
    print("\nTeamet motiveres av belønning på starten av prosjektfasen, men blir fort vandt til tanken og ser ikke på belønningen som motivasjon lenger.\n")
    poengsum += 2
    print("Poengsum er: ",poengsum)

elif løsning_konflikt_3 == "Løsning-3" :
    print("\nFaste sammenkomster skaper gode relasjoner blant kollegaene, og gir glede og motivasjon til å jobbe sammen med de andre i gruppen grunnet styrkede relasjoner.\n")
    poengsum += 3
    print("Poengsum er: ",poengsum)
else:
    print("Du la inn en løsning som ikke var mulig, GAME OVER!")
    exit()


# Avslutning: Tre mulige utfall
if poengsum >= 9:
    print("\nPoengsummen din er: ",poengsum, "\nProsjektet gjennomføres godt og gruppen går videre til norming-fasen.\n")
elif poengsum >= 6:
    print("\nPoengsummen din er: ",poengsum, "\nProsjektet går, men grunnet konflikter må fristen utsettes.\n")
elif poengsum >= 4:
    print("\nPoengsummen din er: ",poengsum, "\nProsjektet blir ikke ferdig innen fristen. Dette skaper en større konflikt blant Erling og hans gruppe som gjør at den går i oppløsning.\n")

