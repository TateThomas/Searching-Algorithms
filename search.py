'''
Project 1: Searching
CS 2420
Tate Thomas
'''


import random
import multiprocessing as mp
import time


def task(iden):
    '''Returns a random integer in the num_range'''

    num_range = 1000000000
    return random.randint(0, num_range)


def find_chunks(my_range):
    '''Determines how big the chunks are for multiprocessing'''

    processors = mp.cpu_count()
    chunks = my_range // processors

    while True:

        new_chunk = chunks / processors
        difference = new_chunk - round(new_chunk)

        if difference != 0.0:
            break

        chunks = int(new_chunk)

    return chunks


def random_list(length):
    '''Uses multiprocessing and other functions to make and random list by determined length'''

    int_list = []
    chunks = find_chunks(length)

    with mp.Pool() as pool:

        for result in pool.map(task, range(length), chunksize=chunks):
            int_list.append(result)

    return int_list


def linear_search(lyst, target):
    '''Looks at a list one by one to see if the target is in it'''

    index = 0

    for num in lyst:

        if num == target:
            return True

        index += 1

    return False


def binary_search(lyst, target):
    '''Divides list into 2 and continues to divide until it finds the number or it doesn't'''

    high = len(lyst) - 1
    low = 0
    mid = high // 2
    index = mid

    while True:

        if (index < low) or (index > high) or (low > high):
            return False

        if target in (lyst[index], lyst[low], lyst[high]):
            return True

        high -= 1
        low += 1

        if lyst[index] < target:
            high -= mid
            mid = (index - low) // 2
            index -= mid

        elif lyst[index] > target:
            low += mid
            mid = (high - index) // 2
            index += mid

        else:
            return False


def jump_search(lyst, target):
    '''If target is > lyst[index], increment 4, if it is ever less,
       decrement 2, check if its '''

    index = 0

    while True:

        if index < 0:
            return False

        if index > (len(lyst) - 1) or lyst[index] > target:
            index -= 2
            if index >= (len(lyst) - 1):
                return lyst[index - 1] == target
            return target in (lyst[index], lyst[index - 1], lyst[index + 1])

        if lyst[index] == target:
            return True

        index += 4


def main():
    '''Main function for this module'''

    length = 10**7 - 1
    print(f"making list of {length} elements...")
    my_list = random_list(length)
    print("done\n")

    print("sorting list...")
    my_list.sort()
    print("done\n")




    print("====================================")
    print("Testing linear_search()...")
    print("====================================\n")

    print(f"First number ({my_list[0]}): ")

    start = time.perf_counter()
    index1 = linear_search(my_list, my_list[0])
    stop = time.perf_counter()

    print(f"\tFound? {index1}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    middle = len(my_list) // 2
    print(f"Middle number ({my_list[middle]}): ")

    start = time.perf_counter()
    index2 = linear_search(my_list, my_list[middle])
    stop = time.perf_counter()

    print(f"\tFound? {index2}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print(f"End number ({my_list[-1]}): ")

    start = time.perf_counter()
    index3 = linear_search(my_list, my_list[-1])
    stop = time.perf_counter()

    print(f"\tFound? {index3}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (-1): ")

    start = time.perf_counter()
    index4 = linear_search(my_list, -1)
    stop = time.perf_counter()

    if index4 is False:
        print(f"\tFound? {index4}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (1000000000): ")

    start = time.perf_counter()
    index5 = linear_search(my_list, 1000000000)
    stop = time.perf_counter()

    if index5 is False:
        print(f"\tFound? {index5}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds\n")




    print("====================================")
    print("Testing binary_search()...")
    print("====================================\n")

    print(f"First number ({my_list[0]}): ")

    start = time.perf_counter()
    index1 = binary_search(my_list, my_list[0])
    stop = time.perf_counter()

    print(f"\tFound? {index1}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    middle = (len(my_list) // 2) - 1
    print(f"Middle number ({my_list[middle]}): ")

    start = time.perf_counter()
    index2 = binary_search(my_list, my_list[middle])
    stop = time.perf_counter()

    print(f"\tFound? {index2}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print(f"End number ({my_list[-1]}): ")

    start = time.perf_counter()
    index3 = binary_search(my_list, my_list[-1])
    stop = time.perf_counter()

    print(f"\tFound? {index3}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (-1): ")

    start = time.perf_counter()
    index4 = binary_search(my_list, -1)
    stop = time.perf_counter()

    if index4 is False:
        print(f"\tFound? {index4}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (1000000000): ")

    start = time.perf_counter()
    index5 = binary_search(my_list, 1000000000)
    stop = time.perf_counter()

    if index5 is False:
        print(f"\tFound? {index5}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds\n")




    print("====================================")
    print("Testing jump_search()...")
    print("====================================\n")

    print(f"First number ({my_list[0]}): ")

    start = time.perf_counter()
    index1 = jump_search(my_list, my_list[0])
    stop = time.perf_counter()

    print(f"\tFound? {index1}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    middle = (len(my_list) // 2) - 1
    print(f"Middle number ({my_list[middle]}): ")

    start = time.perf_counter()
    index2 = jump_search(my_list, my_list[middle])
    stop = time.perf_counter()

    print(f"\tFound? {index2}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print(f"End number ({my_list[-1]}): ")

    start = time.perf_counter()
    index3 = jump_search(my_list, my_list[-1])
    stop = time.perf_counter()

    print(f"\tFound? {index3}")
    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (-1): ")

    start = time.perf_counter()
    index4 = jump_search(my_list, -1)
    stop = time.perf_counter()

    if index4 is False:
        print(f"\tFound? {index4}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds")


    print("Number not in list (1000000000): ")

    start = time.perf_counter()
    index5 = jump_search(my_list, 1000000000)
    stop = time.perf_counter()

    if index5 is False:
        print(f"\tFound? {index5}")
    else:
        print("\tError")

    total = stop - start
    print(f"\tTotal time: {total:.7f} seconds\n")


if __name__ == "__main__":
    main()
