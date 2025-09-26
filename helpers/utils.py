import sys
from class_.Auto import Auto
from class_.Moto import Moto
from class_.Concesionary import Concesionary

def generateMenu(menu):
    result = ""
    for key, val in menu.items():
        result += f"{key}. {val}"
    return {
        "menu": result,
        "range": f"Type an option (1-{len(menu.keys())})\n"
    }

def get_menus():
    return {
        "main_menu": {
            "title": f"\n=== Concesionary warehouse ===\n",
            "options": {
                "1":"See concesionaries\n",
                "2":"Add vehicles\n",
                "3":"See vehicles\n",
                "4":"Exit\n"
            },
            "dispatchs": {
                "1":"get_concesionaries",
                "2":"add_new_vehicle",
                "3":"see_vehicles"
            }
        }
    }

def get_concecionaries_items(key):

    try:

        return {
            "fields": [
                "first_concesionary",
                "second_concesionary"
            ],
            "dict": {
                "first_concesionary": "First concesionary",
                "second_concesionary": "Second concesionary"
            },
            "object_classes": {
                "first_concesionary": Concesionary("First concesionary"),
                "second_concesionary": Concesionary("Second concesionary")
            }
        }[key]

    except KeyError:
        return False

def returnIndex(list_, i):

    try:

        import string
        letters = list(string.ascii_lowercase)

        if type(i) is str and letters.index(i) > -1:
            i = letters.index(i.lower())
            return list_[i]

        return list_[i-1]

    except IndexError:

        return False

def get_type_vehicles():

    return {

        "moto": {

            "class": Moto,
            "extra": "Type the cilindrers: "

        },
        "auto": {

            "class": Auto,
            "extra": "Type the number of doors: "

        }

    }