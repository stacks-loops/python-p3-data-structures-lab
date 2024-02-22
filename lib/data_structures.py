spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [dish["name"] for dish in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [dish for dish in spicy_foods if dish["heat_level"] >= 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for dish in spicy_foods:
        emoji = "🌶" * dish["heat_level"]
        print(f"{dish['name']} ({dish['cuisine']}) | Heat Level: {emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dish in spicy_foods:
        if dish['cuisine'] == cuisine:
            return dish

def print_spiciest_foods(spicy_foods):
    
    for dish in spicy_foods:
        emoji = '🌶' * dish['heat_level']
        if dish["heat_level"] > 5:
            print(f"{dish['name']} ({dish['cuisine']}) | Heat Level: {emoji}")

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for dish in spicy_foods:
        heat_levels.append(dish['heat_level'])

    average = sum(heat_levels) / len(heat_levels)
    return average

def create_spicy_food(spicy_foods, spicy_food):
   spicy_foods.append(spicy_food)
   return spicy_foods
