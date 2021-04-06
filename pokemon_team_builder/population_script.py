import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_team_builder.settings')
working_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

import django

django.setup()

from builder.models import Pokemon, Move, Nature, Ability, Item, UserProfile, Team


def user_add_data(user):
    d, created = UserProfile.objects.get_or_create(user=user)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def Team_add_data(userprofile, teamname, likes,
                  pokedex1, name1, ability1, nature1, item1,
                  move1_1, move2_1, move3_1, move4_1, level1, hp1, atk1, def1, sp_atk1,
                  sp_def1, spd1, hpEV1, atkEV1, defEV1, sp_atkEV1, sp_defEV1, spdEV1,
                  hpIV1, atkIV1, defIV1, sp_atkIV1, sp_defIV1, spdIV1, gmax1,
                  movetype1_1, movetype2_1, movetype3_1, movetype4_1, type1_1, type2_1,
pokedex2, name2, ability2, nature2, item2,
                  move1_2, move2_2, move3_2, move4_2, level2, hp2, atk2, def2, sp_atk2,
                  sp_def2, spd2, hpEV2, atkEV2, defEV2, sp_atkEV2, sp_defEV2, spdEV2,
                  hpIV2, atkIV2, defIV2, sp_atkIV2, sp_defIV2, spdIV2, gmax2,
                  movetype1_2, movetype2_2, movetype3_2, movetype4_2, type1_2, type2_2,
pokedex3, name3, ability3, nature3, item3,
                  move1_3, move2_3, move3_3, move4_3, level3, hp3, atk3, def3, sp_atk3,
                  sp_def3, spd3, hpEV3, atkEV3, defEV3, sp_atkEV3, sp_defEV3, spdEV3,
                  hpIV3, atkIV3, defIV3, sp_atkIV3, sp_defIV3, spdIV3, gmax3,
                  movetype1_3, movetype2_3, movetype3_3, movetype4_3, type1_3, type2_3,
pokedex4, name4, ability4, nature4, item4,
                  move1_4, move2_4, move3_4, move4_4, level4, hp4, atk4, def4, sp_atk4,
                  sp_def4, spd4, hpEV4, atkEV4, defEV4, sp_atkEV4, sp_defEV4, spdEV4,
                  hpIV4, atkIV4, defIV4, sp_atkIV4, sp_defIV4, spdIV4, gmax4,
                  movetype1_4, movetype2_4, movetype3_4, movetype4_4, type1_4, type2_4,
pokedex5, name5, ability5, nature5, item5,
                  move1_5, move2_5, move3_5, move4_5, level5, hp5, atk5, def5, sp_atk5,
                  sp_def5, spd5, hpEV5, atkEV5, defEV5, sp_atkEV5, sp_defEV5, spdEV5,
                  hpIV5, atkIV5, defIV5, sp_atkIV5, sp_defIV5, spdIV5, gmax5,
                  movetype1_5, movetype2_5, movetype3_5, movetype4_5, type1_5, type2_5,
pokedex6, name6, ability6, nature6, item6,
                  move1_6, move2_6, move3_6, move4_6, level6, hp6, atk6, def6, sp_atk6,
                  sp_def6, spd6, hpEV6, atkEV6, defEV6, sp_atkEV6, sp_defEV6, spdEV6,
                  hpIV6, atkIV6, defIV6, sp_atkIV6, sp_defIV6, spdIV6, gmax6,
                  movetype1_6, movetype2_6, movetype3_6, movetype4_6, type1_6, type2_6
                  ):
    d, created = Team.objects.get_or_create(userprofile=userprofile,
                                            teamname=teamname,
                                            likes=likes,
                                            pokedex1=pokedex1,
                                            name1=name1,
                                            ability1=ability1,
                                            nature1=nature1,
                                            item1=item1,
                                            move1_1=move1_1,
                                            move2_1=move2_1,
                                            move3_1=move3_1,
                                            move4_1=move4_1,
                                            movetype1_1=movetype1_1,
                                            movetype2_1=movetype2_1,
                                            movetype3_1=movetype3_1,
                                            movetype4_1=movetype4_1,
                                            level1=level1,
                                            hp1=hp1,
                                            atk1=atk1,
                                            def1=def1,
                                            sp_atk1=sp_atk1,
                                            sp_def1=sp_def1,
                                            spd1=spd1,
                                            hpEV1=hpEV1,
                                            atkEV1=atkEV1,
                                            defEV1=defEV1,
                                            sp_atkEV1=sp_atkEV1,
                                            sp_defEV1=sp_defEV1,
                                            spdEV1=spdEV1,
                                            hpIV1=hpIV1,
                                            atkIV1=atkIV1,
                                            defIV1=defIV1,
                                            sp_atkIV1=sp_atkIV1,
                                            sp_defIV1=sp_defIV1,
                                            spdIV1=spdIV1,
                                            gmax1=gmax1,
                                            type1_1=type1_1,
                                            type2_1=type2_1,
                                            pokedex2=pokedex2, name2=name2, ability2=ability2, nature2=nature2, item2=item2,
                                            move1_2=move1_2, move2_2=move2_2, move3_2=move3_2, move4_2=move4_2, level2=level2, hp2=hp2, atk2=atk2, def2=def2, sp_atk2=sp_atk2,
                                            sp_def2=sp_def2, spd2=spd2, hpEV2=hpEV2, atkEV2=atkEV2, defEV2=defEV2, sp_atkEV2=sp_atkEV2, sp_defEV2=sp_defEV2, spdEV2=spdEV2,
                                            hpIV2=hpIV2, atkIV2=atkIV2, defIV2=defIV2, sp_atkIV2=sp_atkIV2, sp_defIV2=sp_defIV2, spdIV2=spdIV2, gmax2=gmax2,
                                            movetype1_2=movetype1_2, movetype2_2=movetype2_2, movetype3_2=movetype3_2, movetype4_2=movetype4_2, type1_2=type1_2, type2_2=type2_2,
                                            pokedex3=pokedex3, name3=name3, ability3=ability3, nature3=nature3, item3=item3,
                                            move1_3=move1_3, move2_3=move2_3, move3_3=move3_3, move4_3=move4_3, level3=level3, hp3=hp3, atk3=atk3, def3=def3, sp_atk3=sp_atk3,
                                            sp_def3=sp_def3, spd3=spd3, hpEV3=hpEV3, atkEV3=atkEV3, defEV3=defEV3, sp_atkEV3=sp_atkEV3, sp_defEV3=sp_defEV3, spdEV3=spdEV3,
                                            hpIV3=hpIV3, atkIV3=atkIV3, defIV3=defIV3, sp_atkIV3=sp_atkIV3, sp_defIV3=sp_defIV3, spdIV3=spdIV3, gmax3=gmax3,
                                            movetype1_3=movetype1_3, movetype2_3=movetype2_3, movetype3_3=movetype3_3, movetype4_3=movetype4_3, type1_3=type1_3, type2_3=type2_3,
                                            pokedex4=pokedex4, name4=name4, ability4=ability4, nature4=nature4, item4=item4,
                                            move1_4=move1_4, move2_4=move2_4, move3_4=move3_4, move4_4=move4_4, level4=level4, hp4=hp4, atk4=atk4, def4=def4, sp_atk4=sp_atk4,
                                            sp_def4=sp_def4, spd4=spd4, hpEV4=hpEV4, atkEV4=atkEV4, defEV4=defEV4, sp_atkEV4=sp_atkEV4, sp_defEV4=sp_defEV4, spdEV4=spdEV4,
                                            hpIV4=hpIV4, atkIV4=atkIV4, defIV4=defIV4, sp_atkIV4=sp_atkIV4, sp_defIV4=sp_defIV4, spdIV4=spdIV4, gmax4=gmax4,
                                            movetype1_4=movetype1_4, movetype2_4=movetype2_4, movetype3_4=movetype3_4, movetype4_4=movetype4_4, type1_4=type1_4, type2_4=type2_4,
                                            pokedex5=pokedex5, name5=name5, ability5=ability5, nature5=nature5, item5=item5,
                                            move1_5=move1_5, move2_5=move2_5, move3_5=move3_5, move4_5=move4_5, level5=level5, hp5=hp5, atk5=atk5, def5=def5, sp_atk5=sp_atk5,
                                            sp_def5=sp_def5, spd5=spd5, hpEV5=hpEV5, atkEV5=atkEV5, defEV5=defEV5, sp_atkEV5=sp_atkEV5, sp_defEV5=sp_defEV5, spdEV5=spdEV5,
                                            hpIV5=hpIV5, atkIV5=atkIV5, defIV5=defIV5, sp_atkIV5=sp_atkIV5, sp_defIV5=sp_defIV5, spdIV5=spdIV5, gmax5=gmax5,
                                            movetype1_5=movetype1_5, movetype2_5=movetype2_5, movetype3_5=movetype3_5, movetype4_5=movetype4_5, type1_5=type1_5, type2_5=type2_5,
                                            pokedex6=pokedex6, name6=name6, ability6=ability6, nature6=nature6, item6=item6,
                                            move1_6=move1_6, move2_6=move2_6, move3_6=move3_6, move4_6=move4_6, level6=level6, hp6=hp6, atk6=atk6, def6=def6, sp_atk6=sp_atk6,
                                            sp_def6=sp_def6, spd6=spd6, hpEV6=hpEV6, atkEV6=atkEV6, defEV6=defEV6, sp_atkEV6=sp_atkEV6, sp_defEV6=sp_defEV6, spdEV6=spdEV6,
                                            hpIV6=hpIV6, atkIV6=atkIV6, defIV6=defIV6, sp_atkIV6=sp_atkIV6, sp_defIV6=sp_defIV6, spdIV6=spdIV6, gmax6=gmax6,
                                            movetype1_6=movetype1_6, movetype2_6=movetype2_6, movetype3_6=movetype3_6, movetype4_6=movetype4_6, type1_6=type1_6, type2_6=type2_6
                                            )
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


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
    f = open(os.path.join(working_dir, 'pokemon.txt'), "r")
    pokemon = []
    types = []
    abilities = []
    basestats = []
    name = ""
    pokedex = 0
    gmax = 0

    for x in f:
        if x.startswith("["):
            pokedex = int(x[1:-2])
        if x.startswith("Name"):
            name = x[7:].strip()
            if name == "Snorlax":
                gmax = 2
            elif name == "Charizard":
                gmax = 2
            elif name == "Pikachu":
                gmax = 2
            elif name == "Eevee":
                gmax = 2
            elif name == "Butterfree":
                gmax = 2
            elif name == "Meowth":
                gmax = 2
            elif name == "Corviknight":
                gmax = 2
            elif name == "Alcremie":
                gmax = 2
            elif name == "Drednaw":
                gmax = 2
            elif name == "Machamp":
                gmax = 2
            elif name == "Gengar":
                gmax = 2
            elif name == "Toxtricity":
                gmax = 2
            elif name == "Melmetal":
                gmax = 2
            elif name == "Coalossal":
                gmax = 2
            elif name == "Sandaconda":
                gmax = 2
            elif name == "Centiskorch":
                gmax = 2
            elif name == "Grimmsnarl":
                gmax = 2
            elif name == "Hatterene":
                gmax = 2
            elif name == "Copperajah":
                gmax = 2
            elif name == "Duraludon":
                gmax = 2
            elif name == "Flapple":
                gmax = 2
            elif name == "Appletun":
                gmax = 2
            elif name == "Orbeetle":
                gmax = 2
            elif name == "Garbodor":
                gmax = 2
            elif name == "Kingler":
                gmax = 2
            elif name == "Lapras":
                gmax = 2
            elif name == "Inteleon":
                gmax = 2
            elif name == "Cinderace":
                gmax = 2
            elif name == "Rillaboom":
                gmax = 2
            elif name == "Urshifu":
                gmax = 2
            elif name == "Venusaur":
                gmax = 2
            elif name == "Blastoise":
                gmax = 2
            else:
                gmax = 1
        if x.startswith("Type"):
            types.append(x[8:].strip().lower())
        if x.startswith("BaseStats"):
            basestats = x[12:].strip().split(",")
            basestats = [int(x) for x in basestats]
        if x.startswith("Abilities"):
            abilities += x[12:].strip().split(",")
        if x.startswith("HiddenAbility"):
            abilities += [x[16:].strip()]
        if x.startswith("Moves"):
            moves = set(x[8:].strip().split(",")[1::2])
        if x.startswith("EggMoves"):
            moves = set(list(moves) + x[11:].strip().split(","))
        if x.startswith("#-------------------------------"):
            if len(types) != 2:
                types.append(None)
            pokemon.append([pokedex, name] + basestats + types + [gmax])
            abilities = []
            types = []
            moves = {}
    f.close()
    pokemon.pop(0)

    f = open(os.path.join(working_dir,"moves.txt"), "r")
    moves = []
    for x in f:
        if not x.startswith("#"):
            line = x.strip().split(",")
            movename = line[2]
            movetype = line[5].lower()
            moves.append([movename, movetype])
    f.close()

    f = open(working_dir+"/abilities.txt", "r")
    ability = []
    for x in f:
        if not (x.strip().startswith("#") or x.strip().startswith("ï")):
            line = x.strip().split(",")
            abilityname = line[2]
            ability.append([abilityname])
    f.close()

    f = open(working_dir+"/items.txt", "r")
    item = []
    for x in f:
        if not (x.strip().startswith("#") or x.strip().startswith("ï")):
            line = x.strip().split(",")
            itemname = line[2]
            item.append([itemname])
    f.close()

    nature = [["Lonely", "attack", "defence"], ["Brave", "attack", "speed"], ["Adamant", "Attack", "sp_atk"], ["Naughty", "Attack", "sp_def"],
        ["Bold", "defence", "defence"], ["Relaxed", "defence", "speed"], ["Impish", "defence", "sp_atk"], ["Lax", "defence", "sp_def"],
        ["Timid", "speed", "defence"], ["Hasty", "speed", "speed"], ["Jolly", "speed", "sp_atk"], ["Naive", "speed", "sp_def"],
        ["Modest", "sp_atk", "defence"], ["Mild", "sp_atk", "speed"], ["Quiet", "sp_atk", "sp_atk"], ["Rash", "sp_atk", "sp_def"],
        ["Calm", "sp_def", "defence"], ["Gentle", "sp_def", "speed"], ["Sassy", "sp_def", "sp_atk"], ["Careful", "sp_def", "sp_def"],
        ["Hardy", None, None], ["Docile", None, None], ["Serious", None, None], ["Bashful", None, None], ["Quirky", None, None]
          ]

    team_data = [
        ["yes", "Main Team", 1024,
         888, "Zacian", "Intrepid Sword", "Jolly", "Rusted Sword",
        "Wild Charge", "Play Rough", "Iron Head", "Close Combat", 100, 325, 359, 267, 196, 267, 375,
        252, 4, 0, 0, 0, 252, 31, 31, 31, 31, 31, 31, 1, "electric", "fairy", "steel", "fighting", "fairy", None,
         146, "Moltres", "Berserk", "Modest", "Weakness Policy",
         "Fiery Wrath", "Hurricane", "Taunt", "Nasty Plot", 100, 321, 236, 216, 349, 207, 279,
         0, 0, 0, 252, 4, 252, 31, 31, 31, 31, 31, 31, 1, "dark", "flying", "dark", "dark", "fire", "flying",
         645, "Landorus", "Sheer Force", "Modest", "Life Orb",
         "Earth Power", "Sludge Bomb", "Weather Ball", "Protect", 100, 319, 286, 216, 329, 197, 301,
         0, 0, 0, 252, 4, 252, 31, 31, 31, 31, 31, 31, 1, "ground", "poison", "normal", "normal", "ground", "flying",
         882, "Dracovish", "Strong Jaw", "Jolly", "Choice Scarf",
         "Fishios Rend", "Crunch", "Low Kick", "Outrage", 100, 321, 279, 236, 176, 196, 249,
         0, 252, 4, 0, 0, 252, 31, 31, 31, 31, 31, 31, 1, "water", "dark", "fighting", "dragon", "water", "dragon",
         598, "Ferrothorn", "Iron Barbs", "Relaxed", "Leftovers",
         "Power Whip", "Gyro Ball", "Leech Seed", "Protect", 100, 352, 224, 361, 144, 269, 76,
         252, 0, 252, 0, 4, 0, 31, 31, 31, 31, 31, 31, 1, "grass", "steel", "grass", "normal", "grass", "steel",
         59, "Arcanine", "Intimidate", "Jolly", "Mago Berry",
         "Flamethrower", "Snarl", "Will-O-Wisp", "Protect", 100, 326, 224, 325, 144, 269, 113,
         150, 0, 108, 0, 0, 150, 31, 31, 31, 31, 31, 31, 1, "fire", "dark", "fire", "normal", "fire", None
         ],
        ["yes", "Charizard Team", 560,
         6, "Charizard", "Solar Power", "timid", "Heavy Duty Boots",
        "Fire Blast", "Hurricane", "Solar Beam", "Focus Blast", 100, 297, 155, 192, 317, 206, 328,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 2, "fire", "flying", "grass", "fighting", "fire", "flying",
         547, "Whimsicott", "Prankster", "timid", "Leftovers",
         "Tailwind", "Moonblast", "U-turn", "Giga Drain", 100, 324, 152, 206, 191, 186, 364,
         252, 0, 0, 4, 0, 252, 31, 31, 31, 31, 31, 31, 1, "flying", "fairy", "bug", "grass", "grass", "fairy",
         94, "Gengar", "Cursed Body", "timid", "Life Orb",
         "Sludge Bomb", "Shadow Ball", "Trick Room", "Imprison", 100, 261, 121, 156, 359, 187, 350,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 2, "poison", "ghost", "psychic", "psychic", "ghost", "poison",
         423, "Gastrodon", "Storm Drain", "Relaxed", "Rindo Berry",
         "Scald", "Earth Power", "Protect", "Ice Beam", 100, 426, 171, 258, 220, 201, 102,
         252, 0, 252, 0, 4, 0, 31, 0, 31, 31, 31, 31, 2, "water", "ground", "normal", "ice", "water", "ground",
         275, "Shiftry", "Chlorophyll", "Modest", "Focus Sash",
         "Fake Out", "Sucker Punch", "Rock Slide", "Solar Blade", 100, 297, 155, 192, 317, 206, 328,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 2, "normal", "dark", "rock", "grass", "grass", "dark",
         38, "Ninetales", "Drought", "timid", "Charcoal",
         "Protect", "Foul Play", "Solar Beam", "Heat Wave", 100, 287, 157, 167, 261, 237, 328,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 2, "normal", "dark", "grass", "fire", "fire", None,
         ],
        ["omg", "squirtle squad", 197,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
        ],
        ["omg", "squirtle squad2", 160,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         ],
        ["omg", "squirtle squad3", 146,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         ],
        ["omg", "squirtle squad4", 120,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         ],
        ["omg", "squirtle squad5", 45,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         ],
        ["omg", "squirtle squad6", 0,
         7, "Squirtle", "Rain Dish", "timid", "Heavy Duty Boots",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Leftovers",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Life Orb",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Rindo Berry",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Focus Sash",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         7, "Squirtle", "Rain Dish", "timid", "Choice Scarf",
         "Waterfall", "Blizzard", "Protect", "Endure", 100, 229, 132, 166, 199, 165, 185,
         0, 0, 0, 252, 4, 252, 31, 0, 31, 31, 31, 31, 1, "water", "ice", "normal", "normal", "water", None,
         ],
    ]

    for row in team_data:
        Team_add_data(
            row[0], row[1], row[2],
            row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
            row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
            row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36],
            row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48],
            row[49], row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59],
            row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69], row[70],
            row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78], row[79], row[80], row[81], row[82],
            row[83], row[84], row[85], row[86], row[87], row[88], row[89], row[90], row[91], row[92], row[93],
            row[94], row[95], row[96], row[97], row[98], row[99], row[100], row[101], row[102], row[103], row[104],
            row[105], row[106], row[107], row[108], row[109], row[110], row[111], row[112], row[113], row[114], row[115], row[116],
            row[117], row[118], row[119], row[120], row[121], row[122], row[123], row[124], row[125], row[126], row[127],
            row[128], row[129], row[130], row[131], row[132], row[133], row[134], row[135], row[136], row[137], row[138],
            row[139], row[140], row[141], row[142], row[143], row[144], row[145], row[146], row[147], row[148], row[149], row[150],
            row[151], row[152], row[153], row[154], row[155], row[156], row[157], row[158], row[159], row[160], row[161],
            row[162], row[163], row[164], row[165], row[166], row[167], row[168], row[169], row[170], row[171], row[172],
            row[173], row[174], row[175], row[176], row[177], row[178], row[179], row[180], row[181], row[182],row[183], row[184],
            row[185], row[186], row[187], row[188], row[189], row[190], row[191], row[192], row[193], row[194],row[195],
            row[196], row[197], row[198], row[199], row[200], row[201], row[202], row[203], row[204], row[205], row[206],
            row[207], row[208], row[209], row[210], row[211], row[212],
        )

    for row in pokemon:
        pokedex = row[0]
        name = row[1]
        hp = row[2]
        attack = row[3]
        defence = row[4]
        sp_atk = row[6]
        sp_def = row[7]
        speed = row[5]
        type1 = row[8]
        type2 = row[9]
        gigantamax_factor = row[10]
        pokemon_add_data(pokedex, name, hp, attack, defence, sp_atk, sp_def,
                         speed, type1, type2, gigantamax_factor)

    for row in moves:
        name = row[0]
        type = row[1]
        move_add_data(name, type)

    for row in nature:
        nature = row[0]
        upstat = row[1]
        downstat = row[2]
        nature_add_data(nature, upstat, downstat)

    for row in ability:
        name = row[0]
        ability_add_data(name)

    for row in item:
        name = row[0]
        item_add_data(name)


if __name__ == "__main__":
    populate()
