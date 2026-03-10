def equilateral(sides):
    return len(set(sides)) == 1 and all(side > 0 for side in sides)


def isosceles(sides):
    return len(set(sides)) <= 2 and all(side > 0 for side in sides) and sum(sides) - max(sides) > max(sides)


def scalene(sides):
    return len(set(sides)) == 3 and all(side > 0 for side in sides) and sum(sides) - max(sides) > max(sides)