import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from car.car import NumberTrafficLightValidation
from car.car_factory import create_five_cars_by_traffic_light, create_cars_for_two_minute
from producer import connect_with_rabbit_mq
from traffic_light.traffic_light_factory import start_traffic_light

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(connect_with_rabbit_mq())
    asyncio.create_task(start_traffic_light())


@app.post("/enable_creating_cars")
async def root():
    asyncio.create_task(create_cars_for_two_minute())
    return JSONResponse(status_code=200, content={"message": "Success"})


@app.post("/create_traffic_light")
async def create_five_cars(number_traffic_light: NumberTrafficLightValidation):
    await create_five_cars_by_traffic_light(number_traffic_light.number_traffic_light)
    return JSONResponse(status_code=200, content={"message": "Success"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
