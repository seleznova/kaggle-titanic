import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()
data = []

for row in csv_file_object:
    data.append(row)
data = np.array(data)

<<<<<<< HEAD
print data[0:15, 5]

type(data[0::,5])

numpy.ndarray

=======
print data
>>>>>>> f3ab3901a6b77f2a785e3399ffc3388c71c196f6
