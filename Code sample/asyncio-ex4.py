'''18.5.3.4.1. Example: Future with run_until_complete()'''
import asyncio

@asyncio.coroutine
def slow_operation(future):
    print("I am slow_operation ")
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print("loop.run_until_complete done ")
print(future.result())
loop.close()