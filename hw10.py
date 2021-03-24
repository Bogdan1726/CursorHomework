from time import sleep


class BatteryDischarging(Exception):
    pass


class BatteryEmpty(Exception):
    pass


class NoWater(Exception):
    pass


class Container(Exception):
    pass


class RobotVacuumCleaner:
    battery_discharge = 5
    water_consumption = 10
    filling_the_container = 10

    def __init__(self):
        self.battery_charge = 100
        self.garbage_container = 0
        self.amount_of_water = 100

    def move(self):
        print('Loading...')
        while True:
            sleep(1)
            try:
                print(f'Robot vacuum cleaner moves \n'
                      f'battery charge - {self.battery_charge} % \n')
                self.battery_charge -= self.battery_discharge
                if self.battery_charge <= 20:
                    if self.battery_charge == 0:
                        raise BatteryEmpty
                    raise BatteryDischarging
            except BatteryDischarging:
                print(f'Warning! The battery is discharging - {self.battery_charge} % \n')
            except BatteryEmpty:
                print(f'The battery is discharged!')
                break

            try:
                print('Robot vacuum cleaner working')
                self.vacuum_cleaner()
                if self.garbage_container == 100:
                    raise Container
            except Container:
                print('Garbage container is full')
                input('Нажмите Enter чтобы очистить контейнер... ')
                print()
                self.garbage_container = 0

            try:
                if self.amount_of_water > 0:
                    print('Robot vacuum cleaner washes')
                    self.wash()
                else:
                    raise NoWater
            except NoWater:
                print('Warning! Run out of water \n')

    def wash(self):
        self.amount_of_water -= self.water_consumption
        print(f'water level - {self.amount_of_water} % \n')

    def vacuum_cleaner(self):
        self.garbage_container += self.filling_the_container
        print(f'Trash level in container - {self.garbage_container} % \n')


robot = RobotVacuumCleaner()
robot.move()
