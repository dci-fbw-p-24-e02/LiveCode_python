from bike import Bike
from public_transport import PublicTransport


class BikeTaxi(Bike, PublicTransport):
    def __init__(self, motorized: bool):
        if motorized:
            self.__passenger_load = 4
            speed = 30
        else:
            self.__passenger_load = 2
            speed = 18
        super().__init__(speed=speed, motorized=motorized)

    def enter_passengers(self, num: int):
        if self.get_current_passengers() + num > self.__passenger_load:
            print("Cannot load more passengers at this time.")
            return
        super().enter_passengers(num)
