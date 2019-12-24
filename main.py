import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv

_VALUE_CSV_COL_POSITION_ = 1
_FILE_NAME_ = 'data.csv'
_HISTOGRAM_TITLE_ = 'Histogram'
_X_AXIS_LABEL_ = 'Wartość'
_Y_AXIS_LABEL_ = 'Liczba wystąpień'
_BINS_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]


def getValueArrayFromCSVFile(file_name):
    file_data = []
    with open(file_name, 'r') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            file_data.append(float(row[_VALUE_CSV_COL_POSITION_]))
    return file_data


values_array = np.array(getValueArrayFromCSVFile(_FILE_NAME_))
# statistics for file data
mean = values_array.mean()
std_div = values_array.std()
lower_quantile = np.quantile(values_array, 0.25)
median = np.median(values_array)
upper_quantile = np.quantile(values_array, 0.75)
variance = values_array.var()
change_factor = np.sqrt(variance)/mean*100

stats.norm(mean, std_div)
synthetic_value_array = np.random.normal(mean, std_div, 1000)

plt.hist(values_array, bins=_BINS_, histtype='bar', rwidth=0.8, color='blue')
plt.hist(synthetic_value_array, bins=_BINS_, histtype='bar', rwidth=0.8, color='red')

plt.legend(['Dane oryginalne','Dane porównawcze'])

print("Wartość średnia (Mean): ", mean)
print("Odchylenie standardowe (Standard deviation): ", std_div)
print("Kwantyl dolny (rzędu 1/4) ", lower_quantile)
print("Mediana (Median): ", median)
print("Kwantyl górny (rzędu 3.4) ", upper_quantile)
print("Wariancja (Variation): ", variance)
print("Współczynnik zmienności: ", change_factor, '%')

plt.title(_HISTOGRAM_TITLE_)
plt.grid(axis='y', alpha=0.75)
plt.xlabel(_X_AXIS_LABEL_)
plt.ylabel(_Y_AXIS_LABEL_)

plt.show()
