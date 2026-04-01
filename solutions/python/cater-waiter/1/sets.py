"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS
)


def clean_ingredients(dish_name, dish_ingredients):
    """
    Remove duplicates and return (dish_name, ingredient_set)
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """
    Append Cocktail if alcohol present,
    otherwise Mocktail.
    """
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """
    Return 'dish_name: CATEGORY'
    """

    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """
    Return (dish_name, special_ingredients_set)
    """
    dish_name, ingredients = dish
    return (dish_name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """
    Return master set of all ingredients
    """
    master_set = set()
    for dish in dishes:
        master_set |= dish
    return master_set


def separate_appetizers(dishes, appetizers):
    """
    Remove appetizer dishes and de-duplicate
    """
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """
    Return ingredients that appear in only one dish.
    """

    all_ingredients = set()
    duplicates = set()

    for dish in dishes:
        for ingredient in dish:
            if ingredient in all_ingredients:
                duplicates.add(ingredient)
            else:
                all_ingredients.add(ingredient)

    # Remove duplicates and common intersection ingredients
    return all_ingredients - duplicates - intersection