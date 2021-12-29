import math

def get_total_building_volume(buildings: []) -> float:
    sum_total_building_volume = 0
    for building in buildings:
        total_building_volume = 0
        for shape in building["shapes"]:
            shape_quantity = shape.get("quantity", 1)
            if shape["shapeId"] == "cylinder":
                volume = cylinder_volume(shape["shapeDimensions"]["height"], shape["shapeDimensions"]["radius"])
            elif shape["shapeId"] == "cuboid":
                length = shape["shapeDimensions"].get("length")
                width = shape["shapeDimensions"].get("width")
                height = shape["shapeDimensions"].get("height")
                volume = cuboid_volume(length, width, height)
            elif shape["shapeId"] == "square_pyramid":
                baseArea = shape["shapeDimensions"].get("baseArea")
                height = shape["shapeDimensions"].get("height")
                volume = square_pyramid_volume(baseArea, height)
            volume = volume * shape_quantity
            total_building_volume += volume
        print(f'Total volume of {building["buildingName"]}: {total_building_volume}')
        sum_total_building_volume += total_building_volume
    return sum_total_building_volume

def cylinder_volume(height, radius):
    pi = math.pi
    volume = height * pi * radius ** 2
    return volume

def cuboid_volume(length, width, height):
    volume = length * width * height
    return volume

def square_pyramid_volume(baseArea, height):
    volume = (1/3) * baseArea * height
    return volume