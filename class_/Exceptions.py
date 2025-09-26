class VehicleError(Exception):
    """Excepción base para errores en vehículos"""
    pass

class NotFoundOption(Exception):
    """Excepción base para errores en vehículos"""
    pass

class InvalidVehicleDataError(VehicleError):
    """Datos inválidos al crear un vehículo"""
    pass

class ConcesionarioError(Exception):
    """Errores relacionados con el concesionario"""
    pass