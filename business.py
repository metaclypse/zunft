
BUSINESS_TYPES = {
    "forge": 0,
    "carpenter": 1,
    "perfumer": 2,
    "alchemist": 3,
    "tavern": 4,
    "church": 5,
    "hideout": 6,
    "guardhouse": 7
}


class Business(object):
    def __init__(self):
        self.title = ""
        self.type = 0
        self.level = 0
        self.employees = []
        self.resources = {}
        self.building = None

