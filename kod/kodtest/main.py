# Knights of Dunvale
# By Preston and Jacob

import re
from rpg import *

things = {}

player = Creature("You", "It's you.", 100.0)


def parse_command(cmd: str):
    # Allow for multiple commands to be entered simultaneously, separated by "then"
    commands = re.split(r"\bthen\b", cmd.replace(" and ", " ").strip(".?! "))
    for command in commands:
        log("Command: '" + command + "'")
        # Split command into individual words
        words = command.split()
        # TODO: match first word to verb
        if len(words) > 1:
            for i in range(1, len(words)):
                word = words[i]
                # TODO: act on each listed Thing according to verb
                # TODO: account for prepositions like "in"
                log("Word: " + word)

    # words = re.sub(r"\bthe\b|\ba\b", " ", cmd).split(" ")


# TODO: Check and improve implementation
class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Desc', 'Vol', 'Wei', 'CA']))
        for item in self.items.values():
            print('\t'
                  .join([str(x) for x in [item.name, item.description, item.fill_volume, item.weight, item.carry_able]])
                  )


inventory = Inventory()
inventory.add_item(Item(None, None, None, None, None))
inventory.print_items()


def log(log_str: str):
    print(log_str)