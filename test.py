from random import choice
from collections import Counter, defaultdict
import os

# Settings:


colors = {
    "dark": "\033[1;30;40m",
    "red": "\033[1;31;40m",
    "green": "\033[1;32;40m",
    "yellow": "\033[1;33;40m",
    "blue": "\033[1;34;40m",
    "white": "\033[1;37;40m",
    "blue_bg": "\033[0;37;44m",
    "color_over": "\033[0m",
}

resources = {"food": 200, "wood": 0, "stone": 0, "metal": 0}

buildings = {
    "farm": {
        "cost": {"food": 50, "wood": 20},

    }
}

units = {
    "villager": {
        "name": "Villager",
        "shortname": "v",
        "n": 0,
        "cost": {
            "food": 50,
        },
        "attack": 1,
        "life": 15,
    },
    "spearman": {
        "name": "Spearman",
        "shortname": "sp",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 10,
            "metal": 8,
        },
        "attack": 7,
        "life": 30,
    },
    "axeman": {
        "name": "Axeman",
        "n": 0,
        "cost": {
            "food": 50,
            "metal": 15,
        },
        "attack": 10,
        "life": 25,
    },
    "swordsman": {
        "name": "Swordsman",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 5,
            "metal": 25,
        },
        "attack": 12,
        "life": 50,
    },
    "cavalry": {
        "name": "Cavalry",
        "n": 0,
        "cost": {
            "food": 200,
            "wood": 15,
            "metal": 25,
        },
        "attack": 15,
        "life": 80
    }
}

army1_conf = {
    "axemen": 4,
    "cavalry": 1
}
army2_conf = {
    "axemen": 10
}

# General Functions:


def clean():
    os.system("clear")


def pretty_options(options):
    options = ["[%s]%s" % (option[0], option[1:]) for option in options]
    return " - ".join(options) + "\n"


def handle_options(msg, options):
    return input("{} {}".format(msg, pretty_options(options)))


# End of General Functions

# Menus:


def first_menu():
    clean()
    options = ["yes", "no"]
    msg = "want to play?"
    option = handle_options(msg, options)
    if option[0].lower() != "y":
        exit()
    clean()


def resources_menu():
    print("{green}Resources:{color_over} {}\n".format(resources, **colors))


def units_menu():
    print("{blue_bg}Units:{color_over}".format(**colors))
    for unit in units.values():
        # print(unit)
        print("{green}{}{color_over} {}".format(unit["name"], unit["n"], **colors))
    print()


def main_menu():
    clean()
    print("Main Menu\n")
    resources_menu()
    units_menu()

    options = ["recruit", "increase resources"]
    msg = "what do you want?"
    option = handle_options(msg, options)
    if option[0].lower() == "r":
        recruit_menu()
    if option[0].lower() == "i":
        increase_resources_menu()
    else:
        exit()


def recruit_menu():
    clean()
    resources_menu()
    units_menu()
    for unit in units.values():
        # print("%s%s:%s %s" % (green, unit["name"], color_over, unit["cost"]))
        print("{green}{}:{color_over} {}".format(unit["name"], unit["cost"], **colors))
    options = units
    msg = "what unit you want to buy?"
    option = handle_options(msg, options)

    convert_shortname = {"v": "villager", "sp": "spearman"}

    if option in convert_shortname:
        unit = convert_shortname[option]
        cost = Resources(units[unit]["cost"])
        if resources > cost:
            units[unit]["n"] += 1
            resources - cost
            # resources[]
        else:
            print("you don't have enough resources\n")
    else:
        print("I don't understand your option\n")

    options = ["continue buying", "quit"]
    msg = "what you want?"
    option = handle_options(msg, options)
    if option and option[0].lower() == "c":
        recruit_menu()

    main_menu()


def increase_resources_menu():
    clean()
    resources_menu()
    units_menu()
    options = resources.dict.keys()
    msg = "what resource do you want?"
    option = handle_options(msg, options)
    if option and option[0].lower() == "f":
        resources.dict["food"] += units["villager"]["n"]
    options = ["continue", "quit"]
    msg = "what you want?"
    option = handle_options(msg, options)
    if option and option[0].lower() == "c":
        increase_resources_menu()

    main_menu()

# end of menus

# resources


class Resources(object):
    def __init__(self, resources):
        self.dict = resources
        self.n = len(self.dict)

    def __repr__(self):
        return str(self.dict)

    def __gt__(self, other):
        for resource_name in self.dict:
            if self.dict.get(resource_name, 0) < other.dict.get(resource_name, 0):
                return False
        return True

    def __sub__(self, other):
        for resource_name in self.dict:
            self.dict[resource_name] -= other.dict.get(resource_name, 0)
        return self.dict

# end of resources


# Units


class Trop(object):
    def __init__(self):
        self.name = self.conf["name"]
        self.attack = self.conf["attack"]
        self.life = self.conf["life"]

    def take_damage(self, damage):
        self.life -= damage

    def __repr__(self):
        return "%s(attack: %s, life: %s)" % (self.__class__.__name__, self.attack, self.life)


class Axeman(Trop):
    def __init__(self):
        self.conf = units["axeman"]
        super(Axeman, self).__init__()


class Cavalry(Trop):
    def __init__(self):
        self.conf = units["cavalry"]
        super(Cavalry, self).__init__()


def create_a_trop_object(trop_name):
    if trop_name.lower() == "axemen":
        return Axeman()
    if trop_name.lower() == "cavalry":
        return Cavalry()


class Army(object):
    def __init__(self, army_conf):
        self.list = []
        for trop_name, n_trop in army_conf.items():
            # print(trop_name)
            for i in range(n_trop):
                trop = self.create_a_trop_object(trop_name)
                self.list.append(trop)

    def __repr__(self):
        return "%s" % self.list

    def units_resume(self):
        all = defaultdict(int)
        for trop in self.list:
            all[trop.name] += 1
        return dict(all)

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, i):
        return self.list[i]

    def remove(self, trop):
        self.list.remove(trop)

    def create_a_trop_object(self, trop_name):
        if trop_name.lower() == "axemen":
            return Axeman()
        if trop_name.lower() == "cavalry":
            return Cavalry()


def create_an_army(army_conf):
    army = []
    for trop_name, n_trop in army_conf.items():
        # print(trop_name)
        for i in range(n_trop):
            trop = create_a_trop_object(trop_name)
            army.append(trop)
    return army


def fight(attacking_army, defending_army):
    # fight:
    # all_that_dies = []
    # print("attacking_army", attacking_army)
    for trop_attacking in attacking_army:
        # print("trop_attacking", trop_attacking)
        if not defending_army:
            break
        trop_defending = choice(defending_army)
        # print("trop_defending", trop_defending)
        trop_defending.take_damage(trop_attacking.attack)


def check_all_dead(army):
    # print("check_all_dead()", army.list, len(army.list))
    all_that_live = []
    all_that_dies = []
    for i, trop in enumerate(army.list):
        # print("i", i)
        # print("life", trop.life)
        # print("army.list", army.list)
        if trop.life > 0:
            all_that_live.append(trop)
        else:
            all_that_dies.append(trop)
    army.list = all_that_live
    all_that_dies = Counter(all_that_dies)
    # print("all_that_dies", all_that_dies)


# create all units' object
# armyx = {"axemen": 2, "cavalry": 1} -> [axeman, axeman, cavalry]
army1 = Army(army1_conf)
print("army1", army1.units_resume())
army2 = Army(army2_conf)
print("army2", army2.units_resume())


# print("%s vs %s" % (army1, army2))

round = 0
while army1 and army2:
    round += 1
    print("\nround %s" % round)
    if round > 5:
        break
    # print("army1", army1)
    # print("army2", army2)

    fight(army1, army2)
    # print("army1", army1)
    # print("army2", army2)
    fight(army2, army1)
    check_all_dead(army1)
    check_all_dead(army2)

    # print("army1", army1)
    print("army1", army1.units_resume())
    # print("army2", army2)
    print("army2", army2.units_resume())


resources = Resources(resources)
# first_menu()
main_menu()
