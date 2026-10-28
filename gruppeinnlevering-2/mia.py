poeng = 0 
print()
print()
print ("=== === Ta avgjørelser for Erling === ===")
print()
situasjon = "Erling må ta et valg for å løse konflikten mellom Silje og Elias."

alternativ1 = "Erling tar en individuell samtale med Silje og Elias, og forsøker å løse konflikten deres for dem."
alternativ2 = "Erling utvider konflikten fra bare Silje og Elias, til å samle hele teamet i håp om finne løsningen for å utvikle noe som passer kriteriene, en hybridløsning."
alternativ3 = "Erling kaller inn til et møte og inkluderer Noa og Hallgeir som relevante personer for å få innspill på løsningen. Etter felles møtet insierer han et møte med kun Silje og Elias der de kun snakker om deres relasjon, og tar avstand fra prosjektet"

konsekvens1 = "Under de individe samtalene blir rolleforskjellen mellom Silje og Erling og Elias og Erling tydeligjort, de tolker privatmøtet med Erling som en konfrontasjon og låser seg mer i egne meninger."
konsekvens2 = "De får innspill og ny kunnskap til løsning, men Silje og Elias forlater rommet uten å være helt fornøyde, fordi de ikke føler seg hørt. Relasjonen blir ikke reparert, men ender opp som nøytral etter lang tid."
konsekvens3 = "Silje og Elias syntes det er ukomfertabelt å ta opp konflikten, imens produseres det et godt produkt basert på innspillene til teamet. Silje og Elias prater etter møtet, der de får problemstillingen på avstand. De klarer å løse opp i krangelen deres."

print(situasjon)
print()
print("1: " + alternativ1)
print()
print("2: " + alternativ2)
print()
print("3: " + alternativ3)
print()
print()
valg1 = input("Hva skal Erling velge? (1, 2 eller 3)")
print()

if valg1 == "1":
    print("KONSEKVENSEN AV VALGET:",konsekvens1)
    print()
    poeng = poeng + 1
elif valg1 == "2":
    print("KONSEKVENSEN AV VALGET:",konsekvens2)
    print()
    poeng = poeng + 2
elif valg1 == "3":
    print("KONSEKVENSEN AV VALGET:", konsekvens3)
    print()
    poeng = poeng + 3
else:
    print()
    print("Ugyldig valg, sendes tilbake til start")
    print(situasjon)



print("=== === Situasjon 2 === ===")
print()
situasjon = "Erling må ta et valg før Hamdi og Hallgeir sin konflikt eskalerer."
print()
alternativ1 = "Erling gir dem en tydelig påminnelse av tidsfristen og ønsker at de to skal ta et møte så fort så mulig for å drøfte en kompromissløsning"
alternativ2 = "Erling tilkaller til møte med Hamdi og Hallgeir, og setter av god tid til å drøfte løsninger og positive og negativer sider med oppgaven. De prater om løsninger."
konsekvens1 = "Hamdi og Hallgeir møtes på veiene av Erling sin beskjed, og etter en diskusjon som eskalrete til en krangel, kom de frem til at de måtte gi slipp på sine preferanser. Til slutt, har de brukt for lang tid, så de har kommet opp med en løsning som tar hensyn til begge parter, men som fungerer svært dårlig. +2 "
konsekvens2 = "De prater om løsninger sammen med Erling som tar rollen som mekler, og kommer frem til et felles produkt som er godt nok, i god tid +4"

print(situasjon)
print()
print()
print("1: " + alternativ1)
print()
print("2: " + alternativ2)
print()
print()
valg1 = input("Hva skal Erling velge? (1 eller 2)")

if valg1 == "1":
    print(konsekvens1)
    print()
    poeng = poeng + 2
elif valg1 == "2":
    print(konsekvens2)
    print()
    poeng = poeng + 4
else:
    print("Ugyldig valg, skriv 1 eller 2")
    print()

print("=== === Motivasjon i teamet === ===")
print()
print()
situasjon="Erling må finne en måte å bevare motivasjon i teamet"
alternativ1="Erling gir rom for prat under prosjektsamarbeidet, tilater kaffepauser når som helst og skaper et avslappet miljø"
alternativ2="Erling motiverer med belønning, a tom de får levert et bra produkt innen fristen får de dra ut å spise, og minner dem på at det er en belønning i slutten av prosjektet."
alternativ3="Erling tar initiativ til regelmessige felles aktiviteter, der det er frivillig å bli med, men der alle blir inkludert. Dette kan være å. gå tur og å gå ut å spise. "


konsekvens1="Fristene underveis i prosjektet blir holdt, men tempoet er ikke raskt nok og rammene innad i teamet blir ikke holdt. +1"
konsekvens2="Teamet motiveres av belønning på starten av prosjektfasen, men blir fort vandt til tanken og ser ikke på belønningen som motivasjon lenger.+2"
konsekvens3="Faste sammenkomster skaper gode relasjoner blant kollegaene, og gir glede og motivasjon til å jobbe sammen med de andre i gruppen grunnet styrkede relasjoner +3"


print("1: " + alternativ1)
print()
print("2: " + alternativ2)
print()
print("3: " + alternativ3)
print()
valg1 = input("Hva skal Erling velge? (1, 2 eller 3)")

if valg1 == "1":
    print(konsekvens1)
    poeng = poeng + 1
    print()
elif valg1 == "2":
    print(konsekvens2)
    poeng = poeng + 2
    print()
elif valg1 == "3":
    print(konsekvens3)
    poeng = poeng + 3
    print()
else:
    print("Ugyldig valg, skriv 1, 2 eller 3")

print("=== === === !! KONSEKVENSENE AV DINE VALG !! === === ===")
print()
print()
print("Din totale poengsum =", poeng)
print()
if poeng <= 5:
    print("Utfall 3: Ikke godkjent. Konfliktene resulterer i et gruppeprosjekt som ikke lykkes, gruppen brytes opp og relasjonene i gruppen er ødelagte.")
elif poeng <= 8:
    print("Utfall 2: Godkjent, men fristen måtte utsettes og relasjonene i gruppen er anspente.")
else:
    print("Utfall 1: Bra!-ø Teamet går inn i norming-fasen.")
print()
print()



