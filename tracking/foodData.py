foods = {
    "Chicken": {
        "calories": 48,
        "protein": 9,
        "fat": 1,
        "carbs": 0,
    },
    "Burger": {
        "calories": 167,  # per burger (not per oz)
        "protein": 19,
        "fat": 14,
        "carbs": 0,
    },
    "Shrimp": {
        "calories": 30,
        "protein": 6,
        "fat": 0,
        "carbs": 0,
    },
    "Salmon": {
        "calories": 58,
        "protein": 5,
        "fat": 4,
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
    "Shredded Cheese": {
        "calories": 110,
        "protein": 7,
        "fat": 9,
        "carbs": 1,
    },
    "Barebell": {
        "calories": 210,
        "protein": 20,
        "fat": 7,
        "carbs": 20,
    },
    "Built Puff": {
        "calories": 140,
        "protein": 17,
        "fat": 2,
        "carbs": 14,
    },
    "Chocolate Rice Cakes": {
        "calories": 67,
        "protein": 0,
        "fat": 1,
        "carbs": 14,
    },
    "Caramel Rice Cakes": {
        "calories": 57,
        "protein": 0,
        "fat": 1,
        "carbs": 13,
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
    "Cheesecake": {
        "calories": 100,
        "protein": 2,
        "fat": 7,
        "carbs": 8,
    },
    "Brownie Cookie Dough Ice Cream": {
        "calories": 266,
        "protein": 4,
        "fat": 12,
        "carbs": 36,
    },
    "Vanilla Soft Serve": {
        "calories": 280,
        "protein": 6,
        "fat": 10,
        "carbs": 38,
    },
    "Hard Cooked Eggs": {
        "calories": 88,
        "protein": 7,
        "fat": 6,
        "carbs": 0,
    },
    "Cheese Pizza": {
        "calories": 215,
        "protein": 9,
        "fat": 7,
        "carbs": 30,
    },
    "Vegan Mexican Rice": {
        "calories": 42,
        "protein": 2,
        "fat": 1,
        "carbs": 7,
    },
    "Halal Chicken": {
        "calories": 70,
        "protein": 8,
        "fat": 2,
        "carbs": 0,
    },
    "Jasmine Rice": {
        "calories": 48,
        "protein": 0,
        "fat": 0,
        "carbs": 9,
    },
    "Green Apple": {
        "calories": 100,
        "protein": 0,
        "fat": 0,
        "carbs": 25,
    },
}


def foodInfo(foodName):
    return foods[foodName]


def get_foods():
    return foods
