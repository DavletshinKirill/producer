from car.car import Car
from redis_crud import RedisImplementation

redis_connections = [
    RedisImplementation(0),
    RedisImplementation(1),
    RedisImplementation(2),
    RedisImplementation(3),
]


def create_item(car: Car):
    redis_connections[car.number_traffic_light.value].insert_item(car.id, car)
