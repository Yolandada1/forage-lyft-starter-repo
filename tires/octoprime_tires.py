from tires.tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def tire_should_be_serviced(tire_wear_array):
        if sum(tire_wear_array) >= 3:
            return True
        return False
