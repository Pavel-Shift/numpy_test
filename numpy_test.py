import numpy as np

array = np.rint(10 * np.random.rand(3, 3))
print(array)

array_sort_x = np.sort(array, axis = 1)
print( array_sort_x)

array_podschet_x = np.count_nonzero(array, axis= 1)
print(array_podschet_x)