from pycbrf import ExchangeRates

mounth = 1
count = 0
output = open('usd-for-2018-year.txt', mode='w', encoding='utf-8')

while mounth <= 3:
    if mounth == 2:
        n = 28
    elif mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8 or mounth == 10 or mounth == 12:
        n = 31
    else:
        n = 30
    for day in range(1, n+1):
        rates = ExchangeRates('2018-' + str(mounth) + '-' + str(day), locale_en=True)
        output.write(str(rates['USD'].value) + '\n')
        count += 1
        print(count)
    mounth += 1

output.close()
