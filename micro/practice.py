from multiprocessing import Process, Array

"""result = []


def squr(arr):
    global result
    for i in arr:
        print(i * i)
        result.append(i * i)

    print(result)


if __name__ == "__main__":
    arr = [10, 20, 30, 40]

    p1 = Process(target=squr, args=(arr,))
    p1.start()
    p1.join()
    print(result)"""


def squr(arr, shared_memory):
    for index, i in enumerate(arr):
        print(i * i)
        shared_memory[index] = i * i
    print(shared_memory[:])


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    shared_memory = Array("i", 5)
    p1 = Process(target=squr, args=(arr, shared_memory))
    p1.start()
    p1.join()

    print(shared_memory[:])
