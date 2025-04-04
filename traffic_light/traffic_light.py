from enum import Enum


class TrafficLight(Enum):
    RED = "RED"
    RED_WHILE_FLASHING_GREEN = "RED_WHILE_FLASHING_GREEN"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    FLASHING_GREEN = "FLASHING_GREEN"
    YELLOW_TO_RED = "YELLOW_TO_RED"

class TrafficLightState:

    def __init__(self, state: int):
        if state == 1:
            self.state = TrafficLight.RED
        if state == 2:
            self.state = TrafficLight.RED_WHILE_FLASHING_GREEN
        elif state == 3:
            self.state = TrafficLight.YELLOW
        elif state == 4:
            self.state = TrafficLight.GREEN
        elif state == 5:
            self.state = TrafficLight.FLASHING_GREEN
        elif state == 6:
            self.state = TrafficLight.YELLOW_TO_RED
        else:
            self.state = TrafficLight.RED

    def next_value(self):
        if self.state == TrafficLight.RED:
            self.state = TrafficLight.RED_WHILE_FLASHING_GREEN
        elif self.state == TrafficLight.RED_WHILE_FLASHING_GREEN:
            self.state = TrafficLight.YELLOW
        elif self.state == TrafficLight.YELLOW:
            self.state = TrafficLight.GREEN
        elif self.state == TrafficLight.GREEN:
            self.state = TrafficLight.FLASHING_GREEN
        elif self.state == TrafficLight.FLASHING_GREEN:
            self.state = TrafficLight.YELLOW_TO_RED
        elif self.state == TrafficLight.YELLOW_TO_RED:
            self.state = TrafficLight.RED

    def get_state(self):
        return self.state.value

    def to_json(self):
        return {"state": self.state.value}