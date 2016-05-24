import glob
import pickle
import numpy as np
from scipy import ndimage

train_folder = 'notMNIST_large'
test_folder = 'notMNIST_small'

def print_samples_per_class(folder):
  samples_per_class = {}

  for filepath in glob.glob(folder + "/*.pickle"):
    klass = filepath.split('/')[1].split('.')[0]
    dataset = pickle.load( open(filepath, 'rb') )
    samples_per_class[klass] = len(dataset)

  print
  print('Samples per class (%s)' % folder)
  for klass in sorted(samples_per_class, key=samples_per_class.get, reverse=True):
    print('%s: %s' % (klass, samples_per_class[klass]))


print_samples_per_class(train_folder)
print_samples_per_class(test_folder)

