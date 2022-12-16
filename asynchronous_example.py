import asyncio
from asyncio import sleep
import httpx


async def count():
    for i in range(10):
        print(i)
        async with httpx.AsyncClient() as client:
            r = await client.get('https://www.example.com/')
            print(f"{r.status_code=}")


async def long_program():
    all_replies = await asyncio.gather(
        *[count() for _ in range(99)]
    )


if __name__ == "__main__":
    asyncio.run(long_program())
