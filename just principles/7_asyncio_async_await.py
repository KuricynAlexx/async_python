# pip (pip3) install aiohttp


# План:
# 1. Asyncio - фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времён Python 3.4
# 3. Синтаксис Async/await на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов

# Event Loop:
#	coroutine > Task (Future)

import asyncio
from time import time

@asyncio.coroutine # определяет функции как генератор (и запускает их) <--- так было в python3.4 и такой код можно встретить на гитхабе
def print_nums():
	num = 1
	while True:
		print(num)
		num += 1
		yield from asyncio.sleep(0.6)


@asyncio.coroutine
def print_time():
	count = 0
	while True:
		if count % 3 == 0:
			print(f"{count} seconds have passed")
		count += 1
		yield from asyncio.sleep(0.6)


@asyncio.coroutine
def main():
	task1 = asyncio.ensure_future(print_nums())
	task2 = asyncio.ensure_future(print_time()) # события попадают в очередь событийного цикла

	yield from asyncio.gather(task1, task2)



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	loop.close()