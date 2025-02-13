import asyncio

loop = asyncio.new_event_loop()
# print('Event loop created')
# loop = asyncio.get_running_loop()


# print('This will run infinitely')

# this will run infinitely and 'done' will never be printed
# loop.run_forever()



# # check status
# print(f'running={loop.is_running()}, closed={loop.is_closed()}')
# # run a task
# loop.run_until_complete(asyncio.sleep(0.5))
# # check status
# print(f'running={loop.is_running()}, closed={loop.is_closed()}')
# # close the event loop
# loop.close()
# # check status
# print(f'running={loop.is_running()}, closed={loop.is_closed()}')


async def task_coroutine(value):
    print(f'Task {value} is running')
    await asyncio.sleep(1)
    return f"Task {value} is done"


def handlecallback(task):
    print('Task completed')
    print(task.result())

task = asyncio.ensure_future(task_coroutine(1), loop=loop)
# print(task)
print(task.done()) # False
loop.run_until_complete(task)
print(task.done()) # True
print(task.result()) # Task 1 is done

print(f"Task name is : {task.get_name()}")
task.add_done_callback(handlecallback)

