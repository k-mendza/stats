import numpy as np
import matplotlib.pyplot as plt
import csv

_VALUE_CSV_COL_POSITION_ = 1
_FILE_NAME_ = 'data.csv'
_HISTOGRAM_TITLE_ = 'Histogram'
_X_AXIS_LABEL_ = 'Wartość'
_Y_AXIS_LABEL_ = 'Liczba wystąpień'
_BINS_ = [1, 2, 3, 4, 5, 6, 7]


def getValueArrayFromCSVFile(file_name):
    file_data = []
    with open(file_name, 'r') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            file_data.append(int(row[_VALUE_CSV_COL_POSITION_]))
    return file_data


values_array = np.array(getValueArrayFromCSVFile(_FILE_NAME_))

n, bins, patches = plt.hist(values_array, bins=_BINS_, histtype='bar', rwidth=0.8, color='blue')

mean = values_array.mean()
std_div = values_array.std()
dominant = np.array(n).max()
lower_quantile = np.quantile(values_array, 0.25)
median = np.median(values_array)
upper_quantile = np.quantile(values_array, 0.75)
variance = values_array.var()
change_factor = np.sqrt(variance)/mean*100

print("Wartość średnia: ", mean)
print("Odchylenie standardowe: ", std_div)
print("Dominanta: ", dominant)
print("Kwantyl dolny (rzędu 1/4) ", lower_quantile)
print("Mediana: ", median)
print("Kwantyl górny (rzędu 3.4) ", upper_quantile)
print("Wariancja: ", variance)
print("Współczynnik zmienności: ", change_factor, '%')

plt.title(_HISTOGRAM_TITLE_)
plt.grid(axis='y', alpha=0.75)
plt.xlabel(_X_AXIS_LABEL_)
plt.ylabel(_Y_AXIS_LABEL_)

plt.show()
