from class_.Exceptions import VehicleError,NotFoundOption,InvalidVehicleDataError,ConcesionarioError
from class_.Vehicle import Vehicle
from functools import reduce

class Concesionary():
    def __init__(self, alias):
        self.alias = alias
        self.vehicles = []
        self.identities = [] # List to store unique vehicle IDs to associate car through option 1,2,3

    def add_(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ConcesionarioError("Auto or Moto can be added as object")
        self.vehicles.append(vehicle)
        self.identities.append(vehicle.identity)  # Store the vehicle's unique ID
        print(f"✅ Vehicle {vehicle.model} agregado correctamente a {self.alias}")

    def show_by_category(self):
        
        if not self.vehicles:
            return 0
        else:

            categories = {}
            for v in self.vehicles:
                categories[v.type_] = categories.get(v.type_, 0) + 1
            

        return reduce(lambda cc,key: cc + categories[key], categories, 0)

    def show(self, autos):
        current_vehicle = ""
        count = 0
        result = ""
        result+=f"\n🚘 Vehicles from {self.alias}:\n"
        for key in autos:
            brand = autos[key]["brand"]
            model = autos[key]["model"]
            year = autos[key]["year"]
            type_ = autos[key]["type"]
            icon = autos[key]["icon"]
            price = autos[key]["price"]

            if type_ == current_vehicle:
                count += 1
            else:
                count = 1
            current_vehicle = type_

            extra = autos[key].get("cilindre", autos[key].get("doors", "N/A"))

            result += (
                f"{count}º {icon} {type_}:"
                f"\n\t🔖 Brand: {brand}"
                f"\n\t🏷️ Model: {model}"
                f"\n\t🎗️ Year: {year}"
                f"\n\t💵 Price: {price}"
                f"\n\t⭐ Extra: {extra}{' cc' if type_ == 'moto' else ' doors'}\n"
            )
        return result

    def get_vehicle(self, id):
        autos = {}
        for v in self.vehicles:
            if str(v.get_id()) == str(id):
                autos[id] = v.get_properties()

        result = self.show(autos)
        return result

    def show_details_by_category(self):
        if not self.vehicles:
            raise ConcesionarioError(f"{self.alias} there are not any vehicles to show.")

        autos = {}
        for v in self.vehicles:
            autos[v.get_id()] = v.get_properties()

        result = self.show(autos)
        return result