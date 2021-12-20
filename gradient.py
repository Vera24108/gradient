import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)
    image[i, :, :] = [r, g, b]

val = np.linspace(0, 255, image.shape[0]+image.shape[0])
val2 = list(reversed(val))

for i in range(100):
    val3 =  val2[i::]
    val4 = val[i::]
    
    for j in range(100):
            
        image[i][j][0] = val3[j]
        image[j][i][-1] = val4[j]
        

plt.figure(1)
plt.imshow(image)
plt.show()