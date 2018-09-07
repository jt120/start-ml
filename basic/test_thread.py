# encoding: utf-8

from concurrent.futures import ThreadPoolExecutor
import time

executor = ThreadPoolExecutor(10)
total_cost = 0
out_count = 100


def echo_num(num1, num2):
    # print(num1, num2)
    # time.sleep(1)
    return num1 + num2


for j in range(out_count):

    start = time.time()
    fs = []
    for i in range(10000):
        f = executor.submit(echo_num, 1, i)
        fs.append(f)

    for f in fs:
        r = f.result()

    cost = time.time() - start
    total_cost += cost

print('====' + str(total_cost / out_count))
"""
1 5
2 6
3 7
result_iterators = executor.map(echo_num, [1, 2, 3], [5, 6, 7])

for result in result_iterators:
    print(result)

"""
