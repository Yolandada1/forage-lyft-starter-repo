from tires.tire import Tire


class CarriganTires(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def tire_should_be_serviced(tire_wear_array):
        if any(wear >= 0.9 for wear in tire_wear_array):
            return True
        return False
