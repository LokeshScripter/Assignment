class Vechile:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

    def maxspeed(self):
        print(f"the maxspeed of vechile is{self.maxspeed}")


    def mileage(self):
        print(f"the mileage is{self.mileage}")


class Bus(Vechile):
    pass

k = Bus(200,15)

print(k.mileage)