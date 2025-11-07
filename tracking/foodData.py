foods = {
    "Chicken": {
        "calories": round(366 / 4),
        "protein": round(66 / 4),
        "fat": 0,
        "carbs": 0,
    },
    "Burger": {
        "calories": 167,  # per burger (not per oz)
        "protein": 19,
        "fat": 14,
        "carbs": 0,
    },
    "Shrimp": {
        "calories": round(120 / 4),
        "protein": round(23 / 4),
        "fat": 0,
        "carbs": 0,
    },
    "Salmon": {
        "calories": round(236 / 4),
        "protein": round(23 / 4),
        "fat": 0,
        "carbs": 0,
    },
    "Chicken (Bowl)": {
        "calories": round(160 / 4),
        "protein": round(26 / 4),
        "fat": 0,
        "carbs": 0,
    },
    "Sabor Chicken": {
        "calories": round(125 / 3),
        "protein": round(14 / 3),
        "fat": round(6 / 3),
        "carbs": round(3 / 3),
    },
    "Sabor Rice": {
        "calories": round(154 / 4),
        "protein": round(3 / 4),
        "fat": 0,
        "carbs": round(35 / 4),
    },
    "Sabor Cheese": {
        # 13 g serving ≈ 0.46 oz
        "calories": round(49 / 0.46),
        "protein": round(3 / 0.46),
        "fat": round(4 / 0.46),
        "carbs": 0,
    },
    "Ice Cream (All Toppings)": {
        "calories": 480,  # whole serving
        "protein": 0,
        "fat": 0,
        "carbs": 0,
    },
    "Beef Barbacoa": {
        "calories": round(450 / 7),
        "protein": round(50 / 7),
        "fat": 0,
        "carbs": 0,
    },
    "Barebell": {
        "calories": 210,
        "protein": 20,
        "fat": 7,
        "carbs": 20,
    },
    "Built": {
        "calories": 140,
        "protein": 17,
        "fat": 2,
        "carbs": 14,
    },
    "Rice Cake": {
        "calories": 60,
        "protein": 0,
        "fat": 1,
        "carbs": 12,
    },
    "Halos": {
        "calories": 135,
        "protein": 0,
        "fat": 0,
        "carbs": 23,
    },
    "Kind Bar": {
        "calories": 170,
        "protein": 7,
        "fat": 15,
        "carbs": 17,
    },
}


def foodInfo(foodName):
    return foods[foodName]


def get_foods():
    return foods
