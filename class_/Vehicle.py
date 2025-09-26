class Vehicle:
    def __init__(self, brand, model, year, price, type_, icon):
        if year < 1900 or year > 2100:
            raise InvalidVehicleDataError(f"Año inválido: {year}")
        if price < 0:
            raise InvalidVehicleDataError(f"Precio no puede ser negativo: {price}")

        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.type_ = type_
        self.icon = icon

    def get_properties(self):
        return {
            "type": self.type_,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "icon": self.icon
        }