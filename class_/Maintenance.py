from class_.Vehicle import Vehicle
from class_.Concesionary import Concesionary

class Maintenance(Concesionary):

    def __init__(self,alias):

        super().__init__(self,alias)
        self.vehicles = {}
        self.maintenances_history = {}

    def register_maintenance(self, vehicle, maintenance):

        try:

            self.vehicles = super().vehicles

            if not isinstance(vehicle, Vehicle):raise Exception("Error passing instance. Excepted Vehicle")
            maintenances_history.append(maintenance)
            vehicles["maintenances"] = maintenances_history

        except Exception as e:

            print(e)

    def info(self):
        
        return self.vehicles
