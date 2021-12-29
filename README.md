# seeqarch

[![CI](https://github.com/fionniepollack/seeqarch/actions/workflows/ci.yml/badge.svg)](https://github.com/fionniepollack/seeqarch/actions/workflows/ci.yml)

3D architecture library for calculating the volume of buildings.

# API Documentation

### get_total_building_volume(buildings: []) -> float
This function takes a list of buildings and returns the total combined volume of all buildings.

An example `buildings` argument is outlined below:
```
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
```

Valid `shapeId`s are as follows:
- `cylinder`
- `cuboid`
- `square_pyramid`

# Developer Notes
### Test via pytest
```
python3 -m venv .venv

source .venv/bin/activate

pip3 install pytest

pytest -vs
```