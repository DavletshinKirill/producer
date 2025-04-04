import asyncio

from config import FIRST_TRAFFIC_LIGHT, SECOND_TRAFFIC_LIGHT, THIRD_TRAFFIC_LIGHT, FOURTH_TRAFFIC_LIGHT
from producer import send_traffic_lights
from traffic_light.traffic_light import TrafficLightState


class TrafficLightFactory:
    topic_list_traffic_light = [
        FIRST_TRAFFIC_LIGHT,
        SECOND_TRAFFIC_LIGHT,
        THIRD_TRAFFIC_LIGHT,
        FOURTH_TRAFFIC_LIGHT
    ]
    def __init__(self):
        self.traffic_lights = []
        self.traffic_lights.append(TrafficLightState(1))
        self.traffic_lights.append(TrafficLightState(4))
        self.traffic_lights.append(TrafficLightState(1))
        self.traffic_lights.append(TrafficLightState(4))

    def switch_traffic_light(self):
        for index, light in enumerate(self.traffic_lights):
            print(f"Traffic Light {index}: {light.get_state()}")
            send_traffic_lights(self.topic_list_traffic_light[index], light)
            light.next_value()
        print("\n")

async def start_traffic_light():
    traffic_light = TrafficLightFactory()
    while True:
        traffic_light.switch_traffic_light()
        await asyncio.sleep(20)