import hopfield
import os
import re as regexp

current_path = os.getcwd()
train_paths = []
train_directory = current_path + "/train/"
for i in os.listdir(train_directory):
  if regexp.match(r'[0-9a-zA-Z-]*.jp[e]*g', i):
    train_paths.append(train_directory + i)

test_paths = []
test_directory = current_path + "/test/"
for i in os.listdir(test_directory):
  if regexp.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
    test_paths.append(test_directory + i)

hopfield.calc(train_files=train_paths, test_files=test_paths, a=0.5, time=60000, size=(100, 100), threshold=10,
              current_path=current_path)
