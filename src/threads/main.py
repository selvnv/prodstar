import threading
import time
import random
import uuid

# Количество создаваемых задач / потоков
TASK_COUNT = 10

CORE_COUNT = 3


class Task:
    def __init__(self, description):
        self.id = uuid.uuid4()
        self.description = description

    def __repr__(self):
        return f"Task(description={self.description})"


class Processor:
    def __init__(self, core_count):
        self.core_count = core_count
        self.__semaphore = threading.Semaphore(core_count)

    # Запуск задачи
    def run_task(self, task: Task):
        print(f"{task} recieved")

        # "Закрепить" поток. Ожидать, если все core_count заняты
        self.__semaphore.acquire()

        print(f"=>{task} in progress")
        # Имитировать выполнение задачи
        time.sleep(random.randint(0, 5))

        print(f"\t+{task} finished")

        # "Открепить" поток. Освободить слот для ожидающих задач
        self.__semaphore.release()


def main():
    processor = Processor(CORE_COUNT)

    # Создать экземпляры потоков и соответствующие объекты задач
    threads = [
        threading.Thread(target=processor.run_task, args=[Task(f"Task number {i}")])
        for i in range(TASK_COUNT)
    ]

    # Запустить потоки
    for thread in threads:
        thread.start()

    # Ожидать завершения потоков
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
