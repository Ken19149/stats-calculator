import numpy, scipy
from scipy.stats import mode, cumfreq

array = []
sorted_arr = []
while True:
    number = input()
    if number != "":
        array.append(int(number))
        sorted_arr = sorted(array)
        print(array)
        print("ascending order:", sorted_arr)
    else:
        print("ascending order:", sorted_arr)
        print("mean:", numpy.mean(sorted_arr))
        print("median:", numpy.median(sorted_arr))
        print("mode:", scipy.stats.mode(sorted_arr)[0])
        print("cumulative frequency/sum:", numpy.cumsum(array))
