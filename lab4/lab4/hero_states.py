# оружие меняется по Tab
from abc import ABC, abstractmethod
from hero import Hero, State
import random

class HeroStateNothing(State):
    weapon = "nothing"
    def fight(self) -> str:
        return "Hero {} hits the monster with his fists".format(self.context.name)

    def change_state(self):
        results = []
        results.append(self.context.transition_to( next(self.context.cycle) ))
        return "\n".join(results)

class HeroStateMagic(State):
    weapon = "magic"
    def fight(self) -> str:
        return "Hero {} uses magic".format(self.context.name)

    def change_state(self):
        results = []
        results.append(self.context.transition_to( next(self.context.cycle) ))
        return "\n".join(results)


class HeroStateSword(State):
    weapon = "sword"

    def fight(self) -> str:
        return "Hero {} hits the monster with a sword".format(self.context.name)

    def change_state(self):
        results = []
        results.append(self.context.transition_to( next(self.context.cycle) ))
        return "\n".join(results)

class HeroStateGun(State):
    weapon = "gun"

    def fight(self) -> str:
        return "Hero {} shoots a gun".format(self.context.name)

    def change_state(self):
        results = []
        results.append(self.context.transition_to( next(self.context.cycle)))
        return "\n".join(results)
