import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
# import k_means
import math

im0 = Image.open('im0.ppm')
im8 = Image.open('im8.ppm')
left_image = np.asarray(im0, dtype="int32")
right_image = np.asarray(im8, dtype="int32")

lengthL, widthL, heightL = left_image.shape
lengthR, widthR, heightR = right_image.shape

# f = open('disparity.tdispFlatt','w')
# f.write("{")
window_size = 40
disparity_matrix = np.zeros((left_image.shape[0], left_image.shape[1] - window_size))
for i in range(lengthR):
    for j in range(widthR - window_size):
        temp = []
        for k in range(j, j + window_size):
            temp.append(np.linalg.norm(right_image[i][j] - left_image[i][k]))
        disparity_matrix[i][j] = np.min(temp)
        # disparity_matridispFlat[i] = np.array(disparity_matridispFlat[i])
        # f.write(str(disparity_matridispFlat[i])+",")
# f.write("}")
# f.close()
'''
dispFlat = np.ndarray.flatten(disparity_matrix)


dispFlat = dispFlat/max(dispFlat)

dispFlat = dispFlat*255

dispFlat = 255 - dispFlat

dispFlat = np.reshape(dispFlat, (381,390))

new_p = Image.fromarray(dispFlat)
if new_p.mode != 'RGB':
    new_p = new_p.convert('RGB')



new_p.save('depth.jpg')

'''
'''

#def mean(numbers):
#    return float(sum(numbers)) / madispFlat(len(numbers), 1)

mydict = {}

for i in range(len(dispFlat)):
	mydict[i] = dispFlat[i]



from sklearn.cluster import KMeans
'''

# depth_map_kmeans = (k_means.call_kmeans(disparity_matrix, 3))

# depth_map_kmeans = np.array(depth_map_kmeans)



# print(len(depth_map_kmeans))

# print(len(depth_map_kmeans[0][0]),len(depth_map_kmeans[1][0]),len(depth_map_kmeans[2][0]),len(depth_map_kmeans[0]),len(depth_map_kmeans[1]),len(depth_map_kmeans[2]), type(depth_map_kmeans))

# print(depth_map_kmeans)

'''
print(len(depth_map_kmeans[0]), np.mean(depth_map_kmeans[0]) )
a = len(depth_map_kmeans[0])
b = np.mean(depth_map_kmeans[0])
print(len( [np.mean(depth_map_kmeans[0])]*len(depth_map_kmeans[0])))

'''
'''
depth_map_kmeans[0] = np.array(depth_map_kmeans[0])
depth_map_kmeans[1] = np.array(depth_map_kmeans[1])
depth_map_kmeans[2] = np.array(depth_map_kmeans[2])

print("0 \n")
print(depth_map_kmeans[0])
print("1 \n")
print(depth_map_kmeans[1])
print("2 \n")
print(depth_map_kmeans[2])
depth_map_kmeans[0] = np.full(depth_map_kmeans[0].shape, np.mean(depth_map_kmeans[0]))
depth_map_kmeans[1] = np.full(depth_map_kmeans[1].shape, np.mean(depth_map_kmeans[1]))
depth_map_kmeans[2] = np.full(depth_map_kmeans[2].shape, np.mean(depth_map_kmeans[2]))

#mean nikala clusters ka, abi aise assign karna he ki har pidispFlatel position wo ye value mile 
'''

'''


#print((depth_map_kmeans[0].shape))
#print((depth_map_kmeans[1].shape))
#print((depth_map_kmeans[2].shape))

#depth_map_kmeans = np.vstack((depth_map_kmeans[0],depth_map_kmeans[1],depth_map_kmeans[2]))
#len = 381 of 390 elements

#print( depth_map_kmeans[0])
depth_map_kmeans = np.array(depth_map_kmeans)
print(depth_map_kmeans.shape)

'''

vectorized = np.ndarray.flatten(disparity_matrix)
# len = 381*390

# newImage = np.reshape(vectorized, (381,390))



new_p = Image.fromarray(disparity_matrix)
if new_p.mode != 'RGB':
    new_p = new_p.convert('RGB')

new_p.save('depth2.jpg')

# print(vectorized.shape)
vectorized = np.ndarray.flatten(disparity_matrix)
plt.hist(vectorized)
plt.show()
