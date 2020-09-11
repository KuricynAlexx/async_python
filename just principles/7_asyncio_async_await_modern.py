# pip (pip3) install aiohttp

import asyncio
from time import time


async def print_nums():
	num = 1
	while True:
		print(num)
		num += 1
		await asyncio.sleep(0.2) # <--- в python3.5 'yield from' was placed by 'await'

# вызов ассинхронной функции вызывается с помощью метода await

async def print_time():
	count = 0
	while True:
		if count % 3 == 0:
			print(f"{count} seconds have passed")
		count += 1
		await asyncio.sleep(0.2)


async def main():
	task1 = asyncio.create_task(print_nums()) # <--- В python3.6 создавать таски нужно теперь
	task2 = asyncio.create_task(print_time()) # создавать с помощью create_task

	await asyncio.gather(task1, task2)



if __name__ == '__main__':
	#loop = asyncio.get_event_loop()
	#loop.run_until_complete(main())
	#loop.close()
	asyncio.run(main()) # с python3.7 .run() заменяет всю конструкцию выше