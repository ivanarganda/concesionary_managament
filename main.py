# Classes
from class_.Exceptions import VehicleError,NotFoundOption,InvalidVehicleDataError,ConcesionarioError
from helpers.utils import get_type_vehicles,generateMenu,returnIndex,get_menus,get_concecionaries_items
from class_.Vehicle import Vehicle
from class_.Auto import Auto
from class_.Moto import Moto
from class_.Concesionary import Concesionary
from class_.Maintenance import Maintenance

# Common functions
from functools import reduce

# Definimos excepciones personalizadas

fields_concesionaries = get_concecionaries_items("fields")

concesionaries = get_concecionaries_items("dict")

# Diccionario para instanciar vehículos
vehicles_ = get_type_vehicles()

# Almacenamos concesionarios creados
concesionary_objects = get_concecionaries_items("object_classes")

def get_concesionaries():

    import string
    letters = list(string.ascii_lowercase)

    print("=== Concesionaries ===")

    for idx, (key, val) in enumerate(concesionaries.items(),start=1):
        print(f"{letters[idx-1].upper()}. {val} {concesionary_objects[key].show_by_category()}")

    print("======")

def see_vehicles():

    while True:

        get_concesionaries()

        op_ = input("Choose the concesionary ('q' to back to main menu): \n")

        if op_ == "q":
            break

        concesionary_key = returnIndex(list(concesionaries.keys()), op_)
        co = concesionary_objects[concesionary_key]

        try:

            print(co.show_details_by_category())

        except ConcesionarioError as e:

            print(f"❌ {e}")

def add_new_vehicle():

    while True:

        try:

            get_concesionaries()

            op_ = input("Choose the concesionary ('q' to back to main menu): \n")

            if op_ == "q":
                break

            concesionary_key = returnIndex(list(concesionaries.keys()), op_)
            co = concesionary_objects[concesionary_key]

            type_vehicle = input("Type the kind of vehicle (moto or auto):\n")

            if type_vehicle not in vehicles_:
                raise Exception("Not found type")

            brand = input(f"Type the brand of {type_vehicle}: ")
            model = input(f"Type the model of {type_vehicle}: ")
            year = int(input(f"Type the year of fabrication of {type_vehicle}: "))
            price = int(input(f"Type the price of {type_vehicle}: "))

            if brand == "" or model == "" or year <= 0 or price <= 0:
                raise Exception("Type correct data format")

            extra = int(input(vehicles_[type_vehicle]["extra"]))
            vehicle = vehicles_[type_vehicle]["class"](brand, model, year, extra, price)
            co.add_(vehicle)

            confirm = input("Do you desire to add another one? (s/n): ")

            if confirm.lower() == 'n':
                break

        except Exception as e:
            print(f"❌ Error: {e}")

# Ejemplo de uso con manejo de errores

menus = get_menus()

def main_menu():

    try:

        while True:

            menu = generateMenu(menus["main_menu"]["options"])
            op = input(f"{menu["menu"]}{menu["range"]}")

            if op == "4":

                print("Catch you later! 👋")
                break

            if op not in menus["main_menu"]["dispatchs"]: raise NotFoundOption("Not found dispatch option")
            
            eval(menus["main_menu"]["dispatchs"][op])()

    except (NotFoundOption,VehicleError, ConcesionarioError) as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main_menu()