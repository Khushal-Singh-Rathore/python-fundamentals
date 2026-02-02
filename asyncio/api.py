import asyncio
import httpx  # The async version of 'requests'

async def get_external_api_data():
    # 1. Use an 'async' context manager (like opening a client)
    async with httpx.AsyncClient() as client:
        print("Sending request to third-party API...")
        
        # 2. You MUST await the network call
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        
        # 3. Reading JSON is also often a method call
        data = response.json()
        return data

async def main():
    print("Starting process...")
    # 4. Await our custom function
    data = await get_external_api_data()
    print(f"Data Received: {data['title']}")

asyncio.run(main())