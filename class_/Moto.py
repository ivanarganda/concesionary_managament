from class_.Exceptions import VehicleError,NotFoundOption,InvalidVehicleDataError,ConcesionarioError
from class_.Vehicle import Vehicle

class Moto(Vehicle):
    def __init__(self, brand, model, year, cilindre, price):
        if cilindre <= 0:
            raise InvalidVehicleDataError(f"Cilindraje debe ser > 0, recibido: {cilindre}")
        super().__init__(brand, model, year, price, "moto", "🏍️ ")
        self.cilindre = cilindre

    def get_properties(self):
        props = super().get_properties()
        props["cilindre"] = self.cilindre
        return props