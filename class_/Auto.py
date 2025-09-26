from class_.Exceptions import VehicleError,NotFoundOption,InvalidVehicleDataError,ConcesionarioError
from class_.Vehicle import Vehicle

class Auto(Vehicle):
    def __init__(self, brand, model, year, doors, price):
        if doors <= 0:
            raise InvalidVehicleDataError(f"Un auto debe tener al menos 1 puerta, recibido: {doors}")
        super().__init__(brand, model, year, price, "auto", "🚗 ")
        self.doors = doors

    def get_properties(self):
        props = super().get_properties()
        props["doors"] = self.doors
        return props