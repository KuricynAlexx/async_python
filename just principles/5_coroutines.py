# coroutines - это сопрограммы, ккоторые могут принимать извне какие-то данные,
# которые делаются методом send() (есть такой метод у генераторов)

def coroutine(func):
	def inner(*args, **kwargs):
		g = func(*args, **kwargs)
		g.send(None)
		return g
	return inner

def subgen():
	message = yield
	print('Subgen received:', message)


class BlaBlaException(Exception):
	pass



@coroutine
def average():
	count = 0
	summ = 0
	average = None

	while True:
		try:
			x = yield average
		except StopIteration:
			print('Done')
		except BlaBlaException:
			print('..........................')
		else:
			count += 1
			summ += x
			average = round(summ / count, 2)