import uuid

from redis import Redis

from car.car import Car


class RedisImplementation:
    def __init__(self, number_db: int):
        self.redis_client = Redis(host='localhost', port=6379, db=number_db)

    def insert_item(self, key: uuid.UUID, value: Car):
        self.redis_client.set(str(key), value.to_dict())