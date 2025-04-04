from pika import ConnectionParameters, BlockingConnection
from config import *
from traffic_light.traffic_light import TrafficLightState

connection_params = ConnectionParameters(
    host=RABBIT_HOST,
    port=RABBIT_PORT,
)

def connect_with_rabbit_mq():
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue=FIRST_TRAFFIC_LIGHT)
            channel.queue_declare(queue=SECOND_TRAFFIC_LIGHT)
            channel.queue_declare(queue=THIRD_TRAFFIC_LIGHT)
            channel.queue_declare(queue=FOURTH_TRAFFIC_LIGHT)

def send_traffic_lights(topic: str, state: TrafficLightState):
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.basic_publish(
                exchange='',
                routing_key=topic,
                body=state.get_state(),
            )