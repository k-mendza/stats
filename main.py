import numpy as np
import matplotlib.pyplot as plt
import csv

_VALUE_CSV_COL_POSITION_ = 1
_FILE_NAME_ = 'data.csv'

VALUES_ARRAY = []

with open(_FILE_NAME_, 'r') as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        VALUES_ARRAY.append(row[_VALUE_CSV_COL_POSITION_])

BINS = [0, 1, 2, 3, 4, 5, 6, 7]  # bins are segments for grouping the chart
HISTOGRAM_TITLE = 'Histogram'
X_AXIS_LABEL = 'Wartość'
Y_AXIS_LABEL = 'Liczba wystąpień'
Y_AXIS_TICKS = [0, 1, 2, 3]
Y_AXIS_LIMIT = 3

plt.hist(VALUES_ARRAY, BINS, histtype='bar', rwidth=0.8, color='blue')
plt.title(HISTOGRAM_TITLE)
plt.grid(axis='y', alpha=0.75)
plt.xlabel(X_AXIS_LABEL)
plt.ylabel(Y_AXIS_LABEL)
plt.yticks(Y_AXIS_TICKS)
plt.ylim(ymax=Y_AXIS_LIMIT)

plt.show()
