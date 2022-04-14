import asyncio
from receive import main as main_receive
from send import send

async def main():
    asyncio.ensure_future(main_receive())
    while True:
        send(input('Mensagem: '))
        await asyncio.sleep(0.5)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Interrupted')