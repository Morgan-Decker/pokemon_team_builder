import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_team_builder.settings')

import django

django.setup()

from builder.models import Pokemon, Move, Nature, Ability, Item, UserProfile, Team


def user_add_data(user):
    d, created = UserProfile.objects.get_or_create(user=user)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def Team_add_data(pokedex1, teamname, likes, name1, ability1, nature1, item1,
                  move1_1, move2_1, move3_1, move4_1, level1, hp1, atk1, def1, sp_atk1,
                  sp_def1, spd1, hpEV1, atkEV1, defEV1, sp_atkEV1, sp_defEV1, spdEV1,
                  hpIV1, atkIV1, defIV1, sp_atkIV1, sp_defIV1, spdIV1, gmax1,
                  movetype1_1, movetype2_1, movetype3_1, movetype4_1, type1_1, type2_1):
    d, created = Team.objects.get_or_create(teamname=teamname,
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
                                            userprofile="omg"
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
    f = open("C:/Users/craig/Documents/Uni/Computing Science/2nd Year/Semester 2/WAD2/Gen 8/pokemon.txt", "r")
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

    f = open("C:/Users/craig/Documents/Uni/Computing Science/2nd Year/Semester 2/WAD2/Gen 8/moves.txt", "r")
    moves = []
    for x in f:
        if not x.startswith("#"):
            line = x.strip().split(",")
            movename = line[2]
            movetype = line[5].lower()
            moves.append([movename, movetype])
    f.close()

    f = open("C:/Users/craig/Documents/Uni/Computing Science/2nd Year/Semester 2/WAD2/Gen 8/abilities.txt", "r")
    ability = []
    for x in f:
        if not (x.strip().startswith("#") or x.strip().startswith("ï")):
            line = x.strip().split(",")
            abilityname = line[2]
            ability.append([abilityname])
    f.close()

    f = open("C:/Users/craig/Documents/Uni/Computing Science/2nd Year/Semester 2/WAD2/Gen 8/items.txt", "r")
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
          ]

    team_data = [
        [888, "Single Pokemon Tester Team", 1024, "Zacian", "Intrepid Sword", "jolly", "Focus Sash",
        "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 325, 296, 266, 196, 266, 312,
        0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 1, "fire", "dark", "normal", "flying", "fairy", None],
        [6, "Charizard Team", 197, "Charizard", "Solar Power", "jolly", "Focus Sash",
        "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
        0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team2", 3, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team3", 565, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team4", 12, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team5", 123, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team6", 987, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team7", 986, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
        [6, "Charizard Team8", 1, "Charizard", "Solar Power", "jolly", "Focus Sash",
         "Flare Blitz", "Crunch", "Extreme Speed", "Roost", 100, 78, 84, 78, 100, 109, 85,
         0, 0, 0, 0, 0, 0, 31, 31, 31, 31, 31, 31, 2, "fire", "dark", "normal", "flying", "fire", "flying"],
    ]

    for row in team_data:
        Team_add_data(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                      row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                      row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33],
                      row[34], row[35], row[36])

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
