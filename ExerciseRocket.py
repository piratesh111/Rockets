from random import randint
from math import sqrt


class Rocket:
    NextId = 1

    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed
        self.x = 0
        self.id = Rocket.NextId
        Rocket.NextId += 1

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "altitude rocket is:" + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.Rockets = [Rocket(randint(1, 4)) for _ in range(amountOfRockets)]
        for _ in range(10):
            RandomIndexToMove = randint(0, len(self.Rockets) - 1)
            self.Rockets[RandomIndexToMove].move_up()

        for rocket in self.Rockets:
            print(
                "rocket reached altitude:",
                rocket.altitude,
                "doing:",
                int(rocket.altitude / rocket.speed),
                "moves, by speed",
                rocket.speed,
            )

    def __getitem__(self, key):
        return self.Rockets[key]

    def __setitem__(self, key, value):
        self.Rockets[key].speed = value

    @staticmethod
    def get_distance(obj: Rocket, obj2: Rocket) -> float:
        ab = (obj.altitude - obj2.altitude) ** 2
        bc = (obj.x - obj.x) ** 2
        return sqrt(ab + bc)
