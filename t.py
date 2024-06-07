import asyncio

import asyncio

async def fetch_data_1():
    print("Start fetching data 1...")
    await asyncio.sleep(2)  # Simulate a network request with a 2-second delay
    print("Data 1 fetched")
    return {"data": "sample data 1"}

async def fetch_data_2():
    print("Start fetching data 2...")
    await asyncio.sleep(1)  # Simulate a network request with a 3-second delay
    print("Data 2 fetched")
    return {"data": "sample data 2"}

async def main():
    task1 = asyncio.create_task(fetch_data_1())
    task2 = asyncio.create_task(fetch_data_2())

    # Wait for both tasks to complete
    results = await asyncio.gather(task1, task2)

    print(a)
    print(results)

# Run the main function
asyncio.run(main())
