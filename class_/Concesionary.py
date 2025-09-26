class Concesionary():
    def __init__(self, alias):
        self.alias = alias
        self.vehicles = []

    def add_(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ConcesionarioError("Auto or Moto can be added as object")
        self.vehicles.append(vehicle)
        print(f"✅ Vehicle {vehicle.model} agregado correctamente a {self.alias}")

    def show_by_category(self):
        
        if not self.vehicles:
            return 0
        else:

            categories = {}
            for v in self.vehicles:
                categories[v.type_] = categories.get(v.type_, 0) + 1
            

        return reduce(lambda cc,key: cc + categories[key], categories, 0)

    def show_details_by_category(self):
        if not self.vehicles:
            raise ConcesionarioError(f"{self.alias} no tiene vehículos registrados para mostrar.")

        autos = {}
        for v in self.vehicles:
            autos[v.model] = v.get_properties()

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