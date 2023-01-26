class Gomba:
    def __init__(self, sor):
        alkalmas = sor.strip
        self.gombaFajta = alkalmas[0]
        self.gomba = alkalmas[1]
        self.evszak = alkalmas[2]

    def __str__(self):
        return f"{self.gombaFajta} {self.gomba} {self.evszak}"
