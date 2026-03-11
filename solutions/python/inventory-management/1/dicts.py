"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element in items list."""
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from items list."""
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory without allowing negative values."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item completely from inventory if it exists."""
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    """Return list of (item_name, item_count) pairs where count > 0."""
    return [(item, count) for item, count in inventory.items() if count > 0]