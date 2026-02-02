inventory = {
    "C01": {"brand": "Kia", "model": "Seltos", "color": "white", "price": 20000},
    "C02": {"brand": "Toyota", "model": "Fortuner", "color": "black", "price": 45000},
    "C03": {"brand": "Mercedes", "model": "E-Class", "color": "white", "price": 60000},
    "C04": {"brand": "BMW", "model": "M340i", "color": "black", "price": 70000},
    "C05": {"brand": "Hyundai", "model": "Verna", "color": "white", "price": 18000},
}

# // Filtering

expensive_cars = {
    id: details for id, details in inventory.items() if details["price"] > 30000
}
print(expensive_cars)


# Filtering + Converting [ her we are filtering and converting the result in list]

white_cars = [
    {"id": c_id, **details}
    for c_id, details in inventory.items()
    if details["color"] == "white"
]
print(white_cars)

# Advanced Transformation (Selecting Specific Fields)

car_models = [details["brand"].upper() for details in inventory.values()]

print(car_models)

# Sorting (Using sorted() with a List)

all_cars = [{"id": car_id, **details} for car_id, details in inventory.items()]

sorted_by_price = sorted(all_cars, key=lambda x: x["price"])
print(sorted_by_price)
