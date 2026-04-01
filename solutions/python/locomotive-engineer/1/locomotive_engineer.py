"""Functions which help the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons."""
    return [*wagons]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """
    1. Move first two wagons to the end.
    2. Insert missing wagons directly after locomotive (ID = 1).
    """

    # Move first two wagons to the end
    first, second, *rest = each_wagons_id
    reordered = [*rest, first, second]

    # Find locomotive position
    index = reordered.index(1)

    # Unpack around locomotive
    before = reordered[:index]
    loco = reordered[index]
    after = reordered[index + 1:]

    # Insert missing wagons after locomotive
    return [loco, *missing_wagons, *after, *before]


def add_missing_stops(route, **stops):
    """
    Add missing stops to route dictionary.
    Stops are passed as keyword arguments.
    """
    route["stops"] = [*stops.values()]
    return route


def extend_route_information(route, more_route_information):
    """
    Extend route dictionary with additional information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """
    Reorder depot rows so that columns align by color.
    """

    # Deep unpack rows
    (r1c1, r1c2, r1c3), \
    (r2c1, r2c2, r2c3), \
    (r3c1, r3c2, r3c3) = wagons_rows

    return [
        [r1c1, r2c1, r3c1],
        [r1c2, r2c2, r3c2],
        [r1c3, r2c3, r3c3],
    ]