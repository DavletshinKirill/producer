import uuid
from enum import Enum

from pydantic import BaseModel

class Direction(Enum):
    AHEAD = "AHEAD"
    RIGHT = "RIGHT"
    LEFT = "LEFT"

class NumberTrafficLight(Enum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3

class Car(BaseModel):
    id: uuid.UUID
    direction: Direction
    number_traffic_light: NumberTrafficLight

    def to_dict(self):
        return {
            "direction": self.direction.value,
            "number_traffic_light": self.number_traffic_light.value,
        }

class NumberTrafficLightValidation(BaseModel):
    number_traffic_light: NumberTrafficLight