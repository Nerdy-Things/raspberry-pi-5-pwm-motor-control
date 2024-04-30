import asyncio
import json
from json import JSONDecodeError
from motor_handler import MotorHandler
from websocket_command import WebsocketCommand
from websocket_command import WebsocketCommandType
from websockets.exceptions import ConnectionClosed
from websockets.server import serve

PING_INTERVAL = 5  
PING_MESSAGE = "PING"
PONG_TIMEOUT = 3 

ip = "0.0.0.0"
port = 8765

motor_handler = MotorHandler()
motor_handler.init()

ping_tasks = {}

async def handler(websocket):
    ping_tasks[websocket] = asyncio.create_task(ping_sender(websocket))
    try:
        while True:
            message = await websocket.recv()
            print(f'Received a message ${message}')
            try:
                if message == "pong":
                    continue
                data_dict = json.loads(message)
                command = WebsocketCommand(**data_dict) 
                print(f"Command parsed ${command}")
                print(f"Type == {command.type} {type(command.type)}")
                if command.type is WebsocketCommandType.MOTOR:
                    print(f"Motor change")
                    motor_handler.set(command.x, command.y)
            except JSONDecodeError:
                print("Incorrect JSON")
    except ConnectionClosed:
        print("Connection closed!")
        motor_handler.stop()
    finally:
        if websocket in ping_tasks:  # Check if websocket exists before cancellation
            ping_tasks[websocket].cancel()
            ping_tasks.pop(websocket)

async def ping_sender(websocket):
    while True:
        await asyncio.sleep(PING_INTERVAL)
        try:
            await websocket.send(PING_MESSAGE)
            await asyncio.wait_for(websocket.recv(), timeout=PONG_TIMEOUT)  # Wait for pong
        except (asyncio.TimeoutError, ConnectionClosed):
            print("Ping timeout, connection might be closed")
            break

async def main():
    print(f"Starting server on {ip}:{port}")
    async with serve(handler, ip, port):
        await asyncio.Future()  # run forever

asyncio.run(main())