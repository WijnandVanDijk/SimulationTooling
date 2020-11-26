class CoffeeMachine:

    running = False

    def __init__(self, water, melk, bonen, cacao, bekers, geld, saldo):
        self.water = water
        self.melk = melk
        self.bonen = bonen
        self.cacao = cacao
        self.bekers = bekers
        self.geld = geld
        self.saldo = saldo

        # als de machine uit is gaat het aan
        if not CoffeeMachine.running:
            self.start()

    def start(self):
        self.running = True
        self.actie = input("Wat wilt u doen (kopen, vullen (admin), geld opnemen (admin), overzicht (admin), exit (admin)):\n")
        print()
        # Mogelijkheden die het koffie apparaat kan uitvoeren
        if self.actie == "kopen":
            self.kopen()
        elif self.actie == "vullen":
            self.vullen()
        elif self.actie == "geld opnemen":
            self.opnemen()
        elif self.actie == "exit":
            exit()
        elif self.actie == "overzicht":
            self.overzicht()

    def terug_hoofdmenu(self): # gaat terug naar het main menu
        print()
        self.start()

    def keuze_bevestigen(self):
        print('Weet u zeker dat u dat wilt bestellen?')
        zeker = input('0 is ja, 1 is nee ')
        if zeker == '1':
            self.kopen()


    def beschikbaar_check(self): # kijkt of er genoeg materialen zijn om het te maken.
        self.not_available = "" # door checken of de waarde niet onder de 0 gaat.
        if self.water - self.verminder[0] < 0:
            self.not_available = "water"
        elif self.melk - self.verminder[1] < 0:
            self.not_available = "melk"
        elif self.bonen - self.verminder[2] < 0:
            self.not_available = "bonen"
        elif self.cacao - self.verminder[3] < 0:
            self.not_available = "cacao"
        elif self.bekers - self.verminder[4] < 0:
            self.not_available = "bekers"
        elif self.saldo - self.verminder[6] < 0:
            self.not_available = "saldo"

        if self.not_available != "": # als iets onder de 0 is na verminderen
            print(f"Sorry, niet genoeg {self.not_available}!")
            return False
        else: # als er van alles genoeg is.
            print("Ik heb genoeg ingredienten, het komt eraan!")
            return True

    def verminder_supplies(self): # verminderd de supplies die bij de gekozen drank horen.
        self.water -= self.verminder[0]
        self.melk -= self.verminder[1]
        self.bonen -= self.verminder[2]
        self.cacao -= self.verminder[3]
        self.bekers -= self.verminder[4]
        self.geld += self.verminder[5]

    def verminder_saldo(self):
        self.saldo -= self.verminder[6]

    def kopen(self):
        self.keuze = input("Wat wilt u kopen? 1 - espresso $4, 2 - latte $7, 3 - cappuccino $6, 4 - chocolademelk $3, terug - naar hoofdmenu:\n")
        if self.keuze == '1':
            self.verminder = [250, 0, 16, 0, 1, 4, 4] # water, milk, coffee beans, cacao, cups, money, met hoeveel saldo down gaat
            self.keuze_bevestigen()
            if self.beschikbaar_check():
                self.verminder_supplies()
                self.verminder_saldo()

        elif self.keuze == '2':
            self.verminder = [350, 75, 20, 0, 1, 7, 7]
            self.keuze_bevestigen()
            if self.beschikbaar_check():
                self.verminder_supplies()
                self.verminder_saldo()

        elif self.keuze == "3":
            self.verminder = [200, 100, 12, 0, 1, 6, 6]
            self.keuze_bevestigen()
            if self.beschikbaar_check():
                self.verminder_supplies()
                self.verminder_saldo()

        elif self.keuze == "4":
            self.verminder = [200, 100, 0, 25, 1, 3, 3]
            self.keuze_bevestigen()
            if self.beschikbaar_check():
                self.verminder_supplies()
                self.verminder_saldo()

        elif self.keuze == "terug": # als de gebruikers toch iets anders wil
            self.terug_hoofdmenu()

        self.terug_hoofdmenu()

    def vullen(self): # toevoegen van grondstoffen aan de koffiemachine
        self.water += int(input("Hoeveel ml aan water wilt u toevoegen:\n"))
        self.melk += int(input("Hoeveel ml aan melk wilt u toevoegen:\n"))
        self.bonen += int(input("Hoeveel gram bonen wilt u toevoegen:\n"))
        self.cacao += int(input("hoeveel gram cacao wilt u toevoegen:\n"))
        self.bekers += int(input("Hoeveel bekers wilt u toevoegen:\n"))
        self.terug_hoofdmenu()

    def opnemen(self): # geld opnemen van de machine
        print(f"U krijgt ${self.geld}")
        self.geld -= self.geld
        self.terug_hoofdmenu()

    def overzicht(self):  # weergeeft de hoeveelheid grondstoffen die aanwezig zijn
        print(f"Deze koffiemachine bevat:")
        print(f"{self.water} ml water")
        print(f"{self.melk} ml melk")
        print(f"{self.bonen} gr bonen")
        print(f"{self.cacao} gr cacao")
        print(f"{self.bekers} bekers")
        print(f"${self.geld} omzet")
        print(f"${self.saldo} saldo")
        self.terug_hoofdmenu()

pinpas = input('Hoeveel geld staat er op uw pinpas?')
if pinpas < '0':
    pinpas = pinpas == 0
CoffeeMachine(400, 540, 120, 110, 9, 550, float(pinpas)) # begin waardes voor ingredienten
            # water, melk, bonen, cacao, bekers, geld