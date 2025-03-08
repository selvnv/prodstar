import asyncio
import time

def check_time_async(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        finish = time.time()
        print(f"{func.__name__} finished in {finish - start} s")
        return result
    return wrapper

async def simple_msg(text):
    # Простая корутина, которая возвращает текст
    print(text)


async def square(x):
    # Простая корутина, которая возвращает число в квадрате
    print(x**2)


async def long_operation(msg):
    # Корутина с задержкой 3 секунды
    print(f'Старт задачи {msg}') # точка старта
    await asyncio.sleep(3) # тело функции
    print(f'Конец задачи {msg}') # точка завершения

@check_time_async
async def async_as_serial():
    await simple_msg('Сообщение')

    await long_operation("Длинная задача 1")

    await square(10)

    await long_operation("Длинная задача 2")

@check_time_async
async def async_as_async():
    short_task_msg = asyncio.create_task(simple_msg('Сообщение'))

    long_task_1 = asyncio.create_task(long_operation("Длинная задача 1"))

    short_task_square = asyncio.create_task(square(10))

    long_task_2 = asyncio.create_task(long_operation("Длинная задача 2"))

    for task in asyncio.as_completed((short_task_msg, short_task_square,
                          long_task_1, long_task_2)):
        await task


async def main():
    await async_as_serial()
    await async_as_async()


if __name__ == "__main__":
    asyncio.run(main())
