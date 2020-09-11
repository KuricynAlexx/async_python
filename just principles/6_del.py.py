# Делигирующий генератор - это тот генератор, который вызывает другой генератор

def coroutine(func):
	def inner(*args, **kwargs):
		g = func(*args, **kwargs)
		g.send(None)
		return g
	return inner

class BlaBlaException(Exception):
	pass


def subgen():
	while True:
		try:
			message = yield
		except StopIteration:
			print('Ku-Ku!')
		else:
			print('......', message)


@coroutine
def delegator(g):
	# while True:
	#	try:
	#		data = yield
	#		g.send(data)
	#	except BlaBlaException as e:
	#		g.throw(e)

	yield from g