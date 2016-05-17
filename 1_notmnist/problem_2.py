import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy import ndimage

image_file = 'notMNIST_large/A/a29ydW5pc2hpLnR0Zg==.png'
image_data = (ndimage.imread(image_file).astype(float) -
              pixel_depth / 2) / pixel_depth


plt.imshow(image_data)

plt.savefig('problem_2.png')
