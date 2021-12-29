from .seeqarch import *

def test_total_building_volume():
    buildings = [
        {
            "buildingName": "Main Office",
            "shapes": [
                {
                    "shapeId": "cylinder",
                    "shapeDimensions": {
                        "height": 4,
                        "radius": 2
                    },
                    "quantity": 5
                },
                {
                    "shapeId": "cuboid",
                    "shapeDimensions": {
                        "length": 4,
                        "width": 2,
                        "height": 5
                    }
                },
                {
                    "shapeId": "square_pyramid",
                    "shapeDimensions": {
                        "baseArea": 8,
                        "height": 5
                    },
                    "quantity": 2
                }
            ]
        },
        {
            "buildingName": "Remote Office",
            "shapes": [
                {
                    "shapeId": "cylinder",
                    "shapeDimensions": {
                        "height": 4,
                        "radius": 2
                    }
                }
            ]
        }
    ]

    total_building_volume = get_total_building_volume(buildings)

    assert total_building_volume == 368.2595614112868

def test_cylinder_volume_whole_number():
    buildings = [
        {
            "buildingName": "Main Office",
            "shapes": [
                {
                    "shapeId": "cylinder",
                    "shapeDimensions": {
                        "height": (31/(16 * math.pi)),
                        "radius": 4
                    }
                }
            ]
        }
    ]

    total_building_volume = get_total_building_volume(buildings)

    assert total_building_volume == 31