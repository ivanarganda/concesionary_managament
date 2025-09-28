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

there_are_vehicles = False

def get_concesionaries():

    import string
    letters = list(string.ascii_lowercase)

    print("=== Concesionaries ===")

    for idx, (key, val) in enumerate(concesionaries.items(),start=1):
        print(f"{letters[idx-1].upper()}. {val} {concesionary_objects[key].show_by_category()}")
        if concesionary_objects[key].show_by_category() != 0:
            there_are_vehicles = True

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

def see_maintenance():

    while True:

        get_concesionaries()

        op_ = input("Choose the concesionary ('q' to back to main menu): \n")

        if op_ == "q":
            break

        concesionary_key = returnIndex(list(concesionaries.keys()), op_)
        co = concesionary_objects[concesionary_key]

        try:

            print(co.show_details_by_category())

            op_ = int(input("Type the vehicle ID to see maintenance records ('q' to back to main menu): \n"))

            if op_ == "q":
                break

            id_vehicle = returnIndex(co.identities, op_) # we use the id to edit or add maintenance records

            print(co.get_vehicle(id_vehicle))

        except (ConcesionarioError, VehicleError) as e:

            print(f"❌ {e}")
        
        except ValueError:

            print("❌ Invalid input. Please enter a valid vehicle ID or 'q' to quit.")
        
        except AttributeError:

            print("❌ This vehicle has no maintenance records.")

def add_new_vehicle():

    global there_are_vehicles

    while True:

        try:

            get_concesionaries()

            op_ = input("Choose the concesionary ('q' to back to main menu): \n")

            # op_ = "a" # Hardcodeamos las validaciones básicas TODO

            if op_ == "q":
                break

            concesionary_key = returnIndex(list(concesionaries.keys()), op_)
            co = concesionary_objects[concesionary_key]

            type_vehicle = input("Type the kind of vehicle (moto or auto):\n")

            # type_vehicle = "auto" # Hardcodeamos las validaciones básicas TODO

            if type_vehicle not in vehicles_:
                raise Exception("Not found type")

            brand = input(f"Type the brand of {type_vehicle}: ")
            model = input(f"Type the model of {type_vehicle}: ")
            year = int(input(f"Type the year of fabrication of {type_vehicle}: "))
            price = int(input(f"Type the price of {type_vehicle}: "))

            # Hardcodeamos las validaciones básicas TODO
            # brand = "wfef"
            # model = "wefwef"
            # year = 2020
            # price = 20000

            if brand == "" or model == "" or year <= 0 or price <= 0:
                raise Exception("Type correct data format")

            extra = int(input(vehicles_[type_vehicle]["extra"]))
            # extra = 5 # Hardcodeamos las validaciones básicas TODO
            vehicle = vehicles_[type_vehicle]["class"](brand, model, year, extra, price)
            co.add_(vehicle)

            there_are_vehicles = True # Given that a vehicle has been added, we set this to True

            confirm = input("Do you desire to add another one? (s/n): ")

            if confirm.lower() == 'n':
                break

        except Exception as e:
            print(f"❌ Error: {e}")

def main_menu():

    while True:
        try:

            print(there_are_vehicles)

            menus = get_menus( there_are_vehicles )
            menu = generateMenu(menus["main_menu"]["options"])

            op = input(f"{menu["menu"]}{menu["range"]}")

            if op == len(menu["menu"]): # allways exist is the last option

                print("Catch you later! 👋")
                break

            if op not in menus["main_menu"]["dispatchs"]: raise NotFoundOption("Not found dispatch option")
            
            eval(menus["main_menu"]["dispatchs"][op])()

        except (NotFoundOption,VehicleError, ConcesionarioError) as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main_menu()