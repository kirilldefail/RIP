from pynput.keyboard import Key, KeyCode, Listener
import random
import time

from hero import Hero
from hero_builder import menu, HeroBuilder
from hero_states import HeroStateNothing, HeroStateMagic, HeroStateSword, HeroStateGun

class World:

    def __init__(self, builder: HeroBuilder) -> None:
#        self.ground = []
        self._builder = builder or HeroBuilder()
        self.story_of_the_world = []
        self.points = 0

    def on_press(self, key) -> str:
#    print('{0} pressed'.format(key))
        answer = ""
        if key == Key.alt:
            answer = self._builder._hero._state.change_state()
            self._builder._hero.story_of_hero.append(answer)
            print(answer)
        elif key == Key.ctrl:
            answer = self._builder._hero._state.fight()
            self._builder._hero.story_of_hero.append(answer)
            if self.points:
                self.points -= 1
            print(answer)
        elif key == Key.backspace:
            answer = self._builder._hero.go()
            self._builder._hero.story_of_hero.append(answer)
            print(answer)
        elif key == Key.space:
            menu(self._builder)
            answer = self._builder._hero.__str__()
            self._builder._hero.story_of_hero.append("Hero {} changes his gear".format(self._builder._hero.name))
            self.story_of_the_world.append("Hero {} changes his gear".format(self._builder._hero.name))
            self._builder._hero.story_of_hero.append(answer)
        elif key == KeyCode.from_char('q'):
            self.loop = False
            answer = "The hero {} came out of the adventure".format(self._builder._hero.name)
            self._builder._hero.story_of_hero.append(answer)
            print(answer)
        self.story_of_the_world.append(answer)
        return answer

    def game(self) -> str:
        self.story_of_the_world.append(self._builder._hero.__str__())
        self.loop = True
        with Listener(on_press=self.on_press) as listener:
            while(self.loop):
                monster = random.choices(["-------- > Monster detected! <--------\n", ""], weights=[1,3],k=1)
                print("".join(monster), end='')
                self.story_of_the_world.append("".join(monster))
                if not monster==[""]:
                    self.points = random.randint(5,10)
                    while(self.points and self.loop):
                        pass
                    if self.points == 0:
                        answer = []
                        answer.append('Hero {} won!'.format(self._builder._hero.name))
                        answer.append("---------------------------------------")
                        print("\n".join(answer))
                        self.story_of_the_world.append("\n".join(answer))
                time.sleep(random.randint(1, 4))
        return "\n".join(self.story_of_the_world)

def main():
    builder = HeroBuilder()
    builder = menu()
    world = World(builder)

    log = world.game()
    print('\n\n=================\n\n')
    print(log)

if __name__ == "__main__":
    main()
