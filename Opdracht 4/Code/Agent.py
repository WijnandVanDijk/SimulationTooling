from mesa import Agent, Model
import random
from mesa.space import SingleGrid

class CarAgent(Agent):

    max_snelheid = 5

    # Elke auto begint met een random snelheid, van 0 T/M 5.
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.snelheid = random.randint(0, 5)
        self.pos = pos


    def optrekken(self):
        if self.snelheid < CarAgent.max_snelheid:
            self.snelheid += 1

        return self.snelheid

    def remmen(self):
        self.snelheid -= 1

        return self.snelheid

    def move(self):
        oude_positie = self.pos
        nieuwe_positie = (oude_positie[0] + self.snelheid, oude_positie[1])

        return nieuwe_positie # not sure if correct

    def role_of_randomization(self):
        if self.snelheid > 1:
            if random.randint(0,1) == 1:
                self.snelheid -= 1
            else:
                self.snelheid = self.snelheid

        return self.snelheid



class CarModel(Model):

    def __init__(self, height, width, car_amount):
        super().__init__()
        self.running = True
        self.height = height
        self.width = width
        self.car_amount = car_amount

        self.maak_agent()

        self.grid = SingleGrid(height, width, torus=True)

    def maak_agent(self):
        for i in range(self.car_amount):
            while True:
                try:
                    r = random.random()
                    agent = CarAgent((int(r*100), 5), self)
                    self.grid.position_agent(agent, int(r*100))
                    self.schedule.add(agent)
                    break
                except Exception as e:
                    continue

    def step(self):
        self.schedule.step()