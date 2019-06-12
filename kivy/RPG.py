from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.event import EventDispatcher

from kivy.clock import Clock

FPS = 1

# resources
RESOURCES = {
    "food": {
        "n": 500,
        "per_s": 0
    },
    "wood": {
        "n": 0,
        "per_s": 0
    },
    "stone": {
        "n": 0,
        "per_s": 0
    },
    "metal": {
        "n": 0,
        "per_s": 0
    }
}

# Buildings
BUILDINGS = {
    "farm": {
        "name": "Farm",
        "resources_per_s": {"food": 10},
        "n": 0,
    },
    "forest_camp": {
        "name": "Forest Camp",
        "resources_per_s": {"food": 2, "wood": 5},
        "n": 0,
    },
    "quarry": {
        "name": "Quarry",
        "resources_per_s": {"stone": 2},
        "n": 0,
    },
    "mine": {
        "name": "Mine",
        "resources_per_s": {"metal": 1},
        "n": 0,
    }
}

# units
UNITS = {
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
            "food": 80,
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
            "food": 100,
            "metal": 15,
        },
        "attack": 10,
        "life": 25,
    },
    "swordman": {
        "name": "Swordman",
        "n": 0,
        "cost": {
            "food": 100,
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
            "food": 300,
            "wood": 15,
            "metal": 25,
        },
        "attack": 15,
        "life": 80
    }
}


class Farm(EventDispatcher):
    id = "farm"
    name = StringProperty(BUILDINGS.get(id).get("name", "Farm"))
    n = NumericProperty(BUILDINGS.get(id).get("n", 0))
    resources_per_s_per_unit = DictProperty({})
    resources_per_s = DictProperty({})
    id = StringProperty(id)

    def __init__(self):
        super().__init__()
        self.resources_per_s_per_unit = BUILDINGS.get(self.id).get("resources_per_s", 0)
        self.resources_per_s = {}
        for resource in RESOURCES:
            self.resources_per_s[resource] = self.resources_per_s_per_unit.get(resource, 0) * self.n


class ForestCamp(EventDispatcher):
    id = "forest_camp"
    name = StringProperty(BUILDINGS.get(id).get("name", "Forest Camp"))
    n = NumericProperty(BUILDINGS.get(id).get("n", 0))
    resources_per_s_per_unit = DictProperty({})
    resources_per_s = DictProperty({})
    id = StringProperty(id)

    def __init__(self):
        super().__init__()
        self.resources_per_s_per_unit = BUILDINGS.get(self.id).get("resources_per_s", 0)
        self.resources_per_s = {}
        for resource in RESOURCES:
            self.resources_per_s[resource] = self.resources_per_s_per_unit.get(resource, 0) * self.n


class Quarry(EventDispatcher):
    id = "quarry"
    name = StringProperty(BUILDINGS.get(id).get("name", "Quarry"))
    n = NumericProperty(BUILDINGS.get(id).get("n", 0))
    resources_per_s_per_unit = DictProperty({})
    resources_per_s = DictProperty({})
    id = StringProperty(id)

    def __init__(self):
        super().__init__()
        self.resources_per_s_per_unit = BUILDINGS.get(self.id).get("resources_per_s", 0)
        self.resources_per_s = {}
        for resource in RESOURCES:
            self.resources_per_s[resource] = self.resources_per_s_per_unit.get(resource, 0) * self.n


class Mine(EventDispatcher):
    id = "mine"
    name = StringProperty(BUILDINGS.get(id).get("name", "Mine"))
    n = NumericProperty(BUILDINGS.get(id).get("n", 0))
    resources_per_s_per_unit = DictProperty({})
    resources_per_s = DictProperty({})
    id = StringProperty(id)

    def __init__(self):
        super().__init__()
        self.resources_per_s_per_unit = BUILDINGS.get(self.id).get("resources_per_s", 0)
        self.resources_per_s = {}
        for resource in RESOURCES:
            self.resources_per_s[resource] = self.resources_per_s_per_unit.get(resource, 0) * self.n


class Buildings(GridLayout):
    farm = ObjectProperty(Farm())
    forest_camp = ObjectProperty(ForestCamp())
    quarry = ObjectProperty(Quarry())
    mine = ObjectProperty(Mine())

    def calc_total_villager_working(self):
        self.total = 0
        for building_name in BUILDINGS:
            building = getattr(self, building_name)
            self.total += building.n
        return self.total


class Food(EventDispatcher):
    id = "food"
    n = NumericProperty(RESOURCES.get(id).get("n", 0))
    per_s = NumericProperty(RESOURCES.get(id).get("per_s", 0))


class Wood(EventDispatcher):
    id = "wood"
    n = NumericProperty(RESOURCES.get(id).get("n", 0))
    per_s = NumericProperty(RESOURCES.get(id).get("per_s", 0))


class Stone(EventDispatcher):
    id = "stone"
    n = NumericProperty(RESOURCES.get(id).get("n", 0))
    per_s = NumericProperty(RESOURCES.get(id).get("per_s", 0))


class Metal(EventDispatcher):
    id = "metal"
    n = NumericProperty(RESOURCES.get(id).get("n", 0))
    per_s = NumericProperty(RESOURCES.get(id).get("per_s", 0))


class Resources(GridLayout):
    food = ObjectProperty(Food())
    wood = ObjectProperty(Wood())
    stone = ObjectProperty(Stone())
    metal = ObjectProperty(Metal())

    def update(self, dt):
        # print("update resources")
        self.food.n += dt * self.food.per_s
        self.wood.n += dt * self.wood.per_s
        self.stone.n += dt * self.stone.per_s
        self.metal.n += dt * self.metal.per_s
        # print(self.food)


class Villager(EventDispatcher):
    id = "villager"
    name = StringProperty(UNITS.get(id).get("name"))
    n = NumericProperty(UNITS.get(id).get("n"))
    cost = DictProperty(UNITS.get(id).get("cost"))


class Spearman(EventDispatcher):
    id = "spearman"
    name = StringProperty(UNITS.get(id).get("name"))
    n = NumericProperty(UNITS.get(id).get("n"))
    cost = DictProperty(UNITS.get(id).get("cost"))


class Axeman(EventDispatcher):
    id = "axeman"
    name = StringProperty(UNITS.get(id).get("name"))
    n = NumericProperty(UNITS.get(id).get("n"))
    cost = DictProperty(UNITS.get(id).get("cost"))


class Swordman(EventDispatcher):
    id = "swordman"
    name = StringProperty(UNITS.get(id).get("name"))
    n = NumericProperty(UNITS.get(id).get("n"))
    cost = DictProperty(UNITS.get(id).get("cost"))


class Cavalry(EventDispatcher):
    id = "cavalry"
    name = StringProperty(UNITS.get(id).get("name"))
    n = NumericProperty(UNITS.get(id).get("n"))
    cost = DictProperty(UNITS.get(id).get("cost"))


class Units(GridLayout):
    villager = ObjectProperty(Villager())
    spearman = ObjectProperty(Spearman())
    axeman = ObjectProperty(Axeman())
    swordman = ObjectProperty(Swordman())
    cavalry = ObjectProperty(Cavalry())


class RecruitMenu(GridLayout):
    pass


class Game(GridLayout):
    resources = ObjectProperty(Resources())
    units = ObjectProperty(Units())
    buildings = ObjectProperty(Buildings())

    def update(self, dt):
        # print("update game")
        self.resources.update(dt)
    
    def recruit(self, unit, n):
        n = int(n)
        if self.resources.food.n >= unit.cost.get("food", 0) * n and\
                self.resources.wood.n >= unit.cost.get("wood", 0) * n and\
                self.resources.stone.n >= unit.cost.get("stone", 0) * n and\
                self.resources.metal.n >= unit.cost.get("metal", 0) * n:
            self.resources.food.n -= unit.cost.get("food", 0) * n
            self.resources.wood.n -= unit.cost.get("wood", 0) * n
            self.resources.stone.n -= unit.cost.get("stone", 0) * n
            self.resources.metal.n -= unit.cost.get("metal", 0) * n
            unit.n += n
    
    def calc_idle_villagers(self):
        return self.units.villager.n - self.buildings.calc_total_villager_working()
    
    def update_resources_per_s(self):
        self.resources.food.per_s = 0
        self.resources.wood.per_s = 0
        self.resources.stone.per_s = 0
        self.resources.metal.per_s = 0
        for resource_name in RESOURCES:
            resource = getattr(self.resources, resource_name)
            for building_name in BUILDINGS:
                building = getattr(self.buildings, building_name)
                resource.per_s += building.resources_per_s[resource_name]


    def change_people_working_in_a_building(self, building, n):
        n = int(n)
        idle = self.calc_idle_villagers()
        # difference in workers between now and future:
        diff = n - building.n

        if idle >= diff:
            building.n = n
            for resource_name in RESOURCES:
                building.resources_per_s[resource_name] = building.resources_per_s_per_unit.get(resource_name, 0) * n
            self.update_resources_per_s()

class RPGApp(App):
    game = ObjectProperty(Game())

    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0/FPS)
        return game

if __name__ == "__main__":
    RPGApp().run()