from behave import *

from hero_builder import HeroBuilder
from hero_states import HeroStateNothing, HeroStateMagic, HeroStateSword, HeroStateGun
from hero import Hero, State

@given('Create hero')
def step(context):
    context.builder = HeroBuilder()
    context.builder.set_name('L')

@when('The hero received a magic, sword and gun')
def step(context):
    context.builder.add_magic()
    context.builder.add_sword()
    context.builder.add_gun()

@then('The states will change')
def step(context):
    result = context.builder._hero._state.fight()
    assert 'Hero L shoots a gun' in result
    context.builder._hero._state.change_state()
    result = context.builder._hero._state.fight()
    assert 'Hero L hits the monster with his fists' in result
    context.builder._hero._state.change_state()
    result = context.builder._hero._state.fight()
    assert 'Hero L uses magic' in result
    context.builder._hero._state.change_state()
    result = context.builder._hero._state.fight()
    assert 'Hero L hits the monster with a sword' in result
