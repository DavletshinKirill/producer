import asyncio
import random
import time
import uuid

from car.car import Direction, Car, NumberTrafficLight
from redis_service import create_item


def create_car_without_parameters():
    car_id = uuid.uuid4()
    direction = random.randint(1, 3)
    number_traffic_light = random.randint(1, 4)
    return Car(id = car_id, direction = create_direction(direction), number_traffic_light = create_number_traffic_light(number_traffic_light))

def create_car_by_number_traffic_light(number_traffic_light: NumberTrafficLight):
    direction = random.randint(1, 3)
    car_id = uuid.uuid4()
    return Car(id = car_id, number_traffic_light = number_traffic_light, direction = create_direction(direction))

def create_direction(direction_index: int):
    if direction_index == 1:
        return Direction.AHEAD
    elif direction_index == 2:
        return Direction.RIGHT
    elif direction_index == 3:
        return Direction.LEFT

def create_number_traffic_light(number_traffic_light: int):
    if number_traffic_light == 1:
        return NumberTrafficLight.FIRST
    elif number_traffic_light == 2:
        return NumberTrafficLight.SECOND
    elif number_traffic_light == 3:
        return NumberTrafficLight.THIRD
    elif number_traffic_light == 4:
        return NumberTrafficLight.FOURTH


async def create_cars_for_two_minute():
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 120:
            break
        car = create_car_without_parameters()
        print(f"Car was sent to topic")
        create_item(car)
        await asyncio.sleep(1)

async def create_five_cars_by_traffic_light(number_traffic_light: NumberTrafficLight):
    for _ in range(5):
        car = create_car_by_number_traffic_light(number_traffic_light)
        create_item(car)