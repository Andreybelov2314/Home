import random
import asyncio
async def worker(num):
    tm=[1,2,3,4,5,6,6,6]
    waste=random.choice(tm)
    await asyncio.sleep(waste)
    return f'{num}-время выолнения-{waste}'
async def main():
    try:
        async with asyncio.timeout(5):
            task=[asyncio.create_task(worker(i)) for i in range(10)]
            res=await asyncio.gather(*task)
            print(res)
    except TimeoutError:
        print('Привышен лимит выполнения')
asyncio.run(main())