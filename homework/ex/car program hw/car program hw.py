import json
import os
import csv

cars = [
    {"id": 1, "brand": "Opel", "model": "Astra", "hp": 110, "price": 2000},
    {"id": 2, "brand": "Volkswagen", "model": "Golf", "hp": 140, "price": 4000},
    {"id": 3, "brand": "BMW", "model": "M3", "hp": 300, "price": 10000},
    {"id": 4, "brand": "Porsche", "model": "911", "hp": 450, "price": 50000},
    {"id": 5, "brand": "Ferrari", "model": "488", "hp": 670, "price": 250000},
    {"id": 6, "brand": "Lamborghini", "model": "Aventador", "hp": 700, "price": 400000},
]

slow_cars = []
fast_cars = []
sport_cars = []
cheap_cars = []
medium_cars = []
expensive_cars = []

for car in cars:
    if car["hp"] < 120:
        slow_cars.append(car)
    elif car["hp"] < 180:
        fast_cars.append(car)
    else:
        sport_cars.append(car)

    if car["price"] < 1000:
        cheap_cars.append(car)
    elif car["price"] < 5000:
        medium_cars.append(car)
    else:
        expensive_cars.append(car)

if not os.path.exists("output_data"):
    os.makedirs("output_data")

with open("output_data/slow_cars.json", "w") as file:
    json.dump(slow_cars, file)

with open("output_data/fast_cars.json", "w") as file:
    json.dump(fast_cars, file)

with open("output_data/sport_cars.json", "w") as file:
    json.dump(sport_cars, file)

with open("output_data/cheap_cars.json", "w") as file:
    json.dump(cheap_cars, file)

with open("output_data/medium_cars.json", "w") as file:
    json.dump(medium_cars, file)

with open("output_data/expensive_cars.json", "w") as file:
    json.dump(expensive_cars, file)

brand_name = "Opel"
brand_cars = [car for car in cars if car["brand"] == brand_name]

with open(f"output_data/{brand_name.lower()}.json", "w") as file:
    json.dump(brand_cars, file)

with open("input.csv", "r") as file:
    reader = csv.DictReader(file)
    cars_from_csv = [car for car in reader]

with open("output_data/cars_from_csv.json", "w") as file:
    json.dump(cars_from_csv, file)


