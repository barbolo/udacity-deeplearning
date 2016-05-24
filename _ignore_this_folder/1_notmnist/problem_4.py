import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pickle

pickle_file = 'notMNIST.pickle'
datasets = pickle.load( open(pickle_file, 'rb') )

def save_image(dataset, name):
  index = np.random.choice(len(dataset))
  image = dataset[index]
  plt.imshow(image)
  plt.savefig('problem_4_%s.png' % name)

save_image(datasets['train_dataset'], 'train')
save_image(datasets['valid_dataset'], 'valid')
save_image(datasets['test_dataset'], 'test')
