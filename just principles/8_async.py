import requests
from time import time



def get_file(url):
	r = requests.get(url, allow_redirects=True)
	return r


def write_file(response):
	# https://loremflickr.com/cache/resized/65535_49845303721_80df43c416_320_240_nofilter.jpg
	filename = response.url.split('/')[-1]
	with open(filename, 'wb') as file:
		file.write(response.content) # бинарные данные - содержание ответа сервера -
									 # находятся в аттрибуте .content


def main():
	url = 'https://loremflickr.com/320/240'

	for i in range(10):
		write_file(get_file(url))

	
if __name__ == '__main__':
	t0 = time()
	main()
	print(time() - t0)


####################################
# Async-version

import asyncio
import aiohttp

# Документация библиотеки aiohttp говорит, что лучше
# все запросы делать черз созданную сессию (корутины)


# пишем синхронную функцию записи изображений (но прирост производительности всё равно будет)
def write_image(data):
	filename = 'file-{}.jpeg'.format(int(time() * 1000))
	with open(filename, 'wb') as file:
 		file.write(data)

async def fetch_content(url, session):
	# асинхронный контекстный менеджер 'async with'
	async with session.get(url, allow_redirects=True) as response:
		# все объекты в асинхронном фреймворке - это генераторы и корутины.
		# и методы - они тоже ассинхронны. Поэтому для вызова
		# ассинхронного метода мы используем c await
		data = await response.read() # <--- возвращает бинарные данные
		write_image(data)
		# Вообще, смешивать сихронный код с асинхронным -- плохая идея,
		# ибо в какой-то момент может всё встать

async def main2():
	url = 'https://loremflickr.com/320/240'

	# здесь нужно открыть сессию и внутри сессии вызвать
	# 10 раз корутину fetch_content
	tasks = []

	async with aiohttp.ClientSession() as session:
		for i in range(10):
			# здесь по идеи надо вызвать fetch content, но это корутин,
			# а корутины передаются в событийный цикл, и потом уже
			# в событийном цикле вызываются и обрабатываются для исполнения.
			# Чтобы корутин попал в событийный цикл, его необходимо 
			# обернуть в class task с помощью функции '.create_task()'
			task = asyncio.create_task(fetch_content(url, session))
			tasks.append(task)

		# дожидаемся результата работы этих (выше) корутин.
		# т.е. вызвать метод .gather()
		await asyncio.gather(*tasks)
		# gather принимает расспакованные последовательности,
		# поэтому для расспакованных последовательностей используем звездочку.


#if __name__ == '__main__':
#	t0 = time()
#	asyncio.run(main2())
#	print(time()-t0)