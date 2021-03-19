"""Survival
1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
Each animal is born with the following parameters (by using random):
- strength (from 25 to 100 points)
- speed (from 25 to 100 points)
The force cannot be greater than it was at birth (initialization).

At each step of the game we take 1 animal from the forest (iteration):
- If it is herbivorous, then it eats (restores its strength by 50%).
- If it is a predator, it hunts - randomly chooses an animal from the forest and:
    - pulled himself out, he was unlucky and he was left without a dinner;
    - pulled out another animal, then tries to catch up;
    - if he can catch up, he catches up and attacks;
    - if attacked and is stronger, then eats and restores 50% of strength;
    - did not catch up or did not have enough strength, then he and the lucky prey lose 30% of strength (Because both either ran, or fought, or all together)

An animal whose power has expired dies. (You can check the strength at the time of food search)

The game continues as long as predators are present in the forest."""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from random import choice, randint
from uuid import uuid4
from math import ceil


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):

    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def eat(self, forest: Forest):
        booty = choice(list(forest.animals.values()))  # Choosing  booty
        if booty.id == self.id:
            print(f'This forest is empty')
        else:
            if (self.speed > booty.speed) and (self.current_power > booty.current_power):
                print('Predator eats')
                current = self.current_power
                self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
                print(f'Predator restored {ceil(self.current_power - current)} power')
            else:
                print('Predator did not caught target, both are tired')
                self.current_power = self.current_power - 0.3 * self.max_power
                forest.animals[booty.id].current_power = forest.animals[booty.id].current_power - 0.3 * \
                                                          forest.animals[booty.id].max_power


class Herbivorous(Animal):

    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def eat(self, forest: Forest):
        """
        Herbivorous eats and restores its power by 50%
        """
        print('Herbivorous eats')
        current = self.current_power
        self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
        print(f'Herbivorous restored {ceil(self.current_power - current)} power')


AnyAnimal = [Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print(f'A new {animal} has appeared in the forest')
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f'{animal} - no in our forest')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    """
    With the help of libraries generated power, speed and id
    """
    while True:
        generator_animal = choice((Predator(randint(25, 100), randint(25, 100)),
                                   Herbivorous(randint(25, 100), randint(25, 100))))

        generator_animal.id = uuid4()
        yield generator_animal


"""if __name__ == ""__main__"":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass

Tips:
When a predator hunts, an animal is accidentally taken from the forest.
This animal may be the predator itself. To check this and distinguish two animals with the same characteristics,
use the uuid library. But when creating an animal, assign its id a unique value.

You can use the random library to work with random numbers

If you do not know how to create a forest and look at the survival process,
here is an example of code that can be used for debugging
"""

if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        from time import sleep
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_power < 1:
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('There are no predators in the forest')
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        sleep(1)
