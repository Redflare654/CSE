class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("you turn the key an the engine starts")

    def move_forward(self):
        self.fuel -= 1
        print("you move forward")

    def turn_left(self):
        self.fuel -=1
        print("HE'S MAKING A LEFT TURN")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


bethany_car = Viper()
bethany_car.start_engine()
bethany_car.move_forward()
bethany_car.turn_left()
bethany_car.move_forward()
bethany_car.turn_off()
