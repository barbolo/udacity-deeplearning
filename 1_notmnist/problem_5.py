import numpy as np
from scipy.stats import itemfreq
import pickle

def is_duplicate(image1, image2):
  np.array_equal(image1, image2) # we could use a near nuplicate match function

pickle_file = 'notMNIST.pickle'
datasets = pickle.load( open(pickle_file, 'rb') )

datasets = {
  'train' : datasets['train_dataset'],
  'valid' : datasets['valid_dataset'],
  'test'  : datasets['test_dataset']
}

train_size = len(datasets['train'])
valid_size = len(datasets['valid'])
test_size  = len(datasets['test'])

overlaps = {
  'train' : np.full( train_size, False),
  'valid' : np.full( valid_size, False),
  'test'  : np.full( test_size, False)
}

def print_overlaps():
  print
  for name in overlaps:
    frequencies = itemfreq(np.array(overlaps[name]))
    line = np.where(frequencies == True)[0]
    if line.shape[0] > 0:
      count = frequencies[line[0]][1]
    else:
      count = 0
    percentage = count/len(overlaps[name])
    print(name + ': ' + "{0:.02f}%".format(percentage*100))
  print


progress = 0
iterations = valid_size + test_size

for index_valid in range(valid_size):
  progress += 1
  print("{0:.02f}%".format((float(progress)/iterations)*100))
  if progress % 10 == 0: print_overlaps()

  image_valid = datasets['valid'][index_valid]

  for index_test in range(test_size):
    image_test = datasets['test'][index_valid]
    if is_duplicate(image_valid, image_test):
      overlaps['valid'][index_valid] = overlaps['test'][index_valid] = True

  for index_train in range(train_size):
    image_train = datasets['train'][index_valid]
    if is_duplicate(image_valid, image_train):
      overlaps['valid'][index_valid] = overlaps['train'][index_valid] = True

for index_test in range(test_size):
  progress += 1
  print("{0:.02f}%".format((float(progress)/iterations)*100))
  if progress % 10 == 0: print_overlaps()

  image_test = datasets['test'][index_test]

  for index_train in range(train_size):
    image_train = datasets['train'][index_test]
    if is_duplicate(image_test, image_train):
      overlaps['test'][index_test] = overlaps['train'][index_test] = True

