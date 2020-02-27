from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
from math import sin, pi
import matplotlib.pyplot as plt

FD = 1000 # частота дискретизации, отсчётов в секунду
N = 100 # длина входного массива, 0.091 секунд при такой частоте дискретизации
pure_sig = array([sin(2.*pi*50.0*t/FD) for t in range(N)])

spectrum = rfft(pure_sig)


plt.plot(arange(N)/float(FD), pure_sig, 'r') # чистый сигнал будет нарисован красным
plt.xlabel(u'Время, c') # это всё запускалось в Python 2.7, поэтому юникодовские строки
plt.ylabel(u'Высота')
plt.title(u'Сигнал 50 Гц')
plt.grid(True)
plt.show()

plt.plot(rfftfreq(N, 1./FD), np_abs(spectrum)/N)

plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Высота')
plt.title(u'Спектр')
plt.grid(True)
plt.show()

N = 100 # sample count
P = 20  # period
D = 10 # width of pulse
signal = arange(N) % P < D

spectrum1 = rfft(signal)

plt.plot(signal)
plt.show()
plt.plot(spectrum1)
plt.show()

