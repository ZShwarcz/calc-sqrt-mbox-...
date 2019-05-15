import numpy as np

data = open('usd-for-2018-year.txt', mode='r', encoding='utf-8')

output = open('moving_average-usd.txt', mode='w', encoding='utf-8')

data2 = []

for i in data:
    data2.append(float(i))


def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


for i in moving_average(data2, 3):
    output.write(str(i) + '\n')

data.close()
output.close()
