import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_team_builder.settings')

import django

django.setup()

from builder.models import Pokemon, Move, Nature, Ability, Item


def pokemon_add_data(pokedex, name, hp, attack, defence, sp_atk, sp_def, speed, type1, type2, gigantamax_factor):
    d, created = Pokemon.objects.get_or_create(pokedex=pokedex, name=name, hp=hp,
                                               attack=attack, defence=defence, sp_atk=sp_atk,
                                               sp_def=sp_def, speed=speed, type1=type1, type2=type2,
                                               gigantamax_factor=gigantamax_factor)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d

def move_add_data(name, type):
    d, created = Move.objects.get_or_create(name=name, type=type)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d

def nature_add_data(name, upstat, downstat):
    d, created = Nature.objects.get_or_create(name=name, upstat=upstat, downstat=downstat)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d

def ability_add_data(name):
    d, created = Ability.objects.get_or_create(name=name)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d

def item_add_data(name):
    d, created = Item.objects.get_or_create(name=name)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def populate():
    pokemon_data=[[6, "Charizard", 78, 84, 78, 100, 109, 85, "Fire", "Flying", 2],
          [3, "Venusaur", 80, 82, 83, 80, 100, 100, "Grass", "Poison", 2],
          [800, "Necrozma", 97, 107, 101, 79, 127, 89, "psychic", None, 1],
          [888, "Zacian", 92, 130, 115, 138, 80, 115, "fairy", None, 1]
    ]
    move_data=[["Flare Blitz", "fire"], ["Crunch", "dark"], ["Extreme Speed", "normal"], ["Roost", "flying"]]
    nature_data=[["Jolly", "speed", "sp_atk"], ["Modest", "sp_atk", "attack"], ["Relaxed", "defence", "speed"]]
    ability_data=[["Speed Boost"]]
    item_data = [["Focus Sash"]]
    # data is a list of lists
    for row in pokemon_data:
        pokedex = row[0]
        name = row[1]
        hp = row[2]
        attack = row[3]
        defence = row[4]
        sp_atk = row[5]
        sp_def = row[6]
        speed = row[7]
        type1 = row[8]
        type2 = row[9]
        gigantamax_factor = row[10]
        pokemon_add_data(pokedex, name, hp, attack, defence, sp_atk, sp_def,
                 speed, type1, type2, gigantamax_factor)

    for row in move_data:
        name = row[0]
        type = row[1]
        move_add_data(name, type)

    for row in nature_data:
        nature = row[0]
        upstat = row[1]
        downstat = row[2]
        nature_add_data(nature, upstat, downstat)

    for row in ability_data:
        name = row[0]
        ability_add_data(name)

    for row in item_data:
        name = row[0]
        item_add_data(name)


if __name__ == "__main__":
    populate()
