import asyncio
import json
from json import JSONDecodeError
from motor_handler import MotorHandler
from websocket_command import WebsocketCommand
from websocket_command import WebsocketCommandType
from websockets.exceptions import ConnectionClosed
from websockets.server import serve

ip = "0.0.0.0"
port = 8765

motor_handler = MotorHandler()
motor_handler.init()

async def handler(websocket):
    print(f"handler {websocket}")
    try:
        async for message in websocket:
            try:
                print(f'Received a message ${message}')
                data_dict = json.loads(message)
                command = WebsocketCommand(**data_dict) 
                print(f"Command parsed ${command}")
                print(f"Type == {command.type} {type(command.type)}")
                if command.type is WebsocketCommandType.MOTOR:
                    print(f"Motor change")
                    motor_handler.set(command.x, command.y)
                    # return await websocket.send("{\"processed\": true}")
                # return await websocket.send("{\"processed\": false}")
            except JSONDecodeError:
                print("Incorrect JSON")
    except ConnectionClosed:
        motor_handler.stop()
        print("Connection closed!")

async def main():
    print(f"Starting server on {ip}:{port}")
    async with serve(handler, ip, port):
        await asyncio.Future()  # run forever

asyncio.run(main())