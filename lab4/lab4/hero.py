import time
# from pynput.keyboard import Key, KeyCode, Listener
from itertools import cycle

from abc import ABC, abstractmethod
import random

class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    def fight(self) -> str:
        pass

    def change_state(self) -> str:
        pass

class Hero():
    _state = State()

    def __init__(self, state = State(), name = "") -> None:
        self.name = name
        self.emblem = ""
        self.armor = ""
        self.helmet = ""
        self.magic = False
        self.sword = False
        self.gun = False

        self.story_of_hero = []

        self.states = []
        self.cycle = cycle(self.states)
        self.transition_to(state)

    def transition_to(self, state) -> str:
        answer = "Hero {} changes his weapon to a {}".format(self.name, state.weapon)
        self._state = state
        self._state.context = self
        return answer

    def go(self) -> str:
        return "Hero {} go...".format(self.name)

    def __str__(self) -> None:
        dict_parts = vars(self).copy()
        dict_parts.pop('name', None)
        dict_parts.pop('_state', None)
        dict_parts.pop('states', None)
        dict_parts.pop('cycle', None)
        dict_parts.pop('story_of_hero', None)
        list_parts = list(filter(
            lambda key: dict_parts.get(key), dict_parts.keys()))
        if not list_parts:
            return "Hero {} has nothing".format(self.name)
        names_of_parts = list(map(lambda key: "" if isinstance(dict_parts.get(key), bool) else dict_parts.get(key), list_parts))
        list_parts_with_names = list(map(lambda d: "{}{}".format(d[0], d[1]), list(zip(names_of_parts, list_parts))))
        return "Hero {} has {}".format(self.name, ', '.join(list_parts_with_names))

