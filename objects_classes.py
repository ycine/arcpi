class telefon:

    dotykowe = 'tak'

    def nazwa(self, nazwa_telefonu):
        self.nazwa_telefonu = nazwa_telefonu
        print(self.nazwa_telefonu)


    def kolor(self, kolor):
        self.kolor = kolor
        print(self.kolor)

    def funkcje(self, dzwoni, sms, internet):
        self.dzwoni = dzwoni
        self.sms = sms
        self.internet = internet

        print(self.dzwoni)
        print(self.sms)
        print(self.internet)

    def wyswietl_wszystko(self):
        print("Oto telefon: " + self.nazwa_telefonu + ' ' + self.kolor + ' ' + self.dzwoni + ' ' + self.sms + ' ' + self.internet)

    @classmethod
    def typ(cls):
        return cls.dotykowe





telefon1 = telefon()
telefon1.nazwa('Xiaomi')
telefon1.kolor('biały')
telefon1.funkcje('tak', 'tak', 'nie')
telefon1.wyswietl_wszystko()
print(telefon.typ())

telefon2 = telefon()
telefon2.nazwa('Samsung')
telefon2.kolor('szary')
telefon2.funkcje('tak', 'tak', 'nie')
telefon2.wyswietl_wszystko()
