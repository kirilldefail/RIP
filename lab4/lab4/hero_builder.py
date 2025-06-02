from hero import Hero
from hero_states import HeroStateNothing, HeroStateMagic, HeroStateSword, HeroStateGun
from itertools import cycle, chain

class HeroBuilder():
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._hero = Hero(HeroStateNothing())
        self._hero.states.append(HeroStateNothing())

    @property
    def hero(self) -> Hero:
        hero = self._hero
#        self.reset()
        return hero

    def set_name(self, name) -> None:
        self._hero.name = name

    def add_emblem(self, emblem) -> None:
        self._hero.emblem = emblem+" "

    def add_armor(self, armor) -> None:
        self._hero.armor = armor+" "

    def add_helmet(self, helmet) -> None:
        self._hero.helmet = helmet+" "

    def add_magic(self) -> None:
        self._hero.magic = True
        self._hero.states.append(HeroStateMagic())
        self._hero.cycle = cycle(self._hero.states)
        self._hero.transition_to(HeroStateMagic())

    def add_sword(self) -> None:
        self._hero.sword = True
        self._hero.states.append(HeroStateSword())
        self._hero.cycle = cycle(self._hero.states)
        self._hero.transition_to(HeroStateSword())

    def add_gun(self) -> None:
        self._hero.gun = True
        self._hero.states.append(HeroStateGun())
        self._hero.cycle = cycle(self._hero.states)
        self._hero.transition_to(HeroStateGun())

def menu(builder = None):
    if builder == None:
        builder = HeroBuilder()
    loop = True
    while loop == True:
        print('===================================================')
        print('                CHOOSE YOUR GEAR                   ')
        print('===================================================')
        print(' 1 - Name' )
        print(' 2 - Emblem')
        print(' 3 - Armor')
        print(' 4 - Helmet')
        print(' 5 - Magic')
        print(' 6 - Sword')
        print(' 7 - Gun')
        print(' 0 - Exit')
        print('===================================================')
        response = input('Enter a selection -> ')

        if response == '1':
            name = input('Enter your name: ')
            builder.set_name(name)
        elif response == '2':
            emblem = input('Enter your emblem: ')
            builder.add_emblem(emblem)
        elif response == '3':
            armor = input('Enter your armor: ')
            builder.add_armor(armor)
        elif response == '4':
            helmet = input('Enter your helmet: ')
            builder.add_helmet(helmet)
        elif response == '5':
            builder.add_magic()
        elif response == '6':
            builder.add_sword()
        elif response == '7':
            builder.add_gun()
        elif response == '0':
            answer = builder._hero
            print(answer)
            print ('The choice is made')
            print("---------------------------------------------------")
            loop = False
        else:
            print ('Unrecognized command. Try again.')
    return builder
