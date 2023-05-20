class Car:
    def __init__(self, airbag, ABS, kay, max_spid):
        self.airbag = airbag
        self.ABS = ABS
        self.kay = kay
        self.max_spid = max_spid

    def max_speed(self):
        print(self.airbag, self.ABS, self.kay, self.max_spid)


car_1 = Car("airbag", "ABS", "banali", 240)
car_1.max_speed()


class BMW(Car):
    def __init__(self, airbag, ABS, kay, drift, max_spid):
        super(BMW, self).__init__(airbag, ABS, kay, max_spid)
        self.drift = drift

    def Print(self):
        print("BMW", "\n", self.airbag, "\n", self.ABS, "\n", self.kay, "\n", self.drift, "\n", self.max_spid)


bmw_1 = BMW("airbag", "ABS", "kay", "drift", 330)
bmw_1.Print()


class Ferrari(Car):
    def __init__(self, airbag, ABS, kay, good_sound, max_spid):
        super(Ferrari, self).__init__(airbag, ABS, kay, max_spid)
        self.good_sound = good_sound

    def Print(self):
        print("\nFerrari", "\n", self.airbag, "\n", self.ABS, "\n", self.kay, "\n", self.good_sound, "\n", self.max_spid)


ferrari_1 = Ferrari("airbag", "ABS", "kay", "good_sound", 350)
ferrari_1.Print()