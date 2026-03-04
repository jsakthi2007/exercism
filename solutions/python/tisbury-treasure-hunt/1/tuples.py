"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = rui_record[1]
    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],  # treasure
            azara_record[1],  # original coordinate string (e.g. "5B")
            rui_record[0],    # location
            rui_record[1],    # coordinate tuple (e.g. ('5', 'B'))
            rui_record[2],    # quadrant
        )
    return "not a match"


def clean_up(combined_record_group):
    result = ""

    for record in combined_record_group:
        treasure = record[0]
        location = record[2]
        coordinate_tuple = record[3]
        quadrant = record[4]

        cleaned_tuple = (treasure, location, coordinate_tuple, quadrant)

        result += f"{cleaned_tuple}\n"

    return result