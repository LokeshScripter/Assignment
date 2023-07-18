class Vechile:

    def __init__(self, seating):
        self.seating = seating

    def fare_charge(self):
        return self.seating * 100


class Bus(Vechile):

    def __init__(self, seating=50):
        super().__init__(seating)

    def fare_charge(self):
        seat = self.seating * 100
        return seat + seat * 0.1


car = Vechile(10)
car2 = Bus()
print(car2.fare_charge())