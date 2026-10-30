poeng = 0
konflikt1_ferdig = False
konflikt2_ferdig = False
konflikt3_ferdig = False
while True:
        print(f"Total poeng: {poeng}")
        #print("Totalt poeng: ",poeng) notat til meg selv okei
        print("Hva bør Erling gjøre?")
        print("1. Ta opp konflikten mellom Silje og Elias")
        print("2. Ta opp konflikten mellom Hamdi og Hallgeir")  
        print("3. Fikse motivasjonen innad teamet")
        Valg = (input("Erling bør: "))
        if Valg=="1" and konflikt1_ferdig==True:
                print ()
                print("Konflikt 1 er allerede gjordt")
                continue
        elif Valg=="2" and konflikt2_ferdig==True:
                print ()
                print("Konflikt 1 er allerede gjordt")
                continue
        elif Valg=="3" and konflikt3_ferdig==True:
                print ()
                print("Konflikt 1 er allerede gjordt")
                continue #stops the loop and goes back to start
        
        #Oversikt over hovedkonflikter (første ledd)
        if Valg=="1":
                print("Erling velger å ta opp konflikten mellom Silje og Elias")
        elif Valg=="2":
                print("Erling velger å ta opp konflikten mellom Hamdi og Hallgeir")
        elif Valg=="3":
                print("Erling velger å fikse motivasjonen innad teamet")
        #Konflikt#1: Silje og Elias (Ledd 2)
        if Valg=="1":
                print("Erling tar opp konflikten mellom Silje og Elias og prøver å finne en løsning, ")
                print("Hva bør erling gjøre sådan? ")
                print("1. Erling bestemmer seg for at han går til individuell samtale med Silje, og med Elias.")
                print("2. Erling samler hele gruppen for å sette felles kriterier, og deretter samler et team med de relaterte til løsningen for å utvikle noe som passer kriteriene. En hybridløsning")
                print("3. Erling velger å sette de sammen i et rom med Noa og Hallgeir for å forsøke å løse situasjonen ved å få innspill fra de som har mer kunnskap om hva Elias og Silje kritiserer hverandre for.")
                valg_konflikt1=(input("(1-3): "))
        #Siste ledd
                if valg_konflikt1=="1":
                        print("Konsekvens 1 De blir mer sinte på hverandre, forsterker egne meninger og blir mer rigide, og de føler seg truffet fordi de er problemet ")
                        poeng += 1
                        print(f"poeng: {poeng}")
                        konflikt1_ferdig = True
                elif valg_konflikt1=="2":
                        print("Konsekvens 2 Gruppen får en forståelse av hva som må gjøres for å utføre oppgaven, og kommer frem til en god hybridløsning som er et godt bidrag til hovedprosjektet. ")
                        poeng += 2
                        print(f"poeng: {poeng}")
                        konflikt1_ferdig = True
                elif valg_konflikt1=="3":
                        print("Konsekvens 3 De får begge innspill på forslagene de kommer med, blir opplyst faktorer de ikke har tenkt på før, \n "
                        "og begge forlater rommet med å ikke være helt fornøyde grunnet at de føler de ikke har blitt hørt for deres løsning, og må endre noe de var selvsikre og stolte av ")
                        poeng += 3
                        print(f"poeng: {poeng}")
                        konflikt1_ferdig = True
        #konflikt#2: Hamdi og Hallgeir (ledd 2)
        if Valg=="2":
                print("Erling tar opp konflikten mellom Hamdi og Hallgeir og prøver å finne en løsning, ")
                print("Hva bør erling gjøre sådan? ")
                print("1. Erling gir dem tydelig påminnelse, og de to møtes for å drøfte kompromissløsning.")
                print("2. Erling innkaller til møte der Erling deltar, for å komme frem til løsning")
                valg_konflikt2=(input("(1-2): "))

                if valg_konflikt2=="1":
                        print("Konsekvens 1 Hamdi og Hallgeir møtes på veiene av Erling sin beskjed, og etter en diskusjon som eskalerte til en krangel, kom de frem til at de måtte gi slipp på sine preferanser. \n "
                              "Til slutt, har de brukt for lang tid, så de har kommet opp med en løsning som tar hensyn til begge parter, men som fungerer svært dårlig.")
                        poeng += 2
                        print(f"poeng: {poeng}")
                        konflikt2_ferdig = True
                elif valg_konflikt2=="2":
                        print("Konsekvens 2 De prater om løsninger, og kommer frem til et felles produkt som er optimalt, i god tid +4")
                        poeng += 4
                        print(f"poeng: {poeng}")       #Motivasjon i teamet
                        konflikt2_ferdig = True
        if Valg=="3":
                print("Erling tar opp motivasjonen innad teamet og prøver å finne en løsning, ")
                print("Hva bør erling gjøre sådan? ")
                print("1. Erling gir rom for prat under prosjektsamarbeidet, tillater kaffepauser når som helst og skaper et avslappet miljø.")
                print("2. Erling motiverer med belønning, at om de får levert et bra produkt innen fristen får de dra ut å spise, og minner dem på at det er en belønning i slutten av prosjektet.")
                print("3. Erling tar initiativ til regelmessige felles aktiviteter, der det er frivillig å bli med, men der alle blir inkludert. Dette kan være å gå tur, bowle, eller å gå ut å spise.")
                valg_motivasjon=(input("(1-3): "))

                if valg_motivasjon=="1":
                        print("God stemning, men tempoet under arbeid er ikke raskt nok og rammene innad i teamet  sliter med å bli holdt. ")
                        poeng += 1
                        print(f"poeng: {poeng}")
                        konflikt3_ferdig = True
                elif valg_motivasjon=="2":
                        print("Teamet motiveres av belønning på starten av prosjektfasen, men blir fort vandt til tanken og ser ikke på belønningen som motivasjon lenger. ")
                        poeng += 2
                        print(f"poeng: {poeng}")
                        konflikt3_ferdig = True
                elif valg_motivasjon=="3":
                        print("Faste sammenkomster skaper gode relasjoner blant kollegaene, og gir glede og motivasjon til å jobbe sammen med de andre i gruppen grunnet styrkede relasjoner ")
                        poeng += 3
                        print(f"poeng: {poeng}")
                        konflikt3_ferdig = True        
                        if konflikt1_ferdig==True and konflikt2_ferdig==True and konflikt3_ferdig==True:
                                break
                              
