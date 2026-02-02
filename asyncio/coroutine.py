# async def fetch_data():
#     return {"data": "Success"}

# # Just calling it does nothing
# coro = fetch_data() 
# print(coro)  # <coroutine object fetch_data at ...>

# async def main():
#     # Pauses main(), lets other tasks run during the 1-second sleep
#     result = await fetch_data() 
#     print(result)

import asyncio

# async def say_hello():
#     await asyncio.sleep(1) # Non-blocking delay
#     print("Hello!")

# # Starts the Event Loop and runs the coroutine to completion
# asyncio.run(say_hello())

# async def prepare_coffee():
#     print("Starting coffee...")
#     # This is where the pause happens
#     await asyncio.sleep(2) 
#     print("Coffee ready!")
#     return "Cappuccino"


# dd = asyncio.run(prepare_coffee())
# print(dd)

import asyncio
import time

async def fetch_user():
    await asyncio.sleep(1) # Simulates DB
    return "User: Khushal"

async def fetch_posts():
    await asyncio.sleep(1) # Simulates DB
    return ["Post 1", "Post 2"]

async def main():
    start_time = time.perf_counter()

    # We start both 'Futures' at the exact same time
    # Instead of taking 2 seconds, it takes only 1!
    results = await asyncio.gather(fetch_user(), fetch_posts())

    end_time = time.perf_counter()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())