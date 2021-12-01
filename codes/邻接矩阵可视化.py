from PIL import Image
import numpy as np
'''
inward_ori_index = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                    (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                    (20, 19), (22, 23), (23, 8), (24, 25), (25, 12)]
'''
inward_ori_index = [(1, 3), (2, 3), (3, 4), (4, 5)]

inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]

outward = [(j, i) for (i, j) in inward]

total = inward + outward





A = np.zeros((5, 5))
for (i,j) in total:
    A[i,j] = 1
print(A)

D = np.zeros((5,5))
for i in range(5):
    D[i,i] = sum(A[i, :]) + 1
print(D)
#img = np.reshape(A,(25,25))
#img = Image.fromarray(np.uint8(D))
#img.show()

L = np.zeros((5,5))
L = D - A
img = Image.fromarray(np.uint8(L))
img.show()
print(L)