import json
import uuid

from redis import Redis

from car.car import Car
from config import REDIS_HOST, REDIS_PORT


class RedisImplementation:
    def __init__(self, number_db: int):
        self.redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=number_db)

    def insert_item(self, key: uuid.UUID, value: Car):
        self.redis_client.set(f"{key}", json.dumps(value.to_dict()))
        print(value)