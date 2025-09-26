from class_.Exceptions import VehicleError,NotFoundOption,InvalidVehicleDataError,ConcesionarioError
from class_.Vehicle import Vehicle
from class_.Concesionary import Concesionary

class Maintenance(Vehicle, Concesionary):
    def __init__(self):
        Vehicle().__init__(self)
        Concesionary().__init__(self)

    def show_maintenance(self):
        if not self.vehicles:
            raise ConcesionarioError(f"{self.alias} no tiene vehículos registrados para mostrar.")

        result = f"\n🛠️ Mantenimiento de vehículos en {self.alias}:\n"

        return result

    def register_maintenance(self, id,  title, description, date):
        self.maintenance_records[id] = {
            "description": description,
            "date": date
        }