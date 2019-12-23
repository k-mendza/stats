import numpy as np
import matplotlib.pyplot as plt
import csv

_VALUE_CSV_COL_POSITION_ = 1
_FILE_NAME_ = 'data.csv'
_HISTOGRAM_TITLE_ = 'Histogram'
_X_AXIS_LABEL_ = 'Wartość'
_Y_AXIS_LABEL_ = 'Liczba wystąpień'


def getValueArrayFromCSVFile(file_name):
    file_data = []
    with open(file_name, 'r') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            file_data.append(int(row[_VALUE_CSV_COL_POSITION_]))
    return file_data


values_array = np.array(getValueArrayFromCSVFile(_FILE_NAME_))

plt.hist(values_array, bins='auto', histtype='bar', rwidth=0.8, color='blue')
plt.title(_HISTOGRAM_TITLE_)
plt.grid(axis='y', alpha=0.75)
plt.xlabel(_X_AXIS_LABEL_)
plt.ylabel(_Y_AXIS_LABEL_)

plt.show()
