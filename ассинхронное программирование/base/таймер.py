import asyncio
async def tmr():
    print('функция 1 начала работу')
    for i in range(5):
        await asyncio.sleep(3)
        print(f'прошло {i} секунд')
asyncio.run(tmr())