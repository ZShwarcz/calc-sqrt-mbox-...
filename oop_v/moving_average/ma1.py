import numpy as np

data = open('usd-for-2017-year.txt', mode='r', encoding='utf-8')

output = open('moving_average-usd1.txt', mode='w', encoding='utf-8')

data2 = []

for i in data:
    data2.append(float(i))

class ma:
    def __init__(self, data, window):
        self.window = window
        self.values = data

    def moving_average(self):
        weights = np.repeat(1.0, self.window) / self.window
        smas = np.convolve(self.values, weights, 'valid')
        return smas



window = int(input("Введите размер окна: "))

test = ma(data2, window)

for i in test.moving_average():
    output.write(str(i) + '\n')

data.close()
output.close()