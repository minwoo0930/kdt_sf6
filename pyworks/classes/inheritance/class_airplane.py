class Airplane:

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")



class SuperSonicAirplane(Airplane):
    NORMAL = 1
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirplane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            #print("비행기가 일반 비행합니다.")
            super().fly()


sa = SuperSonicAirplane()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC
sa.fly()

