#--- Gruppeinnlevering 2 ---


#--- Introduksjon ---
# Det legges til poeng for hver løsning.
poeng = 0 

print("Se for deg at du er prosjektleder Erling.")
print("Det har gått 6 uker siden Erling samlet sitt prosjektteam for første gang.")
print("Etter en god start med høy energi, begynner samarbeidet i prosjektet å få flere utfordringer.")
print()
print("Videre vil du bli representert ulike konflikter som har oppstått i løpet av prosjektet som du må prøve å finne løsningen på.")
print()
print()


#--- Konflikt 1 ---
print("Konflikt 1: Silje og Elias. Utviklet seg fra å være en sakskonflikt til å bli en personkonflikt. Teknologivalg vs. Design.")
print("Silje mener løsningen til Elias vil låse brukeropplevelsen og hindre innovasjon. Elias mener at Silje sitt forslag er usikkert og kostbart.")
print()

print("Hvilken løsning vil du gå for: ")
print("A: Erling bestemmer seg for at han går til individuell samtale med Silje og Elias.")
print("B: Erling samler hele gruppen i håp om å finne løsningen for å utvikle noe som passer kriteriene, en hybridløsning.")
print("C: Erling velger å plassere Silje og Elias med personer som har mer kunnskap for at Silje og ELias skal få innspill for det de kritiserer hverandre for. Oppfordrer de til å snakke om hendelsen.")
print()

svar1 = input("Løsning? (a, b eller c): ").lower()

if svar1 == "a":
    poeng += 1
    print("Silje og Elias blir mer sinte på hverandre og forsterker egene meninger. De føler seg truffet fordi at de er problemet, men etter litt tid forstår begge at samtalene var et håp om en god løsning som tar hensyn til følelsene. +1 poeng.")
elif svar1 == "b":
    poeng += 2
    print("Gruppen får en forståelse av hva som må gjøres for å utføre oppgaven, en hybridløsning. Dette krever ressurser fra gruppeprosjektet, men etter løsningen, går relasjonene over til nøytral. +2 poeng.")
elif svar1 == "c":
    poeng += 3
    print("Silje og Elias synes det er ukomfortabelt, men får innspill og blir opplyst med faktorer de ikke hadde tenkt på før. Begge blir fornøyd. +3 poeng.")
else:
    print("Svar med a, b eller c.")
print()
print()


#--- Konflikt 2 ---
print("Konflikt 2: Hamdi og Hallgeir. Kulturavdelingen vs. Brukerrepresentant. Uenige om hvordan innbyggerene skal kunne delta i digitale folkemøter.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende platform. Hallgeir ønsker et mer åpent og dialogbasert system med rom for spontane innspill.")
print()

print("Hvilken løsning vil du gå for: ")
print("A: Erling gir dem tydelig påminnelse, og de to møtes for å drøfte om kompromissløsning.")
print("B: Erling kaller inn til møte med Hamdi og Hallgeir for å komme frem til løsning og positive og negative sider med oppgaven.")
print()

svar2 = input("Løsning? (a eller b): ").lower()

if svar2 == "a":
    poeng += 2
    print("Etter en diskusjon som eskalerte til en krangel, kom Hamdi og Hallgeir frem til at de måtte gi slipp på sine preferanser. Brukt lang tid. En løsning som tar hensyn til begge parter, men som fungerer dårlig. +2 poeng.")
elif svar2 == "b":
    poeng += 4
    print("De prater om løsninger og kommer frem til et felles produkt som er optimalt og i god tid. +4 poeng.")
else:
    print("Svar med a eller b.")
print()
print()


#--- Konflikt 3 ---
print("Konflikt 3: Hvordan bevare motivasjonen i teamet: ")
print()

print("Hvilken løsning vil du gå for: ")
print("A: Erling gir rom for prat under prosjektsamarbeidet, tillater kaffepauser og skaper et avslappet miljø.")
print("B: Erling minner på og motiverer med at medlemmene får belønning i slutten av prosjektet.")
print("C: Erling tar initiativ til regelmessige felles frivillige aktiviteter for inkludering.")
print()

svar3 = input("Løsning? (a, b eller c): ").lower()

if svar3 == "a":
    poeng += 1
    print("Fristene underveis i prosjektet blir holdt, men det er lite tempo. Rammene innad i teamet blir ikke holdt. +1 poeng.")
elif svar3 == "b":
    poeng += 2
    print("Teamet motiveres av belønning i starten, men etter hvert ser de ikke på belønningen som motivasjon lengre. +2 poeng.")
elif svar3 == "c":
    poeng += 3
    print("Sammenkomster skaper gode relasjoner, gir glede og motivasjon til å jobbe sammen grunnet styrkede relasjoner. +3 poeng.")
else:
    print("Svar med a, b eller c.")
print()
print()


#--- Resultatet av løsningene til Erling ---
if poeng >= 9:
    print(f"Du fikk {poeng} poeng til sammen! Prosjektet gjennomføres godt, og gruppen går videre til norming-fasen.")
elif poeng >= 6:
    print(f"Du fikk {poeng} poeng til sammen! Prosjektet går, men grunnet konflikter må fristen utsettes.")
else:
    print(f"Du fikk {poeng} poeng til sammen! Prosjektet blir ikke ferdig innen fristen. Dette skaper en større konflikt blant Erling og gruppen som gjør at den går i oppløsning.")
print()
