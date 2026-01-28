import random
import asyncio
async def worker(num):
    tm=[3,3,4,4,2,2,5,1]
    await asyncio.sleep(random.choice(tm))
    return f'{num}-{tm}'
async def main():
    tasks=[asyncio.create_task(worker(i)) for i in range(3)]
    res=await asyncio.gather(*tasks)
    print(res)
asyncio.run(main())

