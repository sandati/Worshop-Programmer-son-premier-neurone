from array import array
import numpy as np
from util import *

my_matrix = np.array([1, 2, 3])
create_first_matrix(my_matrix)

b = my_new_array()
print(np.shape(b))

a1 = np.array([[1, 3],
               [7, 9]])
a2 = np.array([[1, 3, 6, 7],
               [7, 9, 6, 4],
               [8, 6, 7, 7],
               [7, 9, 3, 4]])
a3 = np.array([[1, 3],
               [7, 9],
               [8, 6],
               [7, 9],
               [3, 3]])

check_random_matrix(a1, a2, a3)

a4 = a3.dot(a1)
check_mul(a4)
